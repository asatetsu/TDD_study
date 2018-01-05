package money;

interface Expression {
	Expression times(int multiplier);
	Money reduce(Bank bank,String to);
}
