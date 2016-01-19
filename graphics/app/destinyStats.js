$.ajaxSetup({
    cache: false
}); //removes caching

function loadData() { //start function
    $.getJSON("info.json",
        function(data) {
            // Main Character Data
            $(".level.elyril").html(data.Eskimo.level);
            $(".powerLevel.elyril").html("*" + data.Eskimo.powerLevel);
            $(".progress.elyril").attr("max", data.Eskimo.nextLevelAt);
            $(".progress.elyril").attr("value", data.Eskimo.progressToNextLevel);
            //Second Character Data
            $(".level.solo").html(data.Solo.level);
            $(".powerLevel.solo").html("*" + data.Solo.powerLevel);
            $(".progress.solo").attr("max", data.Solo.nextLevelAt);
            $(".progress.solo").attr("value", data.Solo.progressToNextLevel);
            //Third Character Data
            $(".level.tigress").html(data.Tigress.level);
            $(".powerLevel.tigress").html("*" + data.Tigress.powerLevel);
            $(".progress.tigress").attr("max", data.Tigress.nextLevelAt);
            $(".progress.tigress").attr("value", data.Tigress.progressToNextLevel);
            //Crucible Data
            $(".standing").html(data.PVP.standing);
            $(".kdr").html(data.PVP.kdr);
            //Loading Images
            $(".characterPlate.elyril").css("background-image", "url(img/backgrounds/" + data.Eskimo.background + ")");
            $(".emblem.elyril").css("background-image", "url(img/emblems/" + data.Eskimo.emblem + ")");
            $(".characterPlate.solo").css("background-image", "url(img/backgrounds/" + data.Solo.background + ")");
            $(".emblem.solo").css("background-image", "url(img/emblems/" + data.Solo.emblem + ")");
            $(".characterPlate.tigress").css("background-image", "url(img/backgrounds/" + data.Tigress.background + ")");
            $(".emblem.tigress").css("background-image", "url(img/emblems/" + data.Tigress.emblem + ")");
            $(".cruciblePlate").css("background-image", "url(img/backgrounds/Crucible.BG.jpg)");
            $(".emblem.crucible").css("background-image", "url(img/emblems/Crucible.EM.jpg)");
            setTimeout("loadData()", 5000);
        });
} //end function

$(document).ready(function() {
    //DOCUMENT READY FUNCTION
    loadData();
});

//$(document).ready(function () {
//	$( ".level.solo" ).html(solo.level);
//	$.getJSON("info.json", function(result){
//		elyril.level = result.elyril.level;
//	});

//	var data = $.load("info.json");
//	console.log(result);
//});
