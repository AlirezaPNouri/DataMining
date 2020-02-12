package cs5387;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Arrays;

public class Table {
	// table is an array of 0..(range-1) X 0..(range-1)
	private int[][] table; 
	private int range;
	
	public Table (int N, int[] values ) throws Exception {
		// N has to be a square
		int k = (int) Math.sqrt((double)N);
		if (k*k != N) {
			System.out.println("ERROR!: Input must be square.");
			throw new Exception();
		}
		
		// create table
		range = k;
		table = new int[range][range];
		
		// put the data into the table
		for (int r=0; r<range; r++) {
			for (int c=0; c<range; c++) {
				setTableValue (r, c, values[r*range+c]);
			}			
		}
	}
	public int getSize () {
		return range;
	}
	
	public int getTableValue (int r, int c) {
		return table[r][c];
	}
	
	public void setTableValue(int r, int c, int v) {
		table [r][c] = v;
	}
	
	public String toString () {
		String retS = "";
		for (int r=0; r<range; r++) {
			for (int c=0; c<range; c++) {
				String s = String.format("%6d", getTableValue (r, c));
				retS = retS + s + "  ";
			}	
			retS += "\n";
		}
		return retS;
	}
	
	
	
	// given a file name, return a Table object.
	// The file contains a list of integers representing an NxN 
	// table of values.
	public static Table GetTable (String filename) 
			throws FileNotFoundException, IOException, Exception {
		File f=new File(filename);
		if (!f.exists()) {
			throw new FileNotFoundException();
		}
		return GetTable (f);
	}
	
	public static Table GetTable (File f) throws IOException, Exception   {
		//File fi = new File (".");
		//for (String filename : fi.list()) System.out.println(filename);

		byte[] bytes = new byte[(int) f.length()];
		FileInputStream fis = new FileInputStream(f);
		fis.read(bytes);
		fis.close();

		String [] valueStr;
		int[] tall;
		int i;
		valueStr = new String(bytes).trim().split("\\s+");
		tall = new int[valueStr.length];
		for (i=0; i < valueStr.length; i++) {
			tall[i] = Integer.parseInt(valueStr[i]);
		}
		System.out.println(Arrays.asList(tall));
		return new Table (valueStr.length, tall);
	}
}
