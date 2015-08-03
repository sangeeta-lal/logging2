import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;




/*@Author: Sangeeta
 * @Uses: This progtam is crated to provide utility methods to all classes in java
 * */


public class util_met 
{

	public void print_hello()
	{
		System.out.println("Hello tonew way of coding ");
	}
	
	public int get_try_loc_count(String con)
	{
		//@Comment: This is a specialized method for counting for try block as it counts loc =  loc-2 , because of bracket brolem
		int loc = 0;
		
		String loc_arr[] = con.split("\n");
		for(int i = 0; i< loc_arr.length; i++)
		{
			if(loc_arr[i]!="")
			{
				loc++;
			}
		}
		
		if(loc!=0)
		  {loc = loc-2;}
		
		return loc;
		
	}
	
	public log_level_interface find_and_set_logging_level(String string_content, log_level_interface l) 
	{
		
		  // log_count=0;
			Pattern pat = Pattern.compile("([a-zA-Z0-9_\\(\\)]+\\.info\\()");
			Matcher matcher = pat.matcher(string_content);
			while(matcher.find())
			{
			  System.out.println("Start Index ="+matcher.start());	
			  System.out.print("Start index: " + matcher.start());
		      System.out.print(" End index: " + matcher.end() + " ");
		      System.out.println("pattern matched = "+matcher.group(1));
		      l.log_levels_combined=l.log_levels_combined+"  "+(matcher.group(1).split("\\.")[1]).split("\\(")[0];
		      
			}	
			
			pat = Pattern.compile("([a-zA-Z0-9_\\(\\)]+\\.trace\\()");
			matcher = pat.matcher(string_content);
			while(matcher.find())
			{
			  System.out.println("Start Index ="+matcher.start());	
			  System.out.print("Start index: " + matcher.start());
		      System.out.print(" End index: " + matcher.end() + " ");
		      System.out.println("pattern matched = "+matcher.group(1));
		      l.log_levels_combined=l.log_levels_combined+" "+(matcher.group(1).split("\\.")[1]).split("\\(")[0];
			} 
			
			pat = Pattern.compile("([a-zA-Z0-9_\\(\\)]+\\.debug\\()");
			matcher = pat.matcher(string_content);
			while(matcher.find())
			{
			  System.out.println("Start Index ="+matcher.start());	
			  System.out.print("Start index: " + matcher.start());
		      System.out.print(" End index: " + matcher.end() + " ");
		      System.out.println("pattern matched = "+matcher.group(1));
		      l.log_levels_combined=l.log_levels_combined+" "+(matcher.group(1).split("\\.")[1]).split("\\(")[0];;
			} 
			
			pat = Pattern.compile("([a-zA-Z0-9_\\(\\)]+\\.warn\\()");
			matcher = pat.matcher(string_content);
			while(matcher.find())
			{
			  System.out.println("Start Index ="+matcher.start());	
			  System.out.print("Start index: " + matcher.start());
		      System.out.print(" End index: " + matcher.end() + " ");
		      System.out.println("pattern matched = "+matcher.group(1));
		      l.log_levels_combined=l.log_levels_combined+" "+(matcher.group(1).split("\\.")[1]).split("\\(")[0];;
			} 
			
			pat = Pattern.compile("([a-zA-Z0-9_\\(\\)]+\\.error\\()");
			matcher = pat.matcher(string_content);
			while(matcher.find())
			{
			  System.out.println("Start Index ="+matcher.start());	
			  System.out.print("Start index: " + matcher.start());
		      System.out.print(" End index: " + matcher.end() + " ");
		      System.out.println("pattern matched = "+matcher.group(1));
		      l.log_levels_combined=l.log_levels_combined+" "+(matcher.group(1).split("\\.")[1]).split("\\(")[0];;
			} 
			
			pat = Pattern.compile("([a-zA-Z0-9_\\(\\)]+\\.fatal\\()");
			matcher = pat.matcher(string_content);
			while(matcher.find())
			{
			  System.out.println("Start Index ="+matcher.start());	
			  System.out.print("Start index: " + matcher.start());
		      System.out.print(" End index: " + matcher.end() + " ");
		      System.out.println("pattern matched = "+matcher.group(1));
		      l.log_levels_combined=l.log_levels_combined+" "+(matcher.group(1).split("\\.")[1]).split("\\(")[0];;
			} 
			
			//Pattern:  project.log(""wrong object reference "" + refId + "" - ""+ pref.getClass());
			/*pat = Pattern.compile("([a-zA-Z0-9_]+\\.log\\()");
			matcher = pat.matcher(string_content);
			while(matcher.find())
			{
			  System.out.println("Pat 1:");	
			  System.out.print("Start index: " + matcher.start());
		      System.out.print(" End index: " + matcher.end() + " ");
		      System.out.println("pattern matched = "+matcher.group(1));
		      
		      l.log_levels_combined=l.log_levels_combined+" "+(matcher.group(1).split("\\.")[1]).split("\\(")[0];;
			} */
			
			//***Not Correct****Pattern: Logger.getLogger(getLoggerName(getHost(),url)).log(Level.WARNING,""Unable to determine web application context.xml "" + docBase,e);
			
			/*pat = Pattern.compile("([a-zA-Z0-9_]+\\(.*\\)\\.log\\()");
			matcher = pat.matcher(string_content);
			while(matcher.find())
			{
			  System.out.println("Pat 2 :");	
			  System.out.print("Start index: " + matcher.start());
		      System.out.print(" End index: " + matcher.end() + " ");
		      System.out.println("pattern matched = "+matcher.group(1));
		      
		      l.log_levels_combined=l.log_levels_combined+" "+(matcher.group(1).split("\\.")[1]).split("\\(")[0];;
			} */
			
			//pattern: log(""Error closing redirector: "" + ioe.getMessage(),Project.MSG_ERR)
		    
			pat = Pattern.compile("[\\s\n]*log\\(.*\\)");
			matcher = pat.matcher(string_content);
			while(matcher.find())
			{
			  System.out.println("Pat 3:");	
			  System.out.print("Start index: " + matcher.start());
		      System.out.print(" End index: " + matcher.end() + " ");
		      System.out.println("pattern matched = "+matcher.group(0));
		      
		      String level = get_non_standard_log_levels(string_content, matcher.start());		      
		      l.log_levels_combined=l.log_levels_combined+" "+ level;
			}
			
			
			pat = Pattern.compile("log.append\\(.*\\)");
			matcher = pat.matcher(string_content);
			while(matcher.find())
			{
			  System.out.println("Pat 4:");	
			  System.out.print("Start index: " + matcher.start());
		      System.out.print(" End index: " + matcher.end() + " ");
		      System.out.println("pattern matched = "+matcher.group(0));
		      
		      String level = get_non_standard_log_levels(string_content, matcher.end());		      
		      l.log_levels_combined=l.log_levels_combined+" "+ level;
			}
			
			
			pat = Pattern.compile("getLogWriter().println\\(.*\\)");
			matcher = pat.matcher(string_content);
			while(matcher.find())
			{
			  System.out.println("Pat 5:");	
			  System.out.print("Start index: " + matcher.start());
		      System.out.print(" End index: " + matcher.end() + " ");
		      System.out.println("pattern matched = "+matcher.group(0));
		      
		      String level = get_non_standard_log_levels(string_content, matcher.end());		      
		      l.log_levels_combined=l.log_levels_combined+" "+ level;	
		      System.out.println("HelloLevel");
				BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
				try 
				 {
				 // br.readLine();
				 }catch(Exception e)
				{}
		     }
			
			pat = Pattern.compile("logWriter.println\\(.*\\)");
			matcher = pat.matcher(string_content);
			while(matcher.find())
			{
			  System.out.println("Pat 5:");	
			  System.out.print("Start index: " + matcher.start());
		      System.out.print(" End index: " + matcher.end() + " ");
		      System.out.println("pattern matched = "+matcher.group(0));
		      
		      String level = get_non_standard_log_levels(string_content, matcher.end());		      
		      l.log_levels_combined=l.log_levels_combined+" "+ level;
			}
			
			
			
			if(l.log_levels_combined!="")
			{
			l.log_count= l.log_levels_combined.trim().split(" ").length;
			l.logged = 1;
			}
			//System.out.println("Final Log levels are:"+log_levels_combined);
			
			return l;
	}

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
			level = "log";
			System.out.println("HelloLevel");
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			try 
			 {
				System.out.println("string content="+ string_content+" substring="+substring);
			   // br.readLine();
			 }catch(Exception e)
			{}
			return level;
		}
		else
		{
			level= "hello";
			System.out.println("Helljkjklj");
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			try 
			 {
			  br.readLine();
			 }catch(Exception e)
			{}
			return level;
		}
		
	}

	public int contains_previous_catches(int count)
	{
		if(count==0)
			return 0;
		
		else
		return 1;
	}

	public int are_previous_catches_logged(String previous_catch_as_string, int count) 
	{
		if(count==0)// first catch block
			return 0;
		
		log_level_interface temp  = new log_level_interface();
		find_and_set_logging_level(previous_catch_as_string, temp);
		
		int logged =  temp.logged;
		return logged;
	}
	
	public int get_log_count(String content) 
	{
	   int log_count = 0 ;
	   log_level_interface temp = new log_level_interface();
	   find_and_set_logging_level(content, temp);
	   log_count = temp.log_count;
		return log_count ;
	}


	public int check_return(String content)
	{

	  int contains_return_stmt=0;
	  
	   contains_return_stmt=	content.contains("return ")?1:0;
		
		return contains_return_stmt;
	}

	public int check_ignore(String catch_exp_with_obj)
	{
	
		catch_exp_with_obj= catch_exp_with_obj.toString().toLowerCase();
	
		int obj_contains_ignore=0;
		
		obj_contains_ignore=catch_exp_with_obj.contains(" ignore")?1:0;
		return obj_contains_ignore;
	}

	public int check_interrupted_exception(String catch_exp)
	{
		if(catch_exp.equalsIgnoreCase("InterruptedException"))
		return 1;
		
		else 
			return 0;
	}

	public int check_thread_sleep(String try_con) 
	{
		int thread_sleep_try=0;
		thread_sleep_try= try_con.toLowerCase().contains("Thread.sleep".toLowerCase())?1:0;
		return thread_sleep_try;
	}

	public int check_throwable_exception(String catch_exp) 
	{
		if(catch_exp.equalsIgnoreCase("Throwable"))
			return 1;
			
			else 
			 return 0;
	}

	public int check_thorw_throws(String content) 
	{
		int contains_throw_throws = 0;
		content =  content.toString().toLowerCase();
		content =  content.replace("\n"," ");
		
	
		//check throw
		Pattern throw_pat = Pattern.compile(".*throw\\s+.*");
		Matcher m = throw_pat.matcher(content);
		if (m.find())
		{
		  contains_throw_throws = 1;
		}

		
		//check throws 
		if(contains_throw_throws==0)
		{

			throw_pat = Pattern.compile(".*throws\\s+.*");
			m = throw_pat.matcher(content);
			if (m.find())
			{
			  contains_throw_throws = 1;
			}
			
		}
			
		return contains_throw_throws;
	}

	public int check_if(String content)
	{
		int if_present=0;
		
		content =  content.toString().toLowerCase();
		content =  content.replace("\n"," ");
		
		//check if
		Pattern throw_pat = Pattern.compile(".*if\\s*\\(.*");
		Matcher m = throw_pat.matcher(content);
		if(m.find())
		{
			
			if_present =1;
		}
	
	 return if_present;
	}

	public int get_if_count(String content) 
	{
		int if_count  = 0;
		
		content =  content.toString().toLowerCase();
		
		//content =  content.replace("\n"," "); //@Eding \n causes error and code is not able to find all the ocuurances
		
		//check if
		Pattern if_pat = Pattern.compile(".*if\\s*\\(.*");
		Matcher m = if_pat.matcher(content);
		while(m.find())
		{
			
			//System.out.println(" Grop = "+m.group(0));
			if_count++;
		}
		
		return if_count;
	}

	public int check_assert(String content)
	{
		int contains_assert = 0;
		
		content = content.toLowerCase();
		contains_assert=	content.contains(".assert".toLowerCase())?1:0;
		/*if(contains_assert==0)
		{
			contains_assert=	content.contains(".assertFalse".toLowerCase())?1:0;
		}*/
		
		return contains_assert ;
	}

	public int get_catch_depth(int count)
	{
	
		return  count  +1;
	}

	public String find_final_catch_exp(String catch_exp) 
	{
		 String exp[] = catch_exp.split("\\.");
		 int len = exp.length;		 
		 catch_exp  = exp[len-1];
		 
		 return catch_exp;
		
	}

	public int check_method_parameter(List method_parameter)
	{
		
		
	  int is_param=  method_parameter.size()>0? 1 :0;
				
	  return is_param;
	}

	public int get_param_count(List method_parameter) 
	{
		
	
		int param_count  =0;
		
		param_count =  method_parameter.size();
		
		return param_count; 
	}

	public String clean_string(String input_string) 
	{
		input_string = input_string.replace("\"", " ");
		input_string = input_string.replace("\'", " ");
		return input_string;
	}

	
	

}
