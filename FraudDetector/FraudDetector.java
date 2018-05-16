import java.util.*;
import java.io.*;
import java.lang.*;

public class FraudDetector{
    
    public static void main (String args[]){
	//LinkedList<String[]> transaction = new LinkedList<String[]>();
	HashMap<String, String[]> transactionMap = new HashMap<String,String[]>();
	//ArrayList<String> nameList = new ArrayList<String>();
	HashMap<String, Integer> airLines = new HashMap<String,Integer>();
	ArrayList<String[]> no_return = new ArrayList<String[]>();
	double neg_transaction = 0;
	try {
	    BufferedReader filename = new BufferedReader(new InputStreamReader(System.in));
	    filename.readLine();
	    while (filename.ready()){
		String fileLine = filename.readLine();
		String[] Line = fileLine.split(",(?=([^\"]*\"[^\"]*\")*[^\"]*$)");
		// Individual transactions exceeding $50,000
		if (Double.parseDouble(Line[6])>50000){
		    System.out.println("Exceeding $50,000: "+fileLine);		    
		}
		// Transactions whose value is unusually "round" (i.e. evenly divisible by $100)
		if (Double.parseDouble(Line[6])%100==0){
		    System.out.println("value is round: "+fileLine);
		}
		// Pawn shops, casinos and resorts
		if (Line[10].toUpperCase().contains("PAWN SHOPS")==true||Line[10].toUpperCase().contains("CASINOS")==true||Line[10].toUpperCase().contains("RESORTS")==true){
		    System.out.println("Pawn shops, casinos and resorts: "+fileLine);
		}
		
		// Store the name and number of the airLines
		if (Line[10].contains("AIRLINES")){
		    if (!airLines.containsKey(Line[10])){
			airLines.put(Line[10],1);
		    }
		    else{
			airLines.replace(Line[10],airLines.get(Line[10]),airLines.get(Line[10])+1);
		    }
		}
		// Multiple large ($>20,000) transactions by a single user in a single day
		if (transactionMap.containsKey(Line[4]) && Double.parseDouble((transactionMap.get(Line[4]))[8])>20000){
		    System.out.println("Multiple large transactions by a single user in a single day: ");
		    System.out.println(fileLine);
		}
		// Store the transaction under the cardholder
		transactionMap.put(Line[4]+" "+Line[3], Line);

		// If encouter a negative transaction, add it to neg_transaction, check if other positive transaction from the same person can offset it.
		if (Double.parseDouble(Line[6])<0){
		    no_return.add(Line);
			neg_transaction+=Double.parseDouble(Line[6]);
		}
		else{
		    if (!no_return.isEmpty()){
			for (int i = 0; i<no_return.size();i++){
			    if ((no_return.get(i))[3]==Line[3]&&(no_return.get(i))[4] == Line[4]){
				neg_transaction +=Double.parseDouble(Line[6]);
				if (neg_transaction >0){
				    no_return.clear();
				}
			    }
			}
		    }
		    
		}
	    }
	    System.out.println("_________________________________________________________________________________________________________________________________________________________");
	    // Infrequently used airlines (fewer than 10 occurrences)
	    for (Map.Entry<String,Integer> pair : airLines.entrySet()){
		//iterate over values
		if (pair.getValue()<10){
		    for (Map.Entry<String,String[]> pair2 : transactionMap.entrySet()){
			//iterate over the pairs
			if ((pair2.getValue())[10] == pair2.getKey()){
			    System.out.println("Infrequently used airline: ");
			    System.out.println(pair.getValue());
			}
		    }
		}
	    }
	    // Print out the transactions with negative values that are not returned
	    if(neg_transaction <0){
		for(String[] tran:no_return){
		    System.out.println(tran);
		}
	    }
	    
	    
	} catch (IOException e) {
	    e.printStackTrace();
	}
	
    }

   
}
