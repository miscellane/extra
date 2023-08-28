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
      text: 'Deflator Series'
    },

    subtitle: {
      text: 'Country: United Kingdom, Base Year: '
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
      y: 15
      // align: 'middle'
      // layout: 'vertical'
      // verticalAlign: 'bottom'
    },

    caption: {
      verticalAlign: "bottom",
      y: 25,
      text: '<p>This series is a <b>rebased</b> United Kingdom Treasury\'s deflator series.  At present, the  ' +
        'base year of the treasury\'s series is the latest year in the series.  The series is rebased such ' +
        'that the base year is <b>2010</b>.</p>'
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
      }
    },

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
          headerFormat: '<p><span style="font-size: 13px; color:#aab597">\u25CF {point.x:.0f}</span></p>',
          pointFormat: '<span style="color:{point.color}">\u25CF</span> <b> {series.name} </b>: ' +
            '{point.y:,.2f}<br/>'
        }
      }
    },

    series: seriesOptions

  });

});