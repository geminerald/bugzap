$(document).ready(function () {
    console.log("This is the linked page");
    const currentDate = new Date();
    const date = currentDate.getDate();
    const month = currentDate.getMonth();
    const year = currentDate.getFullYear();
    const dateString = `Date: ${date}/${month + 1}/${year}`
    console.log(dateString)
    const timeStamp = document.getElementById("timeStamp");
    let timeStamp.value = dateString;

});

