var Highcharts;
var optionSelected;
var url = document.getElementById("aggregates").getAttribute("url");


// Generate graphs
jQuery.getJSON(url, function (source) {


    // Definitions
    var alpha = [],
        beta = [],
        gamma = [],
        groupingUnits = [[
            'year',   // unit name
            [1]      // allowed multiples
        ]],
        i = 0;


    // Splits
    for (var i = 0; i < source.data[0].length; i += 1) {
        alpha[i] = {
            name: source.data[0][i].description,
            data: source.data[0][i].data
        };
    }

    for (var i = 0; i < source.data[1].length; i += 1) {
        beta[i] = {
            name: source.data[1][i].description,
            data: source.data[1][i].data
        };
    }

    for (var i = 0; i < source.data[2].length; i += 1) {
        gamma[i] = {
            name: source.data[2][i].description,
            data: source.data[2][i].data
        };
    }

    // Numbers
    Highcharts.setOptions({
        lang: {
            thousandsSep: ','
        }
    });


    // Draw a graph
    Highcharts.stockChart('container0001', {

        rangeSelector: {
            selected: 5,
            verticalAlign: 'top',
            floating: false,
            inputPosition: {
                x: 0,
                y: 0
            },
            buttonPosition: {
                x: 0,
                y: 0
            },
            inputEnabled: true,
            inputDateFormat: '%Y'
        },

        chart: {
            zoomType: 'x'
            // borderWidth: 2,
            // marginRight: 100
        },

        title: {
            text: 'Expenditure'
        },

        subtitle: {
            text: '<p>Annual Central Government Expenditure</p> <br/> ' +
                '<p><b>United Kingdom</b></p>'
        },

        time: {
            // timezone: 'Europe/London'
        },

        credits: {
            enabled: false
        },

        legend: {
            enabled: true,
            width: 600,
            x: 65,
            // align: 'middle',
            layout: 'vertical',
            // verticalAlign: 'bottom',
            // y: 10,
            // x: 35
        },

        caption: {
            // verticalAlign: "top",
            // y: 35,
            text: '<p>The United Kingdom\'s expenditure summaries are split into central & local government summaries.  Each summary has ' +
                'a disaggregates tree.  This is a high level breakdown of central government expenditure across the years; deflator adjusted values.</p>'
        },

        exporting: {
            buttons: {
                contextButton: {
                    menuItems: [ 'viewFullscreen', 'printChart', 'separator',
                        'downloadPNG', 'downloadJPEG', 'downloadPDF', 'downloadSVG' , 'separator',
                        'downloadXLS', 'downloadCSV']
                }
            }
        },

        yAxis: [{
            labels: {
                align: 'left',
                x: 5
            },
            title: {
                text: 'Annual Segment<br>Total',
                align: 'middle',
                margin: 5,
                x: 9
            },
            min: 0,
            height: '35%',
            lineWidth: 2,
            resize: {
                enabled: true
            }
        }, {
           labels: {
               align: 'left',
               x: 5
           },
           title: {
               text: 'Annual Segment<br>Percentage',
               align: 'middle',
               margin: 5,
               x: 21
           },
           min: 0,
           top: '45%',
           height: '35%',
           lineWidth: 2,
           resize: {
               enabled: true
           },
           offset: 0
       }],

        tooltip: {
            shared: true,
            split: false,
            style: {
                fontSize: "11px"
            }
        },

        plotOptions: {
            series: {
                turboThreshold: 4000,
                dataGrouping: {
                  units: groupingUnits
                }
            }

        },

        colors: ['#722f37', '#FFA500', '#6b8e23'],

        series: [{
	          name: alpha[0].name,
	          data: alpha[0].data,
	          tooltip: {
		          pointFormat: '<br/><p><span style="color:{point.color}">{series.name}</span>: {point.y:,.2f}m£<br/></p>'
	          },
	          yAxis: 0,
	          id: "0"
        }, {
	         name: alpha[1].name,
	         data: alpha[1].data,
	         tooltip: {
	            pointFormat: '<br/><p><span style="color:{point.color}">{series.name}</span>: {point.y:,.2f}m£<br/></p>'
	         },
	         yAxis: 0,
	         id: "1"
       }, {
	         name: alpha[2].name,
	         data: alpha[2].data,
	         tooltip: {
	            pointFormat: '<br/><p><span style="color:{point.color}">{series.name}</span>: {point.y:,.2f}m£<br/></p>'
	         },
	         yAxis: 0,
	         id: "2"
       }, {
          name: beta[0].name,
          data: beta[0].data,
          tooltip: {
	            pointFormat: '<br/><br/><p><span style="color:{point.color}">{series.name}</span>: {point.y:,.2f}%<br/></p>'
	        },
          yAxis: 1,
          linkedTo: "0"
       }, {
          name: beta[1].name,
          data: beta[1].data,
          tooltip: {
              pointFormat: '<br/><p><span style="color:{point.color}">{series.name}</span>: {point.y:,.2f}%<br/></p>'
          },
          yAxis: 1,
          linkedTo: "1"
       }, {
          name: beta[2].name,
          data: beta[2].data,
          tooltip: {
              pointFormat: '<br/><p><span style="color:{point.color}">{series.name}</span>: {point.y:,.2f}%<br/></p>'
          },
          yAxis: 1,
          linkedTo: "2"
       }]

    });

});
