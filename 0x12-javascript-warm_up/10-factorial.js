#!/usr/bin/node
/**
 * Recursive function to calculate the factorial of a number
 *
 * @param {number} n Number to calculate the factorial for.
 * @return {number} Factorial of the input number.
 */
function factorial (n) {
  return (n === 0 || isNaN(n) ? 1 : n * factorial(n - 1));
}
console.log(factorial(Number(process.argv[2])));
