import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.eclipse.jdt.core.dom.CatchClause;



public class test
{

	
	public static void main(String args[])
	{ 
	
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