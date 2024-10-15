import sys


def multiples_sum(upperbound, multiples1, multiples2):
    sum1 = multiples1 * ((upperbound-1)//multiples1) * \
        ((upperbound-1)//multiples1+1)//2

    sum2 = multiples2 * ((upperbound-1)//multiples2) * \
        ((upperbound-1)//multiples2+1)//2

    sum3 = multiples1*multiples2 * \
        ((upperbound-1)//(multiples1*multiples2)) * \
        ((upperbound-1)//(multiples1*multiples2)+1)//2

    return sum1 + sum2 - sum3

# OOP
class MultiplesSumCalculator:
    def __init__(self, upperbound, multiples1, multiples2):
        self.upperbound = upperbound
        self.multiples1 = multiples1
        self.multiples2 = multiples2

    def sum_divisible_by(self, number):
        p = (self.upperbound - 1) // number
        return number * p * (p + 1) // 2

    def compute(self):
        sum3 = self.sum_divisible_by(self.multiples1)
        sum5 = self.sum_divisible_by(self.multiples2)
        sum15 = self.sum_divisible_by(self.multiples1*self.multiples2)
        return sum3 + sum5 - sum15


def main():
    sum = multiples_sum(1000, 3, 5)
    print(f"The sum of the multiples of 3 and 5 below 1000 is {sum}")

    calc = MultiplesSumCalculator(1000, 3, 5)
    sum2 = calc.compute()
    print(f"Using OOP, the sum  is {sum2}")


if __name__ == "__main__":
    main()
