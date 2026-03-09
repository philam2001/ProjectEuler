#include <iostream>
#include <vector>

int multThreeAndFive(int max_num)
{
    int sum = 0;
    int upp_bound = max_num - 1;
    // summation notation sum i = a * n * ( n + 1 ) / 2

    int sum_mult_three = 3 * (upp_bound / 3) * (upp_bound / 3 + 1) / 2;
    int sum_mult_five = 5 * (upp_bound / 5) * (upp_bound / 5 + 1) / 2;
    int sum_mult_fifteen = 15 * (upp_bound / 15) * (upp_bound / 15 + 1) / 2;

    sum = sum_mult_three + sum_mult_five - sum_mult_fifteen;

    return sum;
}

// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9.
// The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

int main()
{
    int max_num = 1000;
    int ans = multThreeAndFive(max_num);

    std::cout << "The sum of multiples of 3 or 5 below " << max_num << " is " << ans << "\n";

    return 0;
}