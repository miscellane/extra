// Declarations
var Highcharts;
var seriesOptions = [];
var url = document.getElementById("deflator").getAttribute("url");


// Generate curves
jQuery.getJSON(url, function (calculations){


	// Data
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
  Highcharts.chart('container0005', {

		// Chart
    chart: {
      type: 'spline',
      zoomType: 'xy',
      marginTop: 85,
      height: 390,
      width: 360
    },


		// Title
    title: {
      text: 'Deflator Series',
      margin: 25
    },


		// Subtitle
    subtitle: {
      y: 50,
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
      enabled: false
    },


		// Graph caption
    caption: {
      verticalAlign: "bottom",
      x: 35,
      y: 25,
      text: '<p><b>Base Year</b>: ' + calculations.attribute[0].year + '<br/></p>'
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
      title: {
        text: 'monetary units'
      },
      maxPadding: 0.05,
      gridLineWidth: 0.5,
      min: 0,
      resize: {
        enabled: true
      },
      plotLines: [{
        value: calculations.attribute[0].rebase,
        width: 0.85,
        color: '#5b5b5b'
      }]
    },


		// The x-axis
    xAxis: {
      type: 'datetime',
      title: {
          text: 'Year'
      },
      maxPadding: 0.05,
      gridLineWidth: 0.5,
      plotLines: [{
        value: calculations.attribute[0].epoch,
        width: 0.85,
        color: '#5b5b5b'
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
        color: '#5b5b5b5',
        marker: {
          enabled: true,
          radius: 2,
          fillColor: '#5b5b5b'
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