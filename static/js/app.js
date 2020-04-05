$(document).ready(function () {

    //confirmation that page is being read correctly.
    console.log("This is the linked page");

    //Initialise materialize components

    $('.collapsible').collapsible();
    $('select').material_select();
    $('.sidenav').sidenav();

    //get date for push to DB on new bug page
    const currentDate = new Date();
    const date = currentDate.getDate();
    const month = currentDate.getMonth();
    const year = currentDate.getFullYear();
    const dateString = `${date}/${month + 1}/${year}`
    console.log(dateString);
    document.getElementById("timeStamp").value = dateString;

});