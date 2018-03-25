$(document).ready(function(){
  $("#data-results").hide();
  $("#data-entry").hide();
  $("#submit-btn").hide();

  $("#start-btn").click(function(){
    $("#submit-btn").toggle();
    $("#data-entry").slideToggle(500);
    $(this).hide();
  });

  $("#submit-btn").click(function(){
    $("#input-init").slideToggle(500);
    $("#cover-title").css("padding-top", "2vh");
    $("#data-results").slideToggle(500);
  });

  $("#data-entry input").keyup(function(event) {
    if (event.keyCode === 13) {
          $("#submit-btn").click();
      }
  });

});
/*
sap.ui.getCore().attachInit(function () {
  // create a mobile app and display page1 initially
  var app = new sap.m.App("data-results", {
    initialPage: "page1"
  });
  // create the first page
  var page1 = new sap.m.Page("page1", {
    title : "Hello World",
    showNavButton : false,
    content : new sap.m.Button({
      text : "Go to Page 2",
      press : function () {
        // navigate to page2
        app.to("page2");
      }
    })
  });
  // create the second page with a back button
  var page2 = new sap.m.Page("page2", {
    title : "Hello Page 2",
    showNavButton : true,
    navButtonPress : function () {
      // go back to the previous page
      app.back();
    }
  });
  // add both pages to the app
  app.addPage(page1).addPage(page2);
  // place the app into the HTML document
  app.placeAt("data-results");
});*/
