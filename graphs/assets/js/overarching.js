var Highcharts;

var url = "https://raw.githubusercontent.com/thirdreading/investments/develop/warehouse/expenditure/diagrams/overarching.json"

// Generate curves
jQuery.getJSON(url, function (source){

  var keys = [],
      dataset = [];

  keys = source.columns;
  dataset = source.data;

  Highcharts.chart('container', {

      title: {
          useHTML: true,
          text: 'Central Government'
      },

      subtitle: {
          text: 'Note that the node is initially collapsed!'
      },

      series: [{
          fillSpace: false,
          marker: {
              radius: 25
          },
          type: 'treegraph',
          keys: keys,
          data: dataset,
          dataLabels: {
              format: '{point.id}'
          },
          tooltip: {
            pointFormat: '<b>{point.name}</b><br/>'
          }
      }]

  });

});

document.querySelectorAll('.toggle-collapse-node').forEach(btn => {
    const pointIndex = btn.dataset.value;
    btn.addEventListener('click', () => {
        Highcharts.charts.forEach(chart => {
            chart.series[0].points[pointIndex].update({
                collapsed: !chart.series[0].points[pointIndex].options.collapsed
            });
        });
    });
});
