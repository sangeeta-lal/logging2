
import org.eclipse.core.internal.utils.FileUtil;
import org.eclipse.jdt.core.dom.AST;
import org.eclipse.jdt.core.dom.ASTNode;
import org.eclipse.jdt.core.dom.ASTParser;
import org.eclipse.jdt.core.dom.CompilationUnit;
import  static org.eclipse.jdt.core.dom.ASTNode.CATCH_CLAUSE;


import java.io.*;
import java.lang.instrument.ClassDefinition;
import java.io.IOException;
import java.nio.file.FileVisitResult;
import java.nio.file.FileVisitor;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.SimpleFileVisitor;
import java.nio.file.attribute.BasicFileAttributes;
import org.eclipse.jdt.core.dom.*;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
/* ===========================@Author Sangeeta========
 *  * This file is used to create database that can be used by python trainting  module
 *  * This will fill the database with desired features
 *  * http://stackoverflow.com/questions/25871510/extracting-method-call-from-catch-blocks-java
 *  * http://grepcode.com/file/repository.grepcode.com/java/eclipse.org/3.6/org.eclipse.jdt/core/3.6.0/org/eclipse/jdt/core/dom/MethodInvocation.java#MethodInvocation.%3Cinit%3E%28org.eclipse.jdt.core.dom.AST%29
 * */

public class cloudstack_Training_CATCH {


	boolean flag = false;
	String try_content="";
	
	int method_count = 0 ;
	String rawContent = "";
	String method_name = "";
	String method_content="";
	String class_name="";
	String package_name = "";
	String temp_file_path = "";
	//Set using the function of the file
	int id = 0;
	int log_count = 0;
	ArrayList<String> all_file_list= new ArrayList<String>();
	String log_levels_combined = "";
	/*
	String url = "jdbc:mysql://localhost:3306/";
	String driver = "com.mysql.jdbc.Driver";
	String db_name ="logging_level2";
	String userName = "root"; 
	String password = "123";
	String table ="cloudstack_catch_train";	
   // String listing_file_path = "D:\\Research\\Logging\\result\\cloudstack-4.3.0_java_files.txt";
	String listing_file_path = "D:\\Research\\Logging\\result\\temp_files.txt";
	//*/
    //@Note: create this file using create_file_listing.py
	///*
	String folder_path = "";
	String url = "jdbc:mysql://localhost:3307/";
	String driver = "com.mysql.jdbc.Driver";
	String db_name ="logging_level2";
	String userName = "sangeetal"; 
	String password = "sangeetal";
	String table ="cloudstack_catch_train";
	String listing_file_path = "E:\\Sangeeta\\Research\\Logging\\result\\cloudstack-4.3.0_java_files.txt";  
    //*/
	 
    Connection conn=null;	
	java.sql.Statement stmt = null;
		
