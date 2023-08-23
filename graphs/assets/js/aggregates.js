var Highcharts;
var optionSelected;
var url = document.getElementById("aggregates").getAttribute("url");


// Generate graphs
jQuery.getJSON(url, function (source) {

    // https://api.highcharts.com/highstock/plotOptions.series.dataLabels
    // https://api.highcharts.com/class-reference/Highcharts.Point#.name
    // https://api.highcharts.com/highstock/tooltip.pointFormat


    // split the data set parts
    var dataLength = source.data.length,
        groupingUnits = [[
            'year',   // unit name
            [1]      // allowed multiples
        ]],
        i = 0;

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
            width: 500,
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
            height: '23%',
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
            top: '26%',
            height: '23%',
            offset: 0,
            lineWidth: 2
        }, {
            labels: {
                align: 'left',
                x: 5
            },
            title: {
                text: 'Annual Segment<br>Delta',
                align: 'middle',
                x: 7
            },
            top: '52%',
            height: '23%',
            offset: 0,
            lineWidth: 2
        }, {
             labels: {
                 align: 'left',
                 x: 5
             },
             title: {
                 text: 'Total',
                 align: 'middle',
                 x: 7
             },
             top: '78%',
             height: '18%',
             offset: 0,
             lineWidth: 2
           }
        ],

        plotOptions: {
            series: {
                turboThreshold: 650000
            }
        },

        tooltip: {
            split: true,
            dateTimeLabelFormats: {
                millisecond: "%A, %e %b, %H:%M:%S.%L",
                second: "%A, %e %b, %H:%M:%S",
                minute: "%A, %e %b, %H:%M",
                hour: "%A, %e %b, %H:%M",
                day: "%A, %e %B, %Y",
                week: "%A, %e %b, %Y",
                month: "%B %Y",
                year: "%Y"
            }

        },

        series: [{
            type: 'spline',
            name: source.partitions[0],
            data: source.data[0],
            dataGrouping: {
                units: groupingUnits,
                dateTimeLabelFormats: {
                    millisecond: ['%A, %e %b, %H:%M:%S.%L', '%A, %b %e, %H:%M:%S.%L', '-%H:%M:%S.%L'],
                    second: ['%A, %e %b, %H:%M:%S', '%A, %b %e, %H:%M:%S', '-%H:%M:%S'],
                    minute: ['%A, %e %b, %H:%M', '%A, %b %e, %H:%M', '-%H:%M'],
                    hour: ['%A, %e %b, %H:%M', '%A, %b %e, %H:%M', '-%H:%M'],
                    day: ['%A, %e %b, %Y', '%A, %b %e', '-%A, %b %e, %Y'],
                    week: ['Week from %A, %e %b, %Y', '%A, %b %e', '-%A, %b %e, %Y'],
                    month: ['%B %Y', '%B', '-%B %Y'],
                    year: ['%Y', '%Y', '-%Y']
                }
            },
            tooltip: {
                pointFormat: '<span style="color:{point.color}">\u25CF</span> <b> {series.name}</b>: ' +
                    '{point.y:,.2f}m£<br/>'
            }
        },
            {
                type: 'spline',
                name: source.partitions[1],
                data: source.data[1],
                color: '#6B8E23',
                yAxis: 1,
                dataGrouping: {
                    units: groupingUnits
                },
                tooltip: {
                    pointFormat: '<span style="color:{point.color}">\u25CF</span> <b> {series.name}</b>: ' +
                        '{point.y:,.2f}%<br/>'
                }
            },
            {
                type: 'spline',
                name: source.partitions[2],
                data: source.data[2],
                color: '#A08E23',
                visible: true,
                yAxis: 2,
                dataGrouping: {
                    units: groupingUnits
                },
                tooltip: {
                    pointFormat: '<span style="color:{point.color}">\u25CF</span> <b> {series.name}</b>: ' +
                        '{point.y:,.2f}%<br/>'
                }
            },
            {
                type: 'column',
                name: 'Total',
                data: source.data[0],
                stacking: 'normal',
                yAxis: 3,
                dataGrouping: {
                    units: groupingUnits
                },
                tooltip: {
                    pointFormat: '<span style="color:{point.color}">\u25CF</span> <b> {series.name}</b>: ' +
                        '{point.y:,.2f}m£<br/>'
                }
            }
        ],
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

}).fail(function () {
    console.log("Missing");
    $('#container0001').empty();
});
