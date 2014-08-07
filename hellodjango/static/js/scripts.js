    onePageScroll(".main", {
       sectionContainer: "section",
       loop: false,
       responsiveFallback: false
    });

    $(function () {

	$('#skills').highcharts({

	    chart: {
	        polar: true,
	        type: 'line'
	    },

	    title: {
	        text: 'My relative computer skills',
	        x: -80
	    },

	    pane: {
	    	size: '90%'
	    },

	    xAxis: {
	        categories: ['Java', 'Python', 'MySQL', 'CSS',
	                'Android', 'HTML', 'Django', 'JavaScript'],
	        tickmarkPlacement: 'on',
	        lineWidth: 0
	    },

	    yAxis: {
	        gridLineInterpolation: 'polygon',
	        lineWidth: 0,
	        min: 0
	    },

	    series: [{
	        name: 'Skill Level',
	        data: [8, 9, 6, 3, 6, 5, 9, 4],
	        pointPlacement: 'off'
	    },]

	});
});