	public static void main(String[] args) 
	{				    
		cloudstack_Training_CATCH demo = new cloudstack_Training_CATCH();
		demo.conn = demo.initdb(demo.db_name);
		try {
			BufferedReader br =  new BufferedReader(new FileReader(demo.listing_file_path));
			String file_name =  br.readLine();
			while(br!=null)
			{
				System.out.println("Parsing File="+file_name);
				int len = (file_name.split("\\\\")).length;
				demo.package_name = file_name.split("\\\\")[len-2];
				demo.temp_file_path= file_name;//
				demo.id = 0;
				demo.ast_prser(file_name);
				file_name =  br.readLine();
				//br=null;
			}
		} 
		catch (FileNotFoundException e) 
		{
		   System.out.println("Error.. Can ot open the listing file");
			e.printStackTrace();
		}
		catch(IOException e)
		{
			e.printStackTrace();
		}
			
	}
	
public void ast_prser(String file_name)
	{
		try
		{
			
			rawContent = cloudstack_Training_CATCH.readFileToString(file_name);
			
		}catch(Exception e){
			System.out.println();
		}
		ASTParser parser = ASTParser.newParser(AST.JLS3);
		parser.setSource(rawContent.toCharArray());
		parser.setKind(ASTParser.K_COMPILATION_UNIT);
		
		final CompilationUnit cu = (CompilationUnit) parser.createAST(null);
		
		try{
	    cu.accept(
	    		
	    			new ASTVisitor() 
	    				{
	    	            	public boolean visit(ImportDeclaration id) 
	    	            	{
	    	                   Name imp = id.getName();
	    	                //System.out.println("import =" + id.getName().getFullyQualifiedName());
	    	                return false;
	    	                }

	    	               public boolean visit(VariableDeclarationFragment node) 
	    	                { 
	    	                 SimpleName name = node.getName();
	    	                 //System.out.println("var.declaration =" + (name.getFullyQualifiedName() + ":" + cu.getLineNumber(name.getStartPosition())));
	    	                 return false; // do not continue 
	    	                }	    	        
	    	        
	    	               public boolean visit(TypeDeclaration node)
	    	               { 
	    	            	   String name = node.getName().toString();
	    	            	   //System.out.println("   calss declaration =" + name);
	    	            	   class_name = name;
	    	            	   return true; // do not continue 
	    	               }

	    	               public boolean visit(MethodDeclaration method)
	    	               {
	    	            	    //id=0;
	    	        	      	method_name = method.getName().getFullyQualifiedName();
	    	        	       
	    	        	      	try
	    	        	      	{
	    	        	      	  Block methodBlock = method.getBody();
	    	        	      	  String myblock = methodBlock.toString();
	    	        	      	  method_content = methodBlock.toString();
	    	        	      	  method_content =  method_content.replaceAll("\"", " ");
	    	        	      	  method_content =  method_content.replaceAll("\'", " ");
	    	        	      	  method_content = method_content.replaceAll("\\?"," ");
	    	        	      	  method_content = method_content.trim();
	    	        	      	 //myblock = myblock.replaceAll("\\?","a");
	    	        	      	  //System.out.println("Myblock="+myblock);
	    	        	          methodVisitor(myblock);
	    	        	          //visitMethodDeclarion(myblock);
	    	        	      	}catch(java.lang.NullPointerException jnull)
	    	        	      	{
	    	        	      		System.out.println("Method Body in NULL");
	    	        	      		jnull.printStackTrace();	
		    	        	      	reset_parameters();
		    	        	        insert("11", "","");
	    	        	      	}
	    	                   catch(Exception e)
	    	                   {
	    	                    e.printStackTrace();
	    	                    reset_parameters();
	    	        	        //insert("12", "","");
   	        	      	       }
	    	            
	    	                    /*reset_parameters();
	    	        	        insert("13", "",""); 	        	      	
	    	        	      	System.out.println("Hello");*/
	    	        	      	return false;
	    	               }            
	               }
	    	);
		}catch(NullPointerException e) { e.printStackTrace();}
}

public void methodVisitor(String content) 
{
	ASTParser metparse = ASTParser.newParser(AST.JLS3);
    metparse.setSource(content.toCharArray());
    metparse.setKind(ASTParser.K_STATEMENTS);
    Block block = (Block) metparse.createAST(null);

    block.accept(new ASTVisitor() 
    {
          public boolean visit(VariableDeclarationFragment var) {
           // debug("met.var", var.getName().getFullyQualifiedName());
        	//System.out.println("dec");
            return true;
        }

        public boolean visit(SimpleName node) {
            //System.out.println(" Simple Node="+node.toString());
        	//System.out.println("Node");
            return true;
        }        
        public boolean visit(ForStatement myfor) {
           //System.out.println("myfor="+myfor.toString());
           //System.out.println("for");
            return true;
        }        
        public boolean visit(SwitchStatement myswitch) {
            //System.out.println("myswitch="+myswitch.toString());
             return true;
         }
        public boolean visit(DoStatement mydo) {
            //System.out.println("mydo="+mydo.toString());
             return true;
         }
        public boolean visit(WhileStatement mywhile) {
            //System.out.println("mywhile="+mywhile.toString());
             return true;
         }
         
        public boolean visit(IfStatement myif) 
        {
         	
        	
         return true;
        }
                
        
        public boolean visit(TryStatement mytry) {
        	return true;
        }
       
        public boolean visit(CatchClause mycatch)
        {
        	String catch_train_con = "" ;
        	//String parent_content= myif.getParent().toString();
        	 //System.out.println(" parent_content"+parent_content);
             //String mod_method_con = method_content.replaceAll("\n", " ");
             //mod_method_con = method_content.replaceAll("\\s+", " ");
             
             //String mod_myif =  myif.toString().replaceAll("\n", " ");
             //mod_myif =  myif.toString().replaceAll("\\s+", " ");
            
             int catch_pos = mycatch.getStartPosition();
             catch_train_con = method_content.substring(0, catch_pos);
             //catch_train_con = catch_train_con.replace("\n", " ");//make it comment for parsing
           	 catch_train_con = catch_train_con.replace("\"", "\\\"");
           	 catch_train_con = catch_train_con.replace("\'", "\\\'"); 
          	 catch_train_con = catch_train_con.replace("\\\\", " ");
          	// catch_train_con = catch_train_con.replaceAll("\n", " "); //make it comment for parsing
             catch_train_con = catch_train_con.replaceAll("\\s+", " ");
       	
           
             System.out.println("catch VALUE="+catch_train_con+" ENDcatch");
             /*
             int loc = mod_method_con.indexOf(mod_myif);
             
             if(loc==-1)
               {
            	 int if_loc = myif.getStartPosition();
            	 if_train_con = parent_content.substring(0,if_loc);            	 
        	     //System.out.println("loc ="+loc);
        	     System.out.println("expr"+myif.getExpression()+"if train="+if_train_con);
               }
             else
             {
            	if_train_con= mod_method_con.substring(0,loc); 
            	//System.out.println("loc ="+loc);
       	     	System.out.println("expr"+myif.getExpression()+"if train="+if_train_con);
              
             }*/
             
            // catch_train_con = catch_train_con.replaceAll("\n", " ");
             //catch_train_con =catch_train_con.replaceAll("\\s+", " ");
        	
            
            String catch_exp = mycatch.getException().getType().toString();
         	catch_exp = catch_exp.replace("\n", " ");
         	catch_exp = catch_exp.replace("\"", "\\\"");
         	catch_exp = catch_exp.replace("\'", " ");
         	catch_exp = catch_exp.replace("\\\\", " ");
         	
         	String catch_block = mycatch.toString();
         	catch_block = catch_block.replace("\n", " ");
          	catch_block = catch_block.replace("\"", "\\\"");
          	catch_block = catch_block.replace("\'", "\\\'"); 
          	catch_block = catch_block.replace("\\\\", " "); 
            System.out.println("-------------------------------");
          	System.out.println("Class Name="+ class_name);
         	System.out.println("Method Name="+ method_name);
         	System.out.println("Package Name="+ package_name);
         	System.out.println("File Path="+ temp_file_path);
         	System.out.println("Catch Exception="+catch_exp);
          	find_and_set_logging_level(mycatch.toString());
 	        insert(catch_block,catch_exp.toString(),catch_train_con);
 	      	reset_parameters();	
        	
          return true; 
        }

    }
    );
}

/*
public boolean visitMethodDeclarion(String content)
{

	System.out.println("me here");
	ASTParser metparse = ASTParser.newParser(AST.JLS3);
    metparse.setSource(content.toCharArray());
    //metparse.setKind(ASTParser.K_STATEMENTS);
    metparse.setKind(ASTParser.K_CLASS_BODY_DECLARATIONS);
    //Block block = (Block) metparse.createAST(null);
    final CompilationUnit cu = (CompilationUnit) metparse.createAST(null);
	
	try{
    cu.accept(
    		
    			new ASTVisitor() 
    				{
    	    /*if (node.getName().toString().equals("createQuery")) {

        String argument= node.arguments().get(0).toString();

        // process the argument here
    }*/
    	 
