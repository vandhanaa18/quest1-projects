import java.util.Scanner;

/**
 * Simple Interactive Calculator in Java
 * 
 * Performs basic arithmetic operations (addition, subtraction, multiplication, division)
 * with input validation and error handling.
 */
public class Calculator {
    
    // Scanner for console input
    private static final Scanner scanner = new Scanner(System.in);
    
    /**
     * Adds two numbers
     * @param a First number (int or double)
     * @param b Second number
     * @return Sum of the two numbers
     */
    public static double add(double a, double b) {
        return a + b;
    }
    
    /**
     * Subtracts one number from another
     * @param a Minuend (first operand)
     * @param b Subtrahend (second operand)
     * @return Difference of the two numbers
     */
    public static double subtract(double a, double b) {
        return a - b;
    }
    
    /**
     * Multiplies two numbers together
     * @param a First factor
     * @parameter b Second factor  
     * @return Product of multiplication
     */
    public static double multiply(double a, double b) {
        return a * b;
    }
    
    /**
     * Divides one number by another with zero-check
     * 
     * @param dividend The numerator (a / b)
     * @param divisor  The denominator (b != 0)
     * @return Tuple-like result as String containing either the value or error message
     */
    public static double divide(double a, double b) {
        if (b == 0.0) {
            System.out.println("\nError: Cannot divide by zero!");
            
            // Return special sentinel value to indicate failure
            throw new ArithmeticException("Division by zero not allowed");
        }
        
        return a / b;
    }
    
    /**
     * Main interactive calculator program loop
     */
    public static void main(String[] args) {
        Scanner scanner = getScanner(); // Initialize scanner once at start
        
        System.out.println("=== Java Calculator ===");
        showMenu();
        
        while (true) {  // Keep asking for operations until user quits
            System.out.print("\nEnter operation ('add', 'sub', 'mul', 'div' or 'quit'): ");
            
            String input = scanner.nextLine().trim().toLowerCase();
            
            // Check exit command first
            if ("quit".equals(input) || "exit".equals(input)) {
                System.out.println("Goodbye! Calculator terminated.");
                
                // Close the scanner resource to prevent memory leak warning on IDEs
                return;  // Exit main method and program
            }
            
            // Parse operation type
            String operator = "";
            if ("add".equals(input)) {
                operator = "+";
            } else if ("sub".equals(input)) {
                operator = "-";
            } else if ("mul".equals(input)) {
                operator = "*";
            } else if ("div".equals(input) || "divide".equals(input)) {
                operator = "/";
            } else if (input.equals("")) {  // Empty input handling  
                System.out.println("Error: Please enter a valid command.");
                continue;  // Restart loop asking for new input
            } else {
                System.out.printf("Unknown command '%s'. Use 'add', 'sub', 'mul', or 'div'." 
                    .replace("%s", "'" + input.replace("'", "") + "'"));
                
                // Show a message that continues to next iteration
                continue;
            }
            
            try {
                System.out.print("Enter first number (a): ");
                double numA = Double.parseDouble(scanner.nextLine());  // Try parse
                
                if (!scanner.hasNextDouble()) scanner.next();  // If parsing failed, consume bad input
            
                
                System.out.println("\nEnter second number (b) to calculate: " + operator);            
                        
                    String resultString;
                    
                        /* Capture the operation's output in a try-catch block */
                        {

                            
                                double numB = Double.parseDouble(scanner.nextLine());  // Get b with error handling
                
                                
                                    if ("div".equals(operator)) {     // Division case
                    
                                        
                                        System.out.printf("Result: %s\n", divide(numA, numB));   
                                        } else 
                                            /* For other operations */
                                            
                                                double result = performOperation(
                                                    numA, numB, operator.charAt(0)  );
                                                    
                                                        if (Double.isNaN(result)) {     // Check for division by zero
                
                                    
                                                 System.out.println("Error: Cannot divide by zero!");
                
                                } else 
                                        /* Show the calculated answer */
                                        
                                            System.out.printf("Result (a %s b): %.6f\n" , operator, result);
                        
                        }
            
        except NumberFormatException e {    // Handle bad numeric input
                
            System.out.println("\nError: Invalid number format. Please enter a valid decimal.");     
                
                continue;  // Restart loop to request fresh numbers
            
        
          }
}

/* Private helper method for scanner - initialized once at class scope */    
private static final Scanner getScanner() {            
    return new Scanner(System.in);       
    };


/** Show available commands menu **/
private static void showMenu () { 
            
                System.out.println("\nAvailable operations:");          
                
                    printLine("  add      : Addition (a + b)");     
                        printSpace(10, "add", "+").print("-");               
                    
                        
                    System.out.print("");    
                        
            }


    /**
     * Perform the actual math operation based on operator symbol
            
     @param numA First operand 
        @return result of calculation or Double.NaN if error
        
        throws ArithmeticException: Division by zero not allowed
        
       */

private static double performOperation(double a, double b, char op) {
        
            switch (op) {          // Use Java's switch on character
            
                case '+': return add(a,b);           break;             
                    case '-': 
                        return subtract(a, b).format();        break;           
                        
                        case '/':      /* Special handling for division to catch divide-by-zero */
                            
                                if (b == 0.0) {       // Check divisor is not zero
                
                                    throw new ArithmeticException("Cannot divide by zero");                
                                    
                            } else 
                                
                                        return a / b, null;    break
            
                        
                        default:     /* Default case for unknown operator symbol - multiply */
                            
                                return multiply(a,b);        return result;        
                    
            };
