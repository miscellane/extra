var Highcharts;
var optionSelected;
var url = document.getElementById("aggregates").getAttribute("url");


// Generate graphs
jQuery.getJSON(url, function (source) {

    // https://api.highcharts.com/highstock/plotOptions.series.dataLabels
    // https://api.highcharts.com/class-reference/Highcharts.Point#.name
    // https://api.highcharts.com/highstock/tooltip.pointFormat


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
            selected: 1,
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
            x: 65
            // align: 'middle',
            // layout: 'vertical',
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
                x: 7
            },
            min: 0,
            height: '40%',
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
               x: 7
           },
           min: 0,
           top: '45%',
           height: '40%',
           lineWidth: 2,
           resize: {
               enabled: true
           }
       }
        ],

        plotOptions: {
            series: {
                marker: {
                    enabled: true,
                    radius: 2
                },
                lineWidth: 0.25,
                dataLabels: {
                    enabled: false
                },
                turboThreshold: 4000,
                dataGrouping: {
                  units: groupingUnits
              },
              tooltip: {
                  pointFormat: '<span style="color:{point.color}">\u25CF</span> <b> {series.name}</b>: ' +
                      '{point.y:,.2f}m£<br/>'
              }
            }
        },

        tooltip: {
            split: true
        },

        series: alpha,

        responsive: {
            rules: [{
                condition: {
                    maxWidth: 700
                },
                chartOptions: {
                    rangeSelector: {
                        inputEnabled: false
                    }
                }
            }]
        }
    });

});
