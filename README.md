 <h1>Current Unit Activity</h1>           
<div ng-app="myApp" ng-controller="myCtrl">

<table cellspacing="0" style="border-color:black; width: 100%">
<tbody>
  <thead height="20" style="height:15pt">
    <td height="60" rowspan="2">Housing Type</td>
    <td rowspan="2" >% Area Median Income</td>
    <td rowspan="2" >Household Income</td>
    <td colspan="2">Owner</td>
    <td colspan="2">Renter</td>
    <td rowspan="2">Current YTD</td>
    <td rowspan="2">Annual Goal</td>
    <td rowspan="2">10-Year Goal</td>
  </tr>
  <tr height="40" style="height:30.0pt">
    <td height="40" >Preserved Units</td>
    <td>New Units</td>
    <td>Preserved Units</td>
    <td>New Units</td>
    </tr>
  </thead>
  <tr id="homelessRow" height="20" style="height:15.0pt">
    <td height="20" style="text-align:center"><b>Homeless</b></td>
    <td style="text-align:center"></td>
    <td style="text-align:center"></td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>250</td>
    <td>2,500</td>
  </tr>
  <tr class="affordableRow" height="20" style="height:15.0pt">
    	<td rowspan="3" style="text-align:center"><b>Affordable</b></td>
      <td style="text-align:center">&nbsp;&lt;30%</td>
      <td style="text-align:center">$0 - 25,000</td>
			<td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
			<td>1</td>
			<td>3,940</td>
			<td>39,400</td>
		</tr>
		<tr class="affordableRow" height="22" style="height:16.5pt">
      <td style="text-align:center">30-50%</td>
      <td style="text-align:center">$25,000 - 42,000</td>
			<td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
			<td>1</td>
			<td>1,220</td>
			<td>12,200</td>
		</tr>
		<tr class="affordableRow" height="22" style="height:16.5pt">
      <td style="text-align:center">50-80%</td>
      <td style="text-align:center">$42,000 - 67,000</td>
			<td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
			<td>1</td>
			<td>1,940</td>
			<td>19,400</td>
		</tr>
    <tr class="workforceRow" height="20" style="height:15.0pt">
			<td style="text-align:center"><b>Workforce</b></td>
			<td style="text-align:center">80-120%</td>
			<td style="text-align:center">$67,000-100,000</td>
			<td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
			<td>1</td>
			<td>1,150</td>
			<td>11,500</td>
    </tr>
    <tr class="marketRateRow" height="40" style="height:30.0pt">
			<td style="text-align:center"><b>Market-Rate</b></td>
			<td style="text-align:center"></td>
			<td></td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
			<td>1</td>
			<td>1,500</td>
			<td>15,000</td>
    </tr>
    <tfoot height="20" style="height:15.0pt">
			<td style="text-align:center"><b>Total</b></td>
			<td></td>
			<td></td>
			<td style="text-align:right">1</td>
			<td style="text-align:right">1</td>
			<td style="text-align:right">1</td>
			<td style="text-align:right">1</td>
			<td style="text-align:right">1</td>
			<td style="text-align:right">10,000</td>
			<td style="text-align:right">100,000</td>
    </tfoots>
</tbody>
</table>
