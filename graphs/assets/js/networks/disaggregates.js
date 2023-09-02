var Highcharts;

var url = "https://raw.githubusercontent.com/thirdreading/investments/develop/warehouse/expenditure/diagrams/disaggregates.json"


// Generate curves
jQuery.getJSON(url, function (source){

	// Indices
	let columns = source.columns;
	var pa = columns.indexOf('parent_desc'), ch = columns.indexOf('child_desc');

	// Data
	var data = [];
	for (var i = 0; i < source.data.length; i += 1){

		// parent, child
		data.push([
			source.data[i][pa], source.data[i][ch]
		]);

	}


	// Add the nodes option through an event call. We want to start with the parent
	// item and apply separate colors to each child element, then the same color to
	// grandchildren.
	Highcharts.addEvent(Highcharts.Series, 'afterSetOptions',
	    function (e) {
	        var colors = Highcharts.getOptions().colors,
	            i = 0,
	            nodes = {};

	        if (
	            this instanceof Highcharts.Series.types.networkgraph &&
	            e.options.id === 'segments'
	        ) {
	            e.options.data.forEach(function (link) {

	                if (link[0] === 'Central Government Expenditure') {
	                    nodes['Central Government Expenditure'] = {
	                        id: 'Central Government Expenditure',
	                        marker: {
	                            radius: 24
	                        }
	                    };
	                    nodes[link[1]] = {
	                        id: link[1],
	                        marker: {
	                            radius: 16
	                        },
	                        color: colors[i++]
	                    };
	                } else if (nodes[link[0]] && nodes[link[0]].color) {
	                    nodes[link[1]] = {
	                        id: link[1],
	                        color: nodes[link[0]].color
	                    };
	                }
	            });

	            e.options.nodes = Object.keys(nodes).map(function (id) {
	                return nodes[id];
	            });
	        }
	    }
	);

	Highcharts.chart('container', {
	    chart: {
	        type: 'networkgraph',
	        height: '100%'
	    },
	    title: {
	        text: 'Central Government',
	        align: 'left'
	    },
	    subtitle: {
	        text: 'Force-Directed Network Graph',
	        align: 'left'
	    },
	    plotOptions: {
	        networkgraph: {
	            keys: ['from', 'to'],
	            layoutAlgorithm: {
	                enableSimulation: true,
	                friction: -0.9
	            }
	        }
	    },
	    series: [{
	        accessibility: {
	            enabled: false
	        },
	        dataLabels: {
	            enabled: true,
	            linkFormat: '',
	            style: {
	                fontSize: '0.8em',
	                fontWeight: 'normal'
	            }
	        },
	        id: 'segments',
	        data: data
	    }]
	});

});