/*
Description: CS 111 Project 6 - Count Down function (Set Interval, textcontent)
Author: Karma Woeser
*/



// Grabbing ID's from HTML
const tag = document.getElementById('countDown');
const img = document.getElementById('shipImg');


img.style.display = 'none';

function countDown(seconds) {
    
    // Function runs every 1 second
    setInterval(function handleTimer() {

        // If the seconds == 0 the timer stop and img appears
        if (seconds == 0) {
            tag.textContent = "Blast off!";
            img.style.display = 'block';
            clearInterval();
        // Otherwise it displays the timer and counts down
        } else {
            tag.textContent = seconds;
            seconds --;
        }
    }, 1000);
  
}

countDown(5);