    	/*  @Override
          public boolean visit(MethodInvocation node) 
          {
            System.out.println("Node invo"); 
        	  return true;
          }*/
    	
    	  /*public boolean visit(MethodInvocation node) 
    	  {

    		  System.out.println("I am not called");
    	       // if (node.getName().toString().equals("createQuery")) {

    	         //   String argument= node.arguments().get(0).toString();

    	            // process the argument here

    	        //}
    		  
    		  System.out.println("method invocation="+node);

    	        return true;
    	    }*/
    	  
 
  
/*    });
	}catch(Exception e)
	{}
    
    return true;
}
  */  

public void reset_parameters()
{
	log_levels_combined="";
	log_count =0;
	//method_name = "";
	//method_content="";
	//class_name= "";
}
	
private void find_and_set_logging_level(String if_content) 
{
	  // log_count=0;
		Pattern pat = Pattern.compile("([a-zA-Z0-9_\\(\\)]+\\.info\\()");
		Matcher matcher = pat.matcher(if_content);
		while(matcher.find())
		{
		  System.out.println("Start Index ="+matcher.start());	
		  System.out.print("Start index: " + matcher.start());
	      System.out.print(" End index: " + matcher.end() + " ");
	      System.out.println("pattern matched = "+matcher.group(1));
	      log_levels_combined=log_levels_combined+"  "+(matcher.group(1).split("\\.")[1]).split("\\(")[0];
	      
		}	
		
		pat = Pattern.compile("([a-zA-Z0-9_\\(\\)]+\\.trace\\()");
		matcher = pat.matcher(if_content);
		while(matcher.find())
		{
		  System.out.println("Start Index ="+matcher.start());	
		  System.out.print("Start index: " + matcher.start());
	      System.out.print(" End index: " + matcher.end() + " ");
	      System.out.println("pattern matched = "+matcher.group(1));
	      log_levels_combined=log_levels_combined+" "+(matcher.group(1).split("\\.")[1]).split("\\(")[0];
		} 
		
		pat = Pattern.compile("([a-zA-Z0-9_\\(\\)]+\\.debug\\()");
		matcher = pat.matcher(if_content);
		while(matcher.find())
		{
		  System.out.println("Start Index ="+matcher.start());	
		  System.out.print("Start index: " + matcher.start());
	      System.out.print(" End index: " + matcher.end() + " ");
	      System.out.println("pattern matched = "+matcher.group(1));
	      log_levels_combined=log_levels_combined+" "+(matcher.group(1).split("\\.")[1]).split("\\(")[0];;
		} 
		
		pat = Pattern.compile("([a-zA-Z0-9_\\(\\)]+\\.warn\\()");
		matcher = pat.matcher(if_content);
		while(matcher.find())
		{
		  System.out.println("Start Index ="+matcher.start());	
		  System.out.print("Start index: " + matcher.start());
	      System.out.print(" End index: " + matcher.end() + " ");
	      System.out.println("pattern matched = "+matcher.group(1));
	      log_levels_combined=log_levels_combined+" "+(matcher.group(1).split("\\.")[1]).split("\\(")[0];;
		} 
		
		pat = Pattern.compile("([a-zA-Z0-9_\\(\\)]+\\.error\\()");
		matcher = pat.matcher(if_content);
		while(matcher.find())
		{
		  System.out.println("Start Index ="+matcher.start());	
		  System.out.print("Start index: " + matcher.start());
	      System.out.print(" End index: " + matcher.end() + " ");
	      System.out.println("pattern matched = "+matcher.group(1));
	      log_levels_combined=log_levels_combined+" "+(matcher.group(1).split("\\.")[1]).split("\\(")[0];;
		} 
		
		pat = Pattern.compile("([a-zA-Z0-9_\\(\\)]+\\.fatal\\()");
		matcher = pat.matcher(if_content);
		while(matcher.find())
		{
		  System.out.println("Start Index ="+matcher.start());	
		  System.out.print("Start index: " + matcher.start());
	      System.out.print(" End index: " + matcher.end() + " ");
	      System.out.println("pattern matched = "+matcher.group(1));
	      log_levels_combined=log_levels_combined+" "+(matcher.group(1).split("\\.")[1]).split("\\(")[0];;
		} 
		
		if(log_levels_combined!="")
		{
		log_count= log_levels_combined.trim().split(" ").length;
		}
		//System.out.println("Final Log levels are:"+log_levels_combined);
} 

public void insert(String if_block, String expr_type, String if_train_con)
{
	//log_count=1;
    id++;
    int logged= 0;
    
    if(log_count!=0)
    {
    	logged =1;
    }
    String insert_str= "insert into "+table+" values(\""+package_name+"\",\""+class_name+"\",\""+method_name+"\","+  id+",\""+method_content+"\",\""+
    log_levels_combined+"\",\""+temp_file_path+"\","+"\""+if_block+"\",\""+expr_type+"\","+log_count+",\""
    +if_train_con+"\","+logged+")";
    System.out.println("Insert str"+insert_str);
    try 
    	{
    		if(conn==null)
    			{
    				//System.out.println("I am null");
    			}
    		stmt =  conn.createStatement();
    		stmt.executeUpdate(insert_str);
    	} catch (SQLException e)
    	{ // TODO Auto-generated catch block
    		e.printStackTrace();
    	}
}
	
public static String readFileToString(String filePath) throws IOException
	{
	    StringBuilder fileData = new StringBuilder(1000);
	    BufferedReader reader = new BufferedReader(new FileReader(filePath));

	    char[] buf = new char[10];
	    int numRead = 0;
	    while ((numRead = reader.read(buf)) != -1) {
	        //          System.out.println(numRead);
	        String readData = String.valueOf(buf, 0, numRead);
	        fileData.append(readData);
	        buf = new char[1024];
	    }
	    reader.close();
	    return  fileData.toString();    
	}
	
public Connection initdb(String db_name)
{
	 try {
		      Class.forName(driver).newInstance();
		      conn = DriverManager.getConnection(url+db_name,userName,password);
		      if(conn==null)
		      {
		    	  System.out.println("Hi I am null :( :(");
		      }
		      
		 } catch (Exception e) 
		 {
		      e.printStackTrace();
		 }
		return conn;
}

}//main



/*
public void visit(final MethodCallExpr n, final Void arg)
{
    System.out.println(n);
    super.visit(n, arg);
}

@Override
public boolean visit(MethodInvocation node) {
    if (invocationsForMethods.get(activeMethod) == null) {
        invocationsForMethods.put(activeMethod, new ArrayList<MethodInvocation>());
    }
    invocationsForMethods.get(activeMethod).add(node);
    return super.visit(node);
}*/