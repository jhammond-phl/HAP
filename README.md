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
    <td>{{ homelessPO | currency:'USD' }}</td>
    <td>{{ homelessNO | number }}</td>
    <td>{{ homelessPR | number }}</td>
    <td>{{ homelessNR | number }}</td>
    <td>{{ homelessPO + homelessNO + homelessPR + homelessNR | number }}</td>
    <td>250</td>
    <td>2,500</td>
  </tr>
  <tr class="affordableRow" height="20" style="height:15.0pt">
    	<td rowspan="3" style="text-align:center"><b>Affordable</b></td>
      <td style="text-align:center">&nbsp;&lt;30%</td>
      <td style="text-align:center">$0 - 25,000</td>
			<td>{{ aff30PO | number }}</td>
      <td>{{ aff30NO | number }}</td>
      <td>{{ aff30PR | number }}</td>
      <td>{{ aff30NR | number }}</td>
			<td>{{ aff30PO + aff30NO + aff30PR  + aff30NR | number}}</td>
			<td>3,940</td>
			<td>39,400</td>
		</tr>
		<tr class="affordableRow" height="22" style="height:16.5pt">
      <td style="text-align:center">30-50%</td>
      <td style="text-align:center">$25,000 - 42,000</td>
			<td>{{ aff50PO | number }}</td>
      <td>{{ aff50NO | number }}</td>
      <td>{{ aff50PR | number }}</td>
      <td>{{ aff50NR | number }}</td>
			<td>{{ aff50PO + aff50NO + aff50PR  + aff50NR | number}}</td>
			<td>1,220</td>
			<td>12,200</td>
		</tr>
		<tr class="affordableRow" height="22" style="height:16.5pt">
      <td style="text-align:center">50-80%</td>
      <td style="text-align:center">$42,000 - 67,000</td>
			<td>{{ aff80PO | number }}</td>
      <td>{{ aff80NO | number }}</td>
      <td>{{ aff80PR | number }}</td>
      <td>{{ aff80NR | number }}</td>
			<td>{{ aff80PO + aff80NO + aff80PR  + aff80NR | number}}</td>
			<td>1,940</td>
			<td>19,400</td>
		</tr>
    <tr class="workforceRow" height="20" style="height:15.0pt">
			<td style="text-align:center"><b>Workforce</b></td>
			<td style="text-align:center">80-120%</td>
			<td style="text-align:center">$67,000-100,000</td>
			<td>{{ workforcePO | number }}</td>
      <td>{{ workforceNO | number }}</td>
      <td>{{ workforcePR | number }}</td>
      <td>{{ workforceNR | number }}</td>
			<td>{{ workforcePO + workforceNO + workforcePR  + workforceNR | number}}</td>
			<td>1,150</td>
			<td>11,500</td>
    </tr>
    <tr class="marketRateRow" height="40" style="height:30.0pt">
			<td style="text-align:center"><b>Market-Rate</b></td>
			<td style="text-align:center"></td>
			<td></td>
      <td>{{ marketPO | number }}</td>
      <td>{{ marketNO | number }}</td>
      <td>{{ marketPR | number }}</td>
      <td>{{ marketNR | number }}</td>
			<td>{{ marketPO + marketNO + marketPR  + marketNR | number}}</td>
			<td>1,500</td>
			<td>15,000</td>
    </tr>
    <tfoot height="20" style="height:15.0pt">
			<td style="text-align:center"><b>Total</b></td>
			<td></td>
			<td></td>
			<td style="text-align:right">{{ homelessPO + aff30PO + aff50PO + aff80PO + workforcePO + marketPO | number }}</td>
			<td style="text-align:right">{{ homelessNO + aff30NO + aff50NO + aff80NO + workforceNO + marketNO | number }}</td>
			<td style="text-align:right">{{ homelessPR + aff30PR + aff50PR + aff80PR + workforcePR + marketPR | number }}</td>
			<td style="text-align:right">{{ homelessNR + aff30NR + aff50NR + aff80NR + workforceNR + marketNR | number }}</td>
			<td style="text-align:right">{{ homelessPO + aff30PO + aff50PO + aff80PO + workforcePO + marketPO + homelessNO + aff30NO + aff50NO + aff80NO + workforceNO + marketNO + homelessPR + aff30PR + aff50PR + aff80PR + workforcePR + marketPR + homelessNR + aff30NR + aff50NR + aff80NR + workforceNR + marketNR | number }}</td>
			<td style="text-align:right">10,000</td>
			<td style="text-align:right">100,000</td>
    </tfoots>
</tbody>
</table>
