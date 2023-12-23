public class Euler1 {
    private int upperbound;
    private int multiples1;
    private int multiples2;

    public Euler1(int upperbound, int mu, int mu2) {
        this.upperbound = upperbound;
        this.multiples1 = mu;
        this.multiples2 = mu2;
    }

    private int sum_divisible_by(int number) {
        int n = (this.upperbound - 1) / number;
        return n * (n + 1) / 2;
    }

    public int sumTotal() {
        int sum1 = this.multiples1 * sum_divisible_by(this.multiples1);
        int sum2 = this.multiples2 * sum_divisible_by(this.multiples2);
        int sum3 = this.multiples1 * this.multiples2 * sum_divisible_by(this.multiples1 * this.multiples2);

        return sum1 + sum2 - sum3;
    }

    public static void main(String[] args) {
        Euler1 calc = new Euler1(1000, 3, 5);
        int sum = calc.sumTotal();
        System.out.println("Using Java's OOP the sum of multiples of 3 and 5 is = " + sum);
    }
}