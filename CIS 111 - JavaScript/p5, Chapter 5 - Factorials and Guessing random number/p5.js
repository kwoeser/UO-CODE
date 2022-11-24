/*
Description: CS 111 Project 5 - Factorials and Guessing random number
Author: Karma Woeser
*/


function factorial (num) {
    let i, j;
    let result;
    let fact;
  
    // Step 1: Set -1 as a default result for values < 0 (invalid input)
    if (num < 0) {
        result = -1
    }

    // Step 2: Test if input is > 0, calculate factorial and set result to calculated value
    // Step 2: Create nested loop that will multiply a number and the number ahead of it until it reaches the desired num
    if (num > 0) {
        for (i = 1; i <= num; i++) {
            for (j = i + 1; j <= num; j++) {
                fact = i *= j;
            }
        result = fact
        } 
    }

    // Step 3: Test if input = 0, set result to 1 
    if (num == 0) {
        result = 1
    }

    return result
}

factorial(10)



/**
 * Returns a random integer between min (inclusive) and max (inclusive).
 * The value is no lower than min (or the next integer greater than min
 * if min isn't an integer) and no greater than max (or the next integer
 * lower than max if max isn't an integer).
 * Using Math.round() will give you a non-uniform distribution!
   https://stackoverflow.com/questions/1527803/generating-random-whole-numbers-in-javascript-in-a-specific-rangeLinks to an external site.
 */
function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function guessNumber (target, min, max) {
    let guesses = 0;

    // Step 1. Do while loop that keeps on going until you the target equals the random integer
    do {
        guesses ++;
    }
    while (target != getRandomInt(min, max));

    // Step 2. Return the amount of guesses it took to find the target
    return guesses;
    // console.log("The computer was able to guess",target, "in",guesses, "guesses")
} 



function getAverageGuesses(num, min, max, loops) {
    let i = 0;
    let guess = 0;
    let avg;

    // Step 1. For loop that will keep adding the amount of guesses it took to find the target with itself
    for (i; i < loops; i++) {
        guess = guessNumber(num, min, max) + guess;
    }

    // Step 2. Divide the total amount of guesses it took by the loops to find avg
    avg = guess / loops

    // Step 3. Console.log the final answer and round the avg to 0 decimals
    console.log("The computer was able to guess", num, "in an average of", Math.round(avg, 0) ,"guesses");
}

getAverageGuesses(31, 1, 100, 1000);