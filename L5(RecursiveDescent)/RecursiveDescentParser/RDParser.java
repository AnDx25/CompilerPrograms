



import java.io.*;
import java.util.*;
import java.util.Scanner;
import java.lang.String;

public class RDParser {
	
	public static Scanner scanner;  
	
	public static int value;
	public static String app;
	
	
	public static void main(String[] args) {
	
		System.out.println("A -> I = E |E"); // 
		System.out.println("E -> P O P | P"); //
		System.out.println("O -> + | - | * | / | **");   //
		System.out.println("P -> I | L | UI | UL | (E)");//
		System.out.println("U -> + | - | !"); // 
		System.out.println("I -> C | CI"); 
		System.out.println("C -> a | b | ... | y | z ");
		System.out.println("L -> D | DL");
		System.out.println("D -> 0 | 1 | ... | 8 | 9 ");
		
		System.out.println(" ");   
		
		String filer;
		
		RDParser document = new RDParser();
		filer = "input.txt";
		if(document.open(filer)== 0)
		{
			while(scanner.hasNextLine())
			{  
				value = 0;  
				document.reader();
				}
			scanner.close(); 
			}
		}
	public int open(String Filer) 
	{ 
		try
		{
	     scanner = new Scanner(new File(Filer));  
	     return 0;  
	     }  
		catch(FileNotFoundException x)  
		{    System.out.println("No file has been found"); 
		return 1;}
		}
	
		
	public void reader() 
	{
		app = scanner.nextLine(); 
		System.out.println("String read from file :" + app);
		if(A() && value == app.length())
		{   
			System.out.println("The String:   " + app + "  Is In The Language!");
			}
		else{  System.out.println("The String: " + app + "  Is Not In The Language!");
		} 
		}
	
	
	
	private static boolean I() {
		return false;
	}
	private static boolean E() {
		return false;
	}
	private static boolean P() {
		return false;
	}
	private static boolean O(){
		return false;
	}
	private static boolean L() {
		return false;
	}
	private static boolean U() {
		return false;
	}
	private static boolean C() {
		return false;
	}
	private static boolean D() {
		return false;
	}
	
	public static boolean A() 
	{
		if (I())
		{
			if (value < app.length() && app.charAt(value) == '=') 
			{
				value++;
				if (E())
				{
					return true;
					}
				}
			}
		return false;
		
		//**********************************************
		

        public static boolean E()
        {
        	if (P())
         {
             value++;
             if(O())
             {
                 return true;
             }
             
             else if(P())
             {
                 return true;
             }}
            return false;
             {
                 
             }
        }
      //**********************************************
		
        public static boolean O()
        {
            if(app.CharAt(value) == '+' || app.CharAt(value) == '-' || app.CharAt(value) == '*' || app.CharAt(value) == '/' || app.CharAt(value) == '**'){
            
                value++;
                return true;
            }
             return false;
        }
        
        //**********************************************
        
        public static boolean P()
        {
        	if (I())
        	{
        		return true;
        		}
        	else if
        	(L())
        	{
        		return true;
        		}
        	else if(U())
        	{
        		value++;
        		if(I())
        		{
        			return true;
        			}
                else if(L())
                {
                	return true;  
                	}
                else{        
                	return false;     
                	} 
        		}
        	else
        	{
        		if (value < app.length() && app.charAt(value) == '('    ) 
        		{
        			value++;
        			if (E())      
        			{
        				if (value < app.length() && app.charAt(value) == ')'   )
        				{            
        					value++;
        					return true;
        					}
        				}
        			}
        		}
        		return false;
        }
        
        //*************************************
        		
        public static boolean U()
        {
        	if (app.charAt(value) == '+' || app.charAt(value) == '-' || app.charAt(value) == '!') 
        	{
        		value++;
        		return true;
        		}
        	return false;
        	}
      //*************************************
        public static boolean I() 
        {
        	if (C()){return true;}
        	else if(C())
        	{
        		value++;
        		if(I())
        		{
        			return true;
        			}
        		return false;
        		} 
        	return false;
        	}
        
      //*************************************		
        public static boolean C()
        {
        	if (value < app.length() && (app.charAt(value) >= 'a' && app.charAt(value) <= 'z')) 
        	{
        		value++;
        		return true; 
        		} 
        	return false;
        }
      //*************************************		
        
        public static boolean L()
        {
        	if (D()){return true;
        	}
        	else if(D())
        	{
        		value++;
        		if(L())
        		{
        			return true;
        			}
        		return false;
        		}
        	return false;
        	}
      //*************************************
        
        public static boolean D()
        {
        	if (value < app.length() && (app.charAt(value) >= '0' && app.charAt(value) <= '9'))
        	{
        		value++;
        		return true;
        		}
        	return false;
        
        
        
        	}
	}
	

}
