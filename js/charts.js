// Add new charts by creating a new one like below and adding the following tag into the 
// HTML: <div class="ct-chart ct-square" id="chart2"></div> (where chart2 is whatever follows the #)
// For the tooltips, meta would be the text you want the popup to show, and value will be the number for both the chart
// labels are for the X axis

  new Chartist.Bar('#chart2', {
    labels: [1, 2, 3, 4],
    series: [
      [
        {meta: 'Amount', value: 5},
        {meta: 'Amount', value: 2},
        {meta: 'Amount', value: 8}, 
        {meta: 'Amount', value: 3}
      ]
    ]
  },{
    fullWidth: true,
    plugins: [
      Chartist.plugins.tooltip()
    ]
  });

x = 10000-41-5703-181-1346

  new Chartist.Pie('#chart3', {
    series: [
        {meta: 'Homeless', value: 41},
        {meta: 'Affordable', value: 5703},
        {meta: 'Workforce', value: 181},
        {meta: 'Market-Rate', value: 1346},
        {meta: 'Still needed to make goal', value: x}
    ]
  }, {
    donut: true,
    donutWidth: 40,
    startAngle: 270,
    total: 20000, // double the goal to make it a half arch but we could also make it more if we want it to be a horseshoe
    showLabel: false,
    plugins: [
      Chartist.plugins.tooltip()
    ]
  });