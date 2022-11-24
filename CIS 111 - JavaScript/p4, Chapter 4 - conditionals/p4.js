/*
Description: CS 111 Project 4 - Conditionals 
Author: Karma Woeser
*/

function pizzaPSI(diameter, cost) {
    // Calculate the radius
    r = diameter / 2

    // Calculate the area 
    // r^2 doesn't work in JavaScript?

    // I used Math.pow and Math.PI in project 3 already
    area = Math.pow(r, 2) * Math.PI
    
    // Calculate the PSI
    PSI = cost / area

    // Return the PSI
    return PSI.toFixed(2)

};

console.log("18 pizza at $13.99 has a PSI of", pizzaPSI(10, 13.99));


function isNumeric(character) {
    /*
    // Step 1: If statement to figure out if character is equal to any of the numbers
    if (character == 0) {
        // Step 2: Return true if character is a number
        return true
    } else if (character == 1) {
        return true
    } else if (character == 2) {
        return true
    } else if (character == 3) {
        return true
    } else if (character == 4) {
        return true
    } else if (character == 5) {
        return true
    } else if (character == 6) {
        return true
    } else if (character == 7) {
        return true
    } else if (character == 8) {
        return true
    } else if (character == 9) {
        return true

    } else {
        // Step 3: Return false if character is anything but a number
        return false
    }
    */
    
    // Refactored version and is able to search for every number not just 0-9
    if (isNaN(character) == true) {
        return true
    } else {
        return false
    }
    
    
}
  
// Use two console.log statements to test isNumeric
console.log("Is 5 a number", isNumeric(5));
console.log("Is A a number", isNumeric("A"));



function isLeap(year) {
    return new Date(year, 1, 29).getDate() === 29;
}

function getDaysInMonth(year, month) {


    // 1. Set variables 
    let day = 0
    let date = new Date(year, month, day).getDate()


    // 2. Feburary/leap year if statement 
    if (month == 2) { 
      if (isLeap(year) == false) {
        day = 28
        return date
      }
      return date

      
    }
    
    //3. List out rest of months using switch statement
    switch(month) {
        case 1:
          month= 1;
          return date
        case 3:
          month= 3;
          return date
        case 4:
          month= 4;
          return date
        case 5:
          month= 5;
          return date
        case 6:
          month= 6;
          return date
        case 7:
          month= 7;
          return date
        case 8:
          month= 8;
          return date
        case 9:
          month= 9;
          return date
        case 10:
          month= 10;
          return date
        case 11:
          month= 11;
          return date
        case 12:
          month= 12;
          return date

    }
}


console.log("2022, 11:", getDaysInMonth(2022 ,11))
console.log("2023, 8:", getDaysInMonth(2023 ,8))
console.log("2024, 2:", getDaysInMonth(2024 , 2))
