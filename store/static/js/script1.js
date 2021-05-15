$(document).ready(function () {
    //change the integers below to match the height of your upper div, which I called
    //banner.  Just add a 1 to the last number.  console.log($(window).scrollTop())
    //to figure out what the scroll position is when exactly you want to fix the nav
    //bar or div or whatever.  I stuck in the console.log for you.  Just remove when
    //you know the position.

    $()


    $(window).scroll(function () {


        if ($(window).scrollTop() > $(".navbar").scrollTop()) {
            $(".navbar").css("position", "fixed");
            $(".navbar").css("top", "0");
            $(".navbar").css("width", "100%");

            /*alert("done");*/


        }

        if ($(window).scrollTop() < 451) {
            $(".navbar").css("position", "");
        }
    });
});

function myFunction() {
    alert();
    // Getting sum of numbers

}

//this piece of java script captures the .menu-btn elements and creates a litsener for event click then it proceeds to add classses to it depending on the state
const menuBtn = document.querySelector('.menu-btn');
const navbarlinks = document.querySelector('.nav-menu a')
let menuOpen = false;
menuBtn.addEventListener('click', () => {
    if(!menuOpen){
         menuBtn.classList.add('open');
         navbarlinks.classList.add('active')
         menuOpen= true;

    }
    else {
        menuBtn.classList.remove('open')
        navbarlinks.classList.remove('active')
        menuOpen= false;
    }
});