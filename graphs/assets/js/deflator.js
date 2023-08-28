var Highcharts;
var seriesOptions = [];
var url = document.getElementById("deflator").getAttribute("url");


// Generate curves
jQuery.getJSON(url, function (calculations){

	seriesOptions[0] = {
		name: calculations.description,
		data: calculations.data
	};

  // Definitions
  var groupingUnits = [[
      'year',   // unit name
      [1]       // allowed multiples
    ]];

  // Numbers
  Highcharts.setOptions({
    lang: {
      thousandsSep: ','
    }
  });


  // Draw a graph
  Highcharts.stockChart('container0005', {

		// https://api.highcharts.com/highstock/rangeSelector.buttons
    rangeSelector: {
	    buttonPosition: {
          x: 0,
          y: 0
        },
      buttons: [
        {
          type: 'ytd',
          text: 'YTD',
          title: 'View year to date'
        }, {
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
      selected: 5,  // The default range selection button: All -> 5
      verticalAlign: 'top'
    },

		// Chart
    chart: {
      zoomType: 'x'
      // borderWidth: 2,
      // marginRight: 100
    },

		// Title
    title: {
      text: 'Deflator Series'
    },

		// Subtitle
    subtitle: {
      text: '<p>Country: United Kingdom, Base Year: ' + calculations.attribute[0].year + '</p>'
    },

		// Time
    time: {
      // timezone: 'Europe/London'
    },

		// Credits
    credits: {
      enabled: false
    },

		// Legend
    legend: {
      enabled: true,
      width: 600,
      x: 65,
      y: -45,
      align: 'middle'
    },

		// Graph caption
    caption: {
      verticalAlign: "bottom",
      y: 25,
      text: '<p>This series is a <b>rebased</b> United Kingdom Treasury\'s deflator series.  At present, the base' +
        'year of the treasury\'s series is the latest year in the series.  The series is rebased such' +
        'that the base year is <b>2010</b>.</p>'
    },

		// Export options
    exporting: {
      buttons: {
        contextButton: {
          menuItems: [ 'viewFullscreen', 'printChart', 'separator',
            'downloadPNG', 'downloadJPEG', 'downloadPDF', 'downloadSVG' , 'separator',
            'downloadXLS', 'downloadCSV']
        }
      }
    },

		// The y-axis
    yAxis: {
      labels: {
        align: 'left',
        x: 5
      },
      title: {
        text: 'monetary units',
        align: 'middle',
        x: 7
      },
      min: 0,
      lineWidth: 2,
      resize: {
        enabled: true
      },
      plotLines: [{
        value: calculations.attribute[0].rebase,
        width: 2,
        color: 'orange'
      }]
    },

    xAxis: {
      plotLines: [{
        value: calculations.attribute[0].epoch,
        width: 1.5,
        color: 'orange'
      }]
    },

		// Tooltip
    tooltip: {
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

		// Plot options
    plotOptions: {
      series: {
        turboThreshold: 4000,
        marker: {
          enabled: true,
          radius: 3
        },
        dataGrouping: {
          units: groupingUnits
        },
        tooltip: {
          pointFormat: '<span style="color:{point.color}">\u25CF</span> <b>{series.name}</b>:<br/>' +
            '&nbsp; &nbsp;{point.y:,.2f}<br/>'
        }
      }
    },

    series: seriesOptions

  });

});