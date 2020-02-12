package cs5387;

import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.Assert.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;

import org.easymock.EasyMockSupport;
import org.junit.jupiter.api.Test;
class TableSorterTest extends EasyMockSupport{
	

	private Table tableMock ;
	
	public void setUp() {
		//tableMock = createMock(Table.class) ;
	}

	@Test
	void testIsSortedNotSorted() throws Exception {
		int[] userInput = new int[] {56, 66, 87, 12 };
		tableMock = new Table(4, userInput) ;
		replayAll();
		assertFalse(TableSorter.isSorted(tableMock)) ;
		verifyAll() ;
	}

	@Test
	void testIsSorted() throws Exception {
		int[] userInput = new int[] { 2, 3, 4, 5 };
		tableMock = new Table(4, userInput) ;
		replayAll();
		assertTrue(TableSorter.isSorted(tableMock)) ;
		verifyAll() ;
	}

	@Test
	void testSortable() throws Exception {
		int[] userInput = new int[] {56, 66, 87, 12 };
		tableMock = new Table(4, userInput) ;
		replayAll();
		TableSorter.sortable(tableMock);
		verifyAll() ;
	}

	@Test
	void testNotSortedVector() {
		int[] userInput = new int[] {56, 66, 87, 12 };
		replayAll();
		assertTrue(TableSorter.notSortedVector(userInput)) ;
		verifyAll() ;
	}
	
	@Test
	void testNotSortedVectorReturnFalse() {
		int[] userInput = new int[] { 2, 3, 4, 5 };
		replayAll();
		assertFalse(TableSorter.notSortedVector(userInput)) ;
		verifyAll() ;
	}

	@Test
	void testSortingVector() {
		int[] userInput = new int[] { 56, 66, 87, 12 };
		replayAll();
		int[] result = TableSorter.sortingVector(userInput) ;
		verifyAll() ;
		assertEquals(result, userInput) ;
	}

}
