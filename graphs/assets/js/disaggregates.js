// Declarations
var Highcharts;
var optionSelected;
var dropdown = $('#option_selector');
var url = 'https://raw.githubusercontent.com/thirdreading/investments/develop/warehouse/expenditure/metrics/disaggregates/menu.json';


// Menu data
$.getJSON(url, function (data) {

    $.each(data, function (key, entry) {
        dropdown.append($('<option></option>').attr('value', entry.name).text(entry.desc));
    });

    // Load the first Option by default
    var defaultOption = dropdown.find("option:first-child").val();
    optionSelected = dropdown.find("option:first-child").text();

    // Generate
    generateChart(defaultOption, optionSelected);

});


// Dropdown
dropdown.on('change', function (e) {

    $('#option_selector_title').remove();

    // Save name and value of the selected option
    optionSelected = this.options[e.target.selectedIndex].text;
    var valueSelected = this.options[e.target.selectedIndex].value;

    //Draw the Chart
    generateChart(valueSelected, optionSelected);
});

// Draw
function generateChart(fileNameKey, fileNameValue){

	// Generate curves
	$.getJSON('https://raw.githubusercontent.com/thirdreading/investments/develop/warehouse/expenditure/metrics/disaggregates/' + fileNameKey + '.json', function (source){

		// Definitions
        var total = [],
            percentage = [],
            groupingUnits = [[
                'year',   // unit name
                [1]      // allowed multiples
            ]],
            i = 0;

        // Partition
        let partitions = source.partitions;
        var ot = partitions.indexOf('OTE'), an = partitions.indexOf('annual_code_%'), se = partitions.indexOf('series_delta_%');

	});

}