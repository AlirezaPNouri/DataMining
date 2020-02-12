/*Author : Alireza P. Nouri
 * Assignment 1
 * Course: software Integration and V&V
 * Professor: Dr. Steve Roach
 * 
 * 
 * 
 * 
	Instrument the code to count down the number of function calls, branches, and comparison 
 * 
 * 
 * 
 * 
 */
package cs5387;

public class TableSorter {

	// read the values (it is just a sample of an array)
	public static int[] userInput = new int[] {56, 66, 87, 12, 78, 90, 19, 89, 34 };

	// a sorted array for checking and testing the program
//	public static int[] userInput1 = new int[] {12, 19 , 34, 56, 66, 78, 87, 89, 90};
	// Method isSorted to check if the table is sorted or not. It accepts a table
	// (Table t) and return a boolean value regarding that the table is sorted or
	// not.
	public static boolean isSorted(Table t) {
		int sizeTable = t.getSize();

		for (int i = 0; i < sizeTable - 1; i++) {

			int[] newVectorHorizontal = new int[sizeTable - i];
			int[] newVectorVertical = new int[sizeTable - i];

			for (int j = i; j < sizeTable; j++) {
				newVectorHorizontal[j - i] = t.getTableValue(i, j - i);
				newVectorVertical[j - i] = t.getTableValue(j - i, i);
			}

			if (notSortedVector(newVectorHorizontal) || notSortedVector(newVectorVertical)
					|| (t.getTableValue(i, i) > t.getTableValue(i + 1, i + 1))) {
				return false;
			}

		}

		return true;

	}

	// Method sortable sorts a given Table t
	public static void sortable(Table t) throws Exception {
		// This method sorts a not sorted table

		// get the size of table
		int tableSize = t.getSize();
		// get all values from the table
		int[] valuesInTable = new int[tableSize * tableSize];
		for (int i = 0; i < tableSize; i++) {
			for (int j = 0; j < tableSize; j++) {
				valuesInTable[i * tableSize + j] = t.getTableValue(i, j);
			}
		}

		valuesInTable = sortingVector(valuesInTable);

		for (int r=0; r<tableSize; r++) {
			for (int c=0; c<tableSize; c++) {
				t.setTableValue (r, c, valuesInTable[r*tableSize+c]);
			}			
		}

	}

	public static boolean notSortedVector(int[] a) {

		for (int i = 0; i < a.length - 1; i++) {
			if (a[i] > a[i + 1]) {
				return true;
			}
		}

		return false;

	}

	public static int[] sortingVector(int[] a) {
		int temp;
		int[] newArray = a;
		for (int i = 1; i < a.length; i++) {
			for (int j = i; j > 0; j--) {
				if (a[j] < a[j - 1]) {
					temp = a[j];
					a[j] = a[j - 1];
					a[j - 1] = temp;
				}
			}
		}
		return newArray;
	}

	public static void main(String[] args) {

		try {
			// try a not sorted array
			Table newTable = new Table(userInput.length, userInput);
			
			//print the table in the console
			System.out.println(newTable.toString());
			//check if the table is not sorted, sort the table then print it.
			if(!isSorted(newTable)) {
				sortable(newTable);
				System.out.println(newTable.toString());
			}

		} catch (Exception e) {
			System.out
					.println("There is an error regarding the input of numbers of the elements. It must be a square.");
			e.printStackTrace();
		}

	}

}
