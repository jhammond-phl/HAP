// Add new charts by creating a new one like below and adding the following tag into the 
// HTML: <div class="ct-chart ct-square" id="chart2"></div> (where chart2 is whatever follows the #)
// For the tooltips, meta would be the text you want the popup to show, and value will be the number for both the chart
// labels are for the X axis

document.addEventListener("DOMContentLoaded",function(){

Papa.parse("https://raw.githubusercontent.com/jhammond-phl/HAP/master/writeData.csv", {
  download: true,
  delimiter: ",",
  header:true,
  complete: function(results){
    console.log("Finished: ", results.data)
    var homeless= results.data[0]
    var aff30 = results.data[1]
    var aff50 = results.data[2]
    var aff80 = results.data[3]
    var workforce = results.data[4]
    var market = results.data[5]
    var total = results.data[6]
    console.log(homeless["Owner Preserved Units"])
    console.log(aff30["Renter Preserved Units"])
    var aff30RentPres = aff30["Renter Preserved Units"]
    console.log(aff30RentPres)
    console.log(aff50)
    console.log(aff80)
    console.log(workforce)
    console.log(market)
    console.log(total)
    console.log(aff30RentPres)
    
    var app = angular.module('myApp',[]); 
    app.controller('myCtrl', function($scope) {
      $scope.firstName = "John";
      $scope.lastName = "Doe";
      console.log("jOn");
      console.log(aff30RentPres);
      $scope.homelessPO = Number(homeless["Owner Preserved Units"]);
      $scope.homelessNO = Number(homeless["Owner New Units"]);
      $scope.homelessPR = Number(homeless["Renter Preserved Units"]);
      $scope.homelessNR = Number(homeless["Renter New Units"]);
      $scope.aff30PO = Number(aff30["Owner Preserved Units"]);
      $scope.aff30NO = Number(aff30["Owner New Units"]);
      $scope.aff30PR = Number(aff30["Renter Preserved Units"]);
      $scope.aff30NR = Number(aff30["Renter New Units"]);
      $scope.aff50PO = Number(aff50["Owner Preserved Units"]);
      $scope.aff50NO = Number(aff50["Owner New Units"]);
      $scope.aff50PR = Number(aff50["Renter Preserved Units"]);
      $scope.aff50NR = Number(aff50["Renter New Units"]);
      $scope.aff80PO = Number(aff80["Owner Preserved Units"]);
      $scope.aff80NO = Number(aff80["Owner New Units"]);
      $scope.aff80PR = Number(aff80["Renter Preserved Units"]);
      $scope.aff80NR = Number(aff80["Renter New Units"]);
      $scope.workforcePO = Number(workforce["Owner Preserved Units"]);
      $scope.workforceNO = Number(workforce["Owner New Units"]);
      $scope.workforcePR = Number(workforce["Renter Preserved Units"]);
      $scope.workforceNR = Number(workforce["Renter New Units"]);
      $scope.marketPO = Number(market["Owner Preserved Units"]);
      $scope.marketNO = Number(market["Owner New Units"]);
      $scope.marketPR = Number(market["Renter Preserved Units"]);
      $scope.marketNR = Number(market["Renter New Units"]);
    }
    );
}})
})
