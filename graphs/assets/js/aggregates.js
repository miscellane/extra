// Declarations
var Highcharts;
var optionSelected;
var url = document.getElementById("aggregates").getAttribute("url");


// Generate graphs
jQuery.getJSON(url, function (source) {


    // Definitions
    var total = [],
        percentage = [],
        groupingUnits = [[
            'year',   // unit name
            [1]      // allowed multiples
        ]],
        i = 0;


    // Splits
    for (var i = 0; i < source.data[0].length; i += 1) {

        if (['GF02', 'GF05', 'GF07', 'GF09', 'GF10'].includes(source.data[0][i].name))
            visible = true;
        else
            visible = false;

        total[i] = {
            name: source.data[0][i].description,
            visible: visible,
            data: source.data[0][i].data
        };
    }

    for (var i = 0; i < source.data[1].length; i += 1) {
        percentage[i] = {
            name: source.data[1][i].description,
            data: source.data[1][i].data
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

        chart: {
            zoomType: 'x',
            type: 'spline',
            height: 635,
            width: 395
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

        exporting: {
            buttons: {
                contextButton: {
                    menuItems: [ 'viewFullscreen', 'printChart', 'separator',
                        'downloadPNG', 'downloadJPEG', 'downloadPDF', 'downloadSVG' , 'separator',
                        'downloadXLS', 'downloadCSV']
                }
            }
        },

        xAxis: {
          gridLineWidth: 0.5
        },

        yAxis: [{
            labels: {
                align: 'left',
                x: 5
            },
            title: {
                text: 'Annual Segment<br>Total (m£)',
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
        }, {
           labels: {
               align: 'left',
               x: 5
           },
           title: {
               text: 'Annual Segment<br>Percentage (%)',
               align: 'middle',
               margin: 5,
               x: 21
           },
           min: 0,
           top: '49.5%',
           height: '42.5%',
           lineWidth: 0.05,
           resize: {
               enabled: true
           },
           offset: 0
       }],

        tooltip: {
            shared: true,
            split: false,
            style: {
                fontSize: '11px'
            },
            padding: 15
        },

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
            },
            column: {
              borderWidth: 0,
              opacity: 0.65,
              stacking: 'normal'
            }

        },

        colors: ['#722f37', '#a000c8', '#800000', '#FFA500', '#6b8e23',
                 '#000000', '#999090', '#8080ff', '#ff9966', '#214949'],

        series: [{
	          name: total[0].name,
	          visible: total[0].visible,
	          data: total[0].data,
	          tooltip: {
		          pointFormat: '<br/><p><span style="color:{point.color}">{series.name}</span>: {point.y:,.2f}m£<br/></p>'
	          },
	          yAxis: 0,
	          id: "0"
        }, {
	         name: total[1].name,
	         visible: total[1].visible,
	         data: total[1].data,
	         tooltip: {
	            pointFormat: '<br/><p><span style="color:{point.color}">{series.name}</span>: {point.y:,.2f}m£<br/></p>'
	         },
	         yAxis: 0,
	         id: "1"
       }, {
	         name: total[2].name,
	         visible: total[2].visible,
	         data: total[2].data,
	         tooltip: {
	            pointFormat: '<br/><p><span style="color:{point.color}">{series.name}</span>: {point.y:,.2f}m£<br/></p>'
	         },
	         yAxis: 0,
	         id: "2"
       }, {
           name: total[3].name,
           visible: total[3].visible,
           data: total[3].data,
           tooltip: {
              pointFormat: '<br/><p><span style="color:{point.color}">{series.name}</span>: {point.y:,.2f}m£<br/></p>'
           },
           yAxis: 0,
           id: "3"
       }, {
           name: total[4].name,
           visible: total[4].visible,
           data: total[4].data,
           tooltip: {
              pointFormat: '<br/><p><span style="color:{point.color}">{series.name}</span>: {point.y:,.2f}m£<br/></p>'
           },
           yAxis: 0,
           id: "4"
       }, {
           name: total[5].name,
           visible: total[5].visible,
           data: total[5].data,
           tooltip: {
              pointFormat: '<br/><p><span style="color:{point.color}">{series.name}</span>: {point.y:,.2f}m£<br/></p>'
           },
           yAxis: 0,
           id: "5"
       }, {
           name: total[6].name,
           visible: total[6].visible,
           data: total[6].data,
           tooltip: {
              pointFormat: '<br/><p><span style="color:{point.color}">{series.name}</span>: {point.y:,.2f}m£<br/></p>'
           },
           yAxis: 0,
           id: "6"
       }, {
           name: total[7].name,
           visible: total[7].visible,
           data: total[7].data,
           tooltip: {
              pointFormat: '<br/><p><span style="color:{point.color}">{series.name}</span>: {point.y:,.2f}m£<br/></p>'
           },
           yAxis: 0,
           id: "7"
       }, {
           name: total[8].name,
           visible: total[8].visible,
           data: total[8].data,
           tooltip: {
              pointFormat: '<br/><p><span style="color:{point.color}">{series.name}</span>: {point.y:,.2f}m£<br/></p>'
           },
           yAxis: 0,
           id: "8"
       }, {
           name: total[9].name,
           visible: total[9].visible,
           data: total[9].data,
           tooltip: {
              pointFormat: '<br/><p><span style="color:{point.color}">{series.name}</span>: {point.y:,.2f}m£<br/><br/></p>'
           },
           yAxis: 0,
           id: "9"
       }, {
          name: percentage[0].name,
          type: 'column',
          data: percentage[0].data,
          tooltip: {
	            pointFormat: '<br/><br/><p><span style="color:{point.color}">{series.name}</span>: {point.y:,.2f}%<br/></p>'
	        },
          yAxis: 1,
          linkedTo: "0"
       }, {
          name: percentage[1].name,
          type: 'column',
          data: percentage[1].data,
          tooltip: {
              pointFormat: '<br/><p><span style="color:{point.color}">{series.name}</span>: {point.y:,.2f}%<br/></p>'
          },
          yAxis: 1,
          linkedTo: "1"
       }, {
          name: percentage[2].name,
          type: 'column',
          data: percentage[2].data,
          tooltip: {
              pointFormat: '<br/><p><span style="color:{point.color}">{series.name}</span>: {point.y:,.2f}%<br/></p>'
          },
          yAxis: 1,
          linkedTo: "2"
       }, {
          name: percentage[3].name,
          type: 'column',
          data: percentage[3].data,
          tooltip: {
              pointFormat: '<br/><p><span style="color:{point.color}">{series.name}</span>: {point.y:,.2f}%<br/></p>'
          },
          yAxis: 1,
          linkedTo: "3"
       }, {
          name: percentage[4].name,
          type: 'column',
          data: percentage[4].data,
          tooltip: {
              pointFormat: '<br/><p><span style="color:{point.color}">{series.name}</span>: {point.y:,.2f}%<br/></p>'
          },
          yAxis: 1,
          linkedTo: "4"
       }, {
          name: percentage[5].name,
          type: 'column',
          data: percentage[5].data,
          tooltip: {
              pointFormat: '<br/><p><span style="color:{point.color}">{series.name}</span>: {point.y:,.2f}%<br/></p>'
          },
          yAxis: 1,
          linkedTo: "5"
       }, {
          name: percentage[6].name,
          type: 'column',
          data: percentage[6].data,
          tooltip: {
              pointFormat: '<br/><p><span style="color:{point.color}">{series.name}</span>: {point.y:,.2f}%<br/></p>'
          },
          yAxis: 1,
          linkedTo: "6"
       }, {
          name: percentage[7].name,
          type: 'column',
          data: percentage[7].data,
          tooltip: {
              pointFormat: '<br/><p><span style="color:{point.color}">{series.name}</span>: {point.y:,.2f}%<br/></p>'
          },
          yAxis: 1,
          linkedTo: "7"
       }, {
          name: percentage[8].name,
          type: 'column',
          data: percentage[8].data,
          tooltip: {
              pointFormat: '<br/><p><span style="color:{point.color}">{series.name}</span>: {point.y:,.2f}%<br/></p>'
          },
          yAxis: 1,
          linkedTo: "8"
       }, {
          name: percentage[9].name,
          type: 'column',
          data: percentage[9].data,
          tooltip: {
              pointFormat: '<br/><p><span style="color:{point.color}">{series.name}</span>: {point.y:,.2f}%<br/></p>'
          },
          yAxis: 1,
          linkedTo: "9"
       }]
    });

});
