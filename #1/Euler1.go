package main

import "fmt"

// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9.
// The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

// I'm thinking of using the summation mathematical notation by finding the bounds for these first
// summation notation sum 3i = 3 * n * (n+1)/2
func sum_multiples_of_3_or_5(upperbound int) int {
	var sum int
	// 3*333=999 (largest value before 1000)
	// summation notation sum i = n * (n+1)/2
	sum3 := 3 * ((upperbound - 1) / 3) * ((upperbound-1)/3 + 1) / 2
	sum5 := 5 * ((upperbound - 1) / 5) * ((upperbound-1)/5 + 1) / 2
	sum15 := 15 * ((upperbound - 1) / 15) * ((upperbound-1)/15 + 1) / 2

	sum = sum3 + sum5 - sum15

	return sum
}

func main() {

	sum := sum_multiples_of_3_or_5(1000)

	fmt.Print("Sum of all multiples of 3 and 5 below 1000 is: ", sum, "\n")

	sum = sum_general_multiples(1000, 3, 5)

	fmt.Print("Using the other formula the sum is: ", sum, "\n")

}

func sum_general_multiples(upperbound int, multiple1 int, multiple2 int) int {
	var sum int
	// 3*333=999 (largest value before 1000)
	// summation notation sum i = n * (n+1)/2
	sum1 := multiple1 * ((upperbound - 1) / multiple1) * ((upperbound-1)/multiple1 + 1) / 2
	sum2 := multiple2 * ((upperbound - 1) / multiple2) * ((upperbound-1)/multiple2 + 1) / 2
	sum3 := multiple1 * multiple2 * ((upperbound - 1) / (multiple1 * multiple2)) * ((upperbound-1)/(multiple1*multiple2) + 1) / 2

	sum = sum1 + sum2 - sum3

	return sum
}
