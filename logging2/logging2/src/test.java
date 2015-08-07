import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.eclipse.jdt.core.dom.CatchClause;



public class test
{
	private String get_non_standard_log_levels(String string_content, int start_index)
	{
		String level = "";
		
		int end_index= string_content.indexOf(")", start_index);
		String substring = string_content.substring(start_index, end_index);
		
		System.out.println("Substring oitside="+ substring);
		int index =  substring.indexOf("Level");
		System.out.println("level index=" +index);
		if(index==-1)
		{
			level = "NoLogLevel";
			System.out.println("HelloLevel");
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			try 
			 {
				System.out.println("string content="+ string_content+" substring="+substring);
			    br.readLine();
			 }catch(Exception e)
			{}
			return level;
		}
		else
		{
			//level= "hello";
			System.out.println("I am here");
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			try 
			 {
			   br.readLine();
			 }catch(Exception e)
			{}
			
			System.out.println("Helljkjklj");
			String  substring_part[]  =  substring.split(",");
			System.out.println("xyz"+substring_part[0]+"xyz");
			String temp_level2[] =  substring_part[0].split("\\.");
			level = temp_level2[1];
			if(level.equalsIgnoreCase("WARNING"))
			{
				level = "warn";
			}
			
			System.out.println("level = "+ level);
		//	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			try 
			 {
			   br.readLine();
			 }catch(Exception e)
			{}
			return level;
		}
		
	}

	
	public static void main(String args[])
	{ 
	
		test t = new test();
		String content = "log(Level.WARNING,\"Unable to determine web application context.xml \" + docBase,e)";
		t.get_non_standard_log_levels(content, 0);
		
		String a  =  "public boolean visit(CatchClause mycatch)   {        	String catch_train_con =  ;             retur true;          }";
		a = a +" project.log(\"  \"  wrong object reference \"\" + refId + \"\" -\"\"+ pref.getClass());  3.\n  " ;
		a = a+ "\n log(\"\"Error closing redirector: \"\" + ioe.getMessage(),Project.MSG_ERR)    "+" Logger.getLogger(getLoggerName(getHost(),url)).log(Level.WARNING,\"\"Unable to determine web application context.xml \"\" + docBase,e);";
		
		System.out.println("a="+a);;
		
	   util_met u  =  new util_met();
		
	   log_level_interface l = new log_level_interface();
	   log_level_interface val =  u.find_and_set_logging_level(a, l);
		
		System.out.println("vla "+ val.log_count+  "  "+ val.log_levels_combined+  "   "+ val.logged );
		
		
		a = "Try Content={"+
				 " webResource=resourceRoot.getResource(getMount() + );"+
		"}" +
		" All Catch Blocks="+
		"catch (IllegalArgumentException iae) {"+
		 " Assert.assertFalse(getMount().length() == 0); "+
		  "return;";
		
	
		
		//val = u.check_assert   (a);
		
		String abc = "IOException";
		
		abc= u.find_final_catch_exp(abc);
		
		System.out.println("value= " +abc);
		
		System.out.println("vla "+ val );
	}		

}