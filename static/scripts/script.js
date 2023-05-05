search = document.getElementById("Search");
//dashboard = document.getElementById("dashboard");
back_btn = document.getElementById("back_btn");
vid = document.getElementById("vid");
//Enables enter to be used as search execute
document.getElementById("search_txt")
  .addEventListener("keyup", function(event) {
    event.preventDefault();
    if (event.keyCode === 13) {
      document.getElementById("search_bttn").click();
    }
  });



function search_invis() {

  search.style.visibility = "hidden";

  setTimeout(10)
     back_btn.style.visibility = "visible";




  search.value = "";

}


function dash_invis() {

  search.style.visibility = "visible";
  dashboard.style.visibility = "hidden";
  back_btn.style.visibility = "hidden";

}

