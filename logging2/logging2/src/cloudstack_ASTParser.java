
import org.eclipse.core.internal.utils.FileUtil;
import org.eclipse.jdt.core.dom.AST;
import org.eclipse.jdt.core.dom.ASTNode;
import org.eclipse.jdt.core.dom.ASTParser;
import org.eclipse.jdt.core.dom.CompilationUnit;
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

/* This file is used to fill features in the given table.
 * 
 * @pre-requirement:
 * 1. Create this file using create_file_listing.py
	
 * */
//Link for code : http://opensourcejavaphp.net/java/htmlunit/com/gargoylesoftware/htmlunit/CodeChecker.java.html
//link for code: https://github.com/juliangamble/ASTCodeGenTest/blob/master/src/ast/testgen/CodeGenDemo.java
//Link for useful code: http://www.programcreek.com/2011/11/use-jdt-astparser-to-parse-java-file/
//Link for useful source code: http://stackoverflow.com/questions/18939857/how-to-get-a-class-name-of-a-method-by-using-eclipse-jdt-astparser

public class cloudstack_ASTParser {

	String rawContent = "";
	String method_name = "";
	String method_content="";
	String class_name="";
	String package_name = "";
	String temp_file_path = "";
	//Set using the function of the file
	int id = 0;
	
	ArrayList<String> all_file_list= new ArrayList<String>();
	String log_levels_combined = "";
	/*	
	String url = "jdbc:mysql://localhost:3306/";
	String driver = "com.mysql.jdbc.Driver";
	String db_name ="logging_level2";
	String table ="cloudstack_level_feature";
	String userName = "root"; 
	String password = "123";
    //String listing_file_path = "D:\\Research\\Logging\\result\\cloudstack-4.3.0_java_files.txt";  
    String listing_file_path = "D:\\Research\\Logging\\result\\temp_files.txt";
	*/
    
    String url = "jdbc:mysql://localhost:3307/";
	String driver = "com.mysql.jdbc.Driver";
	String db_name ="logging_level2";
	String table ="cloudstack_level_feature";
	String userName = "sangeetal"; 
	String password = "sangeetal";
    String listing_file_path = "E:\\Sangeeta\\Research\\Logging\\result\\cloudstack-4.3.0_java_files.txt";  
   
    
    //@Note: create this file using create_file_listing.py
	
	String folder_path = "";
	
	 
    Connection conn=null;	
	java.sql.Statement stmt = null;
		
	public static void main(String[] args) 
	{				    
		cloudstack_ASTParser demo = new cloudstack_ASTParser();
		demo.conn = demo.initdb(demo.db_name);
		try {
			BufferedReader br =  new BufferedReader(new FileReader(demo.listing_file_path));
			String file_name =  br.readLine();
			while(br!=null)
			{
				System.out.println("Parsing File="+file_name);
				int len = (file_name.split("\\\\")).length;
				demo.package_name = file_name.split("\\\\")[len-2];
				//demo.id=0;
				demo.temp_file_path= file_name;//
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
		
		//String rawContent = demo.readFile();		
		try{
			
			//rawContent = ASTParserDemo1.readFileToString("D:\\Research\\Logging\\dataset\\temp\\BeanNameELResolver.java");
			rawContent = cloudstack_ASTParser.readFileToString(file_name);
			
		}catch(Exception e){
			System.out.println();
		}
		//String rawContent = "public class HelloWorld { public String s = \"hello\"; public static void main(String[] args) { HelloWorld hw = new HelloWorld(); String s1 = hw.s; } }";
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
	    	        	      	method_name = method.getName().getFullyQualifiedName();
	    	        	      	System.out.println("method=" +  method.getName().getFullyQualifiedName());
	    	        	      	// System.out.println("method.return =" + method.getReturnType2().toString());
	    	            
	    	        	      	//List<SingleVariableDeclaration> params = method.parameters();
	    	        	      	//for(SingleVariableDeclaration param: params)
	    	        	      	//{
	    	        	      		//System.out.println("param" + param.getName().getFullyQualifiedName());
	    	        	      	//}
                                try
                                {
                                	Block methodBlock = method.getBody();
                                	String myblock = methodBlock.toString();
	    	            
                                	/*List<Statement> methodStatements = methodBlock.statements();
                                	for (Statement methodStatement: methodStatements ) 
	    	        	      			{
	    	        	      				String statementString = methodStatement.toString();
	    	        	      				System.out.println("statementString:" + statementString);
	    	        	      			}  */      
	    	            
	    	        	      	method_content = methodBlock.toString();
	    	        	      	method_content =  method_content.replaceAll("\"", " ");
	    	        	      	method_content =  method_content.replaceAll("\'", " ");
	    	        	      	method_content =  method_content.replaceAll("\n", " ");
	    	        	      	method_content = method_content.trim();
	    	        	      	//System.out.println("Content="+method_content);
	    	                   	find_and_set_logging_level(method_content);
                                }catch(NullPointerException e)
                                { e.printStackTrace();
                                  method_content = "";
                                  log_levels_combined = "";
                                }
	    	        	      	insert();
	    	        	      	reset_parameters();
	    	        	      	//System.out.println("Hello");
	    	        	      	return false;
	    	               }
			
	               }
	    	);
		}catch(NullPointerException e) { e.printStackTrace();}
	}
	
