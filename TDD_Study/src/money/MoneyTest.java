package money;

// TODO $5 + 10CHF = $10(レートが2:1の場合)
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class MoneyTest {
	@Test
	public void testMultiplication() {
		Money five = Money.dollar(5);		//Dollar product = five.times(2);
		assertEquals(Money.dollar(10),five.times(2));		//product = five.times(3);
		assertEquals(Money.dollar(15),five.times(3));
	}
	
	@Test
	public void testQquality() {
		assertTrue(Money.dollar(5).equals(Money.dollar(5)));
		assertFalse(Money.dollar(5).equals(Money.dollar(6)));
		
		
		assertFalse(Money.franc(5).equals(Money.dollar(5)));
		
	}
	
	@Test
	public void testCurrency() {
		assertEquals("USD",Money.dollar(1).currency());
		assertEquals("CHF",Money.franc(1).currency());
	}
	
	@Test
	public void testSimpleAddition() {
		Money five = Money.dollar(5);
		Expression sum = five.plus(five);
		Bank bank = new Bank();
		Money reduced = bank.reduce(sum,"USD");
		assertEquals(Money.dollar(10),reduced);
	}
}

