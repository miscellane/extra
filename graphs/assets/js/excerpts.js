var Highcharts;
var optionSelected;
var dropdown = $('#option_selector');
var url = 'https://raw.githubusercontent.com/thirdreading/investments/develop/graphs/assets/menu/excerpts.json';


$.getJSON(url, function (data) {

    $.each(data, function (key, entry) {
        dropdown.append($('<option></option>').attr('value', entry.name).text(entry.desc));
    });

    // Load the first Option by default
    var defaultOption = dropdown.find("option:first-child").val();
    optionSelected = dropdown.find("option:first-child").text();

    // Generate
    generateChart(defaultOption);

});


// Dropdown
dropdown.on('change', function (e) {

    $('#option_selector_title').remove();

    // Save name and value of the selected option
    optionSelected = this.options[e.target.selectedIndex].text;
    var valueSelected = this.options[e.target.selectedIndex].value;

    //Draw the Chart
    generateChart(valueSelected);
});

function generateChart(fileNameKey){

  // Generate curves
  $.getJSON('https://raw.githubusercontent.com/thirdreading/investments/develop/warehouse/expenditure/graphs/excerpts/' + fileNamekey + '.json', function (calculations){

      // https://api.highcharts.com/highstock/tooltip.pointFormat
      // https://jsfiddle.net/gh/get/library/pure/highcharts/highcharts/tree/master/samples/highcharts/demo/bubble
      // https://api.highcharts.com/highcharts/tooltip.headerFormat
      // https://www.highcharts.com/demo/stock/compare


      // Split
      for (var i = 0; i < calculations.length; i += 1) {

          seriesOptions[i] = {
              name: calculations[i].description,
              data: calculations[i].data
          };

      }


      // Graphing
      Highcharts.setOptions({
          lang: {
              thousandsSep: ","
          }
      });


      // Hence
      Highcharts.chart("container0003", {

          chart: {
              type: "line",
              zoomType: "xy",
              marginTop: 50,
              marginBottom: 160,
              height: 390,
              width: 330,
          },

          title: {
              text: 'Annual Central Government Expenditure',
              x: 0,
              y: 5,
              style: {
                  fontSize: '15px'
              }
          },
          subtitle: {
              text: 'United Kingdom',
              x: 0,
              y: 45,
              style: {
                  fontStyle: 'italic',
                  fontSize: '13px',
                  fontWeight: 'normal',
                  color: 'grey',
                  width: '80px'
              }
          },

          credits: {
              enabled: false
          },

          legend: {
              enabled: true,
              layout: 'horizontal',
              align: 'center',
              itemStyle: {
                  fontSize: '10px',
                  width: '100px',
                  textOverflow: 'ellipsis'
              },
              verticalAlign: 'bottom',
              margin: 40,
              itemMarginTop: 2,
              itemMarginBottom: 2,
              x: 7.5,
              y: 20,
              floating: true
          },

          xAxis: {
              title: {
                  text: 'Year'
              },
              maxPadding: 0.1,
              gridLineWidth: 1
          },

          yAxis: {
              title: {
                  text: "Expense<br>(million pounds)"
              },
              maxPadding: 0.05,
              min: 0,
              endOnTick: false
          },

          exporting: {
              buttons: {
                  contextButton: {
                      menuItems: ["viewFullscreen", "printChart", "separator",
                          "downloadPNG", "downloadJPEG", "downloadPDF", "downloadSVG", "separator",
                          "downloadXLS", "downloadCSV"]
                  }
              }
          },

          tooltip: {
              shared: true,
              headerFormat: '<p><span style="font-size: 13px; color:#aab597">\u25CF {point.x:.0f}</span></p>',
              pointFormat: '<br/><p><br/>' +
                  '<span style="color:{point.color}">{series.name}</span>: {point.y:,.2f} (m£)<br/></p>' ,
              style: {
                  fontSize: "11px"
              }
          },

          plotOptions: {
              series: {
                  marker: {
                      enabled: true,
                      radius: 1
                  },
                  lineWidth: 0.5,
                  dataLabels: {
                      enabled: false
                  },
                  turboThreshold: 4000
              }
          },

          series: seriesOptions

          /* responsive: {
              rules: [{
                  condition: {
                      maxWidth: 300
                  }
              }]
          } */

      });

  }).fail(function () {
    console.log("Missing");
    $('#container0003').empty();
  });

}
