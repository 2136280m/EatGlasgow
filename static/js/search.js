function showHint(str) {
    var xmlhttp;
    if (str.length == 0) {//if contant of search is null
        document.getElementById("txtHint").innerHTML = "";//the tab is null(no result)
        return;
    }
    if (window.XMLHttpRequest) {// code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp = new XMLHttpRequest();//make Request
    }
    else {// code for IE6, IE5
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {//successly received
            document.getElementById("txtHint").innerHTML = xmlhttp.responseText;
        }//display the result
        else {
            document.getElementById("txtHint").innerHTML = "Fail";//opps, fail
        }
    }
    xmlhttp.open("GET", "search/" + str, true);//set the keyword to send
    xmlhttp.send();//send!
}