public void reset_parameters()
{
	log_levels_combined="";
	//method_name = "";
	//method_content="";
	//class_name= "";
}
	
private void find_and_set_logging_level(String catch_content) 
{
		Pattern pat = Pattern.compile("([a-zA-Z0-9_\\(\\)]+\\.info\\()");
		Matcher matcher = pat.matcher(catch_content);
		while(matcher.find())
		{
		  //System.out.println("Start Index ="+matcher.start());	
		  //System.out.print("Start index: " + matcher.start());
	      //System.out.print(" End index: " + matcher.end() + " ");
	      //System.out.println("pattern matched = "+matcher.group(1));
	      log_levels_combined=log_levels_combined+"  "+(matcher.group(1).split("\\.")[1]).split("\\(")[0];
	      
		}
		
		
		pat = Pattern.compile("([a-zA-Z0-9_\\(\\)]+\\.trace\\()");
		matcher = pat.matcher(catch_content);
		while(matcher.find())
		{
		  //System.out.println("Start Index ="+matcher.start());	
		  //System.out.print("Start index: " + matcher.start());
	      //System.out.print(" End index: " + matcher.end() + " ");
	      //System.out.println("pattern matched = "+matcher.group(1));
	      log_levels_combined=log_levels_combined+" "+(matcher.group(1).split("\\.")[1]).split("\\(")[0];
		} 
		
		pat = Pattern.compile("([a-zA-Z0-9_\\(\\)]+\\.debug\\()");
		matcher = pat.matcher(catch_content);
		while(matcher.find())
		{
		  //System.out.println("Start Index ="+matcher.start());	
		  //System.out.print("Start index: " + matcher.start());
	      //System.out.print(" End index: " + matcher.end() + " ");
	      //System.out.println("pattern matched = "+matcher.group(1));
	      log_levels_combined=log_levels_combined+" "+(matcher.group(1).split("\\.")[1]).split("\\(")[0];;
		} 
		
		pat = Pattern.compile("([a-zA-Z0-9_\\(\\)]+\\.warn\\()");
		matcher = pat.matcher(catch_content);
		while(matcher.find())
		{
		  //System.out.println("Start Index ="+matcher.start());	
		  //System.out.print("Start index: " + matcher.start());
	      //System.out.print(" End index: " + matcher.end() + " ");
	      //System.out.println("pattern matched = "+matcher.group(1));
	      log_levels_combined=log_levels_combined+" "+(matcher.group(1).split("\\.")[1]).split("\\(")[0];;
		} 
		
		pat = Pattern.compile("([a-zA-Z0-9_\\(\\)]+\\.error\\()");
		matcher = pat.matcher(catch_content);
		while(matcher.find())
		{
		  //System.out.println("Start Index ="+matcher.start());	
		  //System.out.print("Start index: " + matcher.start());
	      //System.out.print(" End index: " + matcher.end() + " ");
	      //System.out.println("pattern matched = "+matcher.group(1));
	      log_levels_combined=log_levels_combined+" "+(matcher.group(1).split("\\.")[1]).split("\\(")[0];;
		} 
		
		pat = Pattern.compile("([a-zA-Z0-9_\\(\\)]+\\.fatal\\()");
		matcher = pat.matcher(catch_content);
		while(matcher.find())
		{
		  //System.out.println("Start Index ="+matcher.start());	
		  //System.out.print("Start index: " + matcher.start());
	      //System.out.print(" End index: " + matcher.end() + " ");
	      //System.out.println("pattern matched = "+matcher.group(1));
	      log_levels_combined=log_levels_combined+" "+(matcher.group(1).split("\\.")[1]).split("\\(")[0];;
		} 
		
} 

public void insert()
{
	id++;	
	//method_content="hi";
	String insert_str= "insert into "+table+" values(\""+package_name+"\",\""+class_name+"\",\""+method_name+"\","+  id+",\""+method_content+"\",\""+
	log_levels_combined+"\",\""+temp_file_path+"\","+"\"r\" ,\"u\")";
	System.out.println("Insert str"+1);
	try 
	{
		if(conn==null)
		{
			//System.out.println("I am null");
		}
			stmt =  conn.createStatement();
			stmt.executeUpdate(insert_str);
	} catch (SQLException e) {
			// TODO Auto-generated catch block
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
		    	  System.out.println("Hi I am ull :( :(");
		      }
		      
		 } catch (Exception e) 
		 {
		      e.printStackTrace();
		 }
		return conn;
}

}//main

