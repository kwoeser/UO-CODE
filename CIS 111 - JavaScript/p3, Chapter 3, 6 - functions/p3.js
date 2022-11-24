/*
Description: CS 111 Project 3 - Functions
Author: Karma Woeser
*/


function basicFacts() {
    // Prints basic facts into console
    console.log("#1:", "Karma Woeser");
    console.log("#2:", "India");
    console.log("#3:", "Blue");
    console.log("#4:", "Favorite");
    console.log("#5:", "Tibet");

};



function averageFourNums(num1, num2, num3, num4) {
    // Finds sum of all numbers
    sum = num1 + num2 + num3 + num4

    // Finds average of 4 numbers
    avg = sum / 4
    console.log("The average of", num1, num2, num3, num4, "is", avg);
};




function pizzaPSI(diameter, cost) {
    // Calculate the radius
    r = diameter / 2

    // Calculate the area 
    // r^2 doesn't work in JavaScript?
    area = Math.pow(r, 2) * Math.PI
    
    // Calculate the PSI
    PSI = (cost / area)

    // Return the PSI
    return PSI

};

console.log("10 pizza at $5.99 has a PSI of", pizzaPSI(10, 5.99));
console.log("12 pizza at $7.99 has a PSI of", pizzaPSI(12, 7.99));
console.log("14 pizza at $9.99 has a PSI of", pizzaPSI(14, 9.99));
console.log("16 pizza at $11.99 has a PSI of", pizzaPSI(16, 11.99));