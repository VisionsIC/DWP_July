/*
WDD Degree Program
Course: DPW
Student: Aaron Wilson
Student ID: 0004619821
Assignment: Project 3 - Reusable Library: validation.js
Date: February 16, 2016
*/

$(document).ready(function(){

    $("form").submit(function(){
        //if either of the name fields isn't full, alert the user and don't let the form submit.
        if($("#first_name").val() == "" || $("#last_name").val() == "") {
            alert("Please enter your First and Last Name");
            return false;
        }
        //ensures that either "male" or "female" is selected by the user.
        if (!$("option[name='select']").is(true)) {
            alert('Please select either Male or Female.');
            return false;
        }
    });
});