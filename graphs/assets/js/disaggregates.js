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
        var to = partitions.indexOf('OTE');


        // Splits
        for (var i = 0; i < source.data[to].length; i += 1) {
            total[i] = {
                name: source.data[to][i].description,
                visible: visible,
                data: source.data[to][i].data
            };
        }


        // Selector
        rangeSelector: {
            buttonPosition: {
            x: 0,
            y: 0
	        },
	        buttons: [
	          {
	            type: 'year',
	            count: 5,
	            text: '5y',
	            title: 'View 5 years',
	            dataGrouping: {
	              units: [['year', [1]]]
	            }
	          }, {
	           type: 'year',
	           count: 10,
	           text: '10y',
	           title: 'View 10 years',
	           dataGrouping: {
	             units: [['year', [1]]]
	           }
	          }, {
	            type: 'all',
	            text: 'All',
	            title: 'View all'
	          }
	        ],
	        floating: false,
	        inputDateFormat: '%Y',
	        inputEnabled: true,
	        inputPosition: {
	            x: 0,
	            y: 0
	        },
	        selected: 5,
	        verticalAlign: 'top'
	    },


	    // Chart
	    chart: {
            zoomType: 'x',
            type: 'spline',
            height: 635,
            width: 395
        },


		// Title
        title: {
            text: 'Expenditure'
        },


		// Subtitle
        subtitle: {
            text: '<p>Annual Central Government Expenditure</p> <br/> ' +
                '<p><b>...</b></p>'
        },


        // Credits
        credits: {
            enabled: true
        },


        // Legend
        legend: {
            enabled: true,
            layout: 'horizontal',
            align: 'center',
            itemStyle: {
                fontSize: '11px',
                width: '150px',
                textOverflow: 'ellipsis'
            },
            verticalAlign: 'bottom',
            margin: 25,
            width: 560,
            x: 85
        },


        // Exporting
        exporting: {
            buttons: {
                contextButton: {
                    menuItems: [ 'viewFullscreen', 'printChart', 'separator',
                        'downloadPNG', 'downloadJPEG', 'downloadPDF', 'downloadSVG' , 'separator',
                        'downloadXLS', 'downloadCSV']
                }
            }
        },


        // Axes
        xAxis: {
          gridLineWidth: 0.5
        },

        yAxis: {
             labels: {
                 align: 'left',
                 x: 5
             },
             title: {
                 text: 'Annual Transaction<br>Total (m£)',
                 align: 'middle',
                 margin: 5,
                 x: 9
             },
             min: 0,
             height: '42.5%',
             lineWidth: 0.05,
             resize: {
                 enabled: true
            }
        },


        // Plot Options
        plotOptions: {
            series: {
                marker: {
                    enabled: true,
                    radius: 1,
                    symbol: 'circle'
                },
                lineWidth: 0.5,
                turboThreshold: 4000,
                dataGrouping: {
                  units: groupingUnits
                }
            }

        },


		// Colours
        colors: ['#722f37', '#a000c8', '#800000', '#FFA500', '#6b8e23',
                 '#000000', '#999090', '#8080ff', '#ff9966', '#214949'],


        // Series
        series: total

	});

}



















