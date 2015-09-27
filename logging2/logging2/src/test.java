import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;


public class test

{
	
	private static method_name_and_count mnc  =  new method_name_and_count();

	public static void main(String args[])
	{
		
		 
		 util_met  utm = new util_met();
         String filename = "F:\\Research\\test.java";
         BufferedReader br  =  null;
        
         /*try {
			 br =  new BufferedReader(new FileReader(filename));
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
         
         String a = "";
         String b = "";
         try {
			    while((a=br.readLine()) != null)
			         {
				       b=b+"  \n"+a;
				 
			          }
		} 
          catch (IOException e) 
         {
			 e.printStackTrace();
		  }
         
       //  System.out.println("file content="+ b);
         mnc= utm.get_method_call_name(b, mnc);
         System.out.println(" method_name"+ mnc.method_names);
         */
         
		 TOMCAT_Training2_CATCH obj =  new TOMCAT_Training2_CATCH();
         obj.ast_prser(filename);
         
	}

}
        		    

        		     

        		   

        		     
        		     