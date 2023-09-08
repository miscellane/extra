var Highcharts;
var optionSelected;
var dropdown = $("#option_selector");

var url = document.getElementById("delta").getAttribute("url");
var url = document.getElementById("delta").getAttribute("variable");



// Build data selection menu
$.getJSON(url, function (source) {

		// Partition
    let partitions = source.partitions;
    var pa = partitions.indexOf('series_delta_%');

    // Data parts of ...
    let data = source.data[pa];

		// Menu
    for (var k = 0; k < (data.length - 1); k += 1) {
        dropdown.append($("<option></option>").attr("value", data[k].name).text(data[k].description));
    }

    // Load the first Option by default
    var defaultOption = dropdown.find("option:first-child").val();
    optionSelected = dropdown.find("option:first-child").text();

    // Generate
    generateChart(defaultOption);

});

