//javascript.js
var postData = "X-Requested-With=XMLHttpRequest&" + $("#submitform").serialize();


//set map options
var myLatLng = { lat: 41.881832, lng: -87.623177 };
var mapOptions = {
    center: myLatLng,
    zoom: 10,
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    strictBounds: true,
    types: ['geocode'],
    componentRestrictions: { country: "IL" }

};






//create map
var map = new google.maps.Map(document.getElementById('googleMap'), mapOptions);

//create a DirectionsService object to use the route method and get a result for our request
var directionsService = new google.maps.DirectionsService();

//create a DirectionsRenderer object which we will use to display the route
var directionsDisplay = new google.maps.DirectionsRenderer();

//bind the DirectionsRenderer to the map
directionsDisplay.setMap(map);


//define calcRoute function


   //Get the value of Start and End of Week


  function calcRoute() {
  
    //create request
    var request = {
        origin: document.getElementById("from").value,
        destination: document.getElementById("to").value,
        travelMode: google.maps.TravelMode.DRIVING, //WALKING, BYCYCLING, TRANSIT
        unitSystem: google.maps.UnitSystem.IMPERIAL
    }

    //pass the request to the route method
    directionsService.route(request, function (result, status) {
        if (status == google.maps.DirectionsStatus.OK) {
            
   var select_ride =  $("#id_ride_type").val(); // The value of the selected option

   var e = document.getElementById("id_ride_type");
     miles=parseFloat(result.routes[0].legs[0].distance.text);
     select_ride = e.options[e.selectedIndex].value;
     price = parseFloat(select_ride );
     elementi = document.getElementById("test");
     priceupdate=parseInt(price*miles);
     $('#id_price').val(priceupdate);
     $('#submitform').html('Book Now '+priceupdate+'$');


    e.onchange = function() {


     miles=parseFloat(result.routes[0].legs[0].distance.text);
     select_ride = e.options[e.selectedIndex].value;
     price = parseFloat(select_ride );
     elementi = document.getElementById("test");
     priceupdate=parseInt(price*miles);
     elementi.innerHTML = ' Trip Price '+priceupdate+'$'; 
     $('#id_price').val(priceupdate);
     $('#submitform').html('Book Now '+priceupdate+'$');


   }

            //Get distance and time
            const output = document.querySelector('#output');
            //output.innerHTML = "<div class=''>From: " + document.getElementById("from").value + ".<br />To: " + document.getElementById("to").value + ".<br /> Driving distance in miles <i class='fas fa-road'></i> : " + result.routes[0].legs[0].distance.text + ".<br />Duration <i class='fas fa-hourglass-start'></i> : " + result.routes[0].legs[0].duration.text + ".</div>";
           
           
           
            output.innerHTML = "<div class='trip-info container-fluid'>" + " Driving distance <i class='fas fa-road'></i> : "
              + result.routes[0].legs[0].distance.text+'les'
              + " Duration <i class='fas fa-hourglass-start'></i> : "
               + result.routes[0].legs[0].duration.text + "<div id='test'> Trip Price " + priceupdate + "$</div>" + " </div>";
              
            //display route
            directionsDisplay.setDirections(result);
        } else {
            //delete route from map
            directionsDisplay.setDirections({ routes: [] });
            //center map in London
            map.setCenter(myLatLng);

            //show error message
            output.innerHTML = "<div class='alert-danger'><i class='fas fa-exclamation-triangle'></i> Could not retrieve driving distance.</div>";
        }
    });

}


$('#resetform').on("click", function(){
  $('#form1').trigger("reset");
  $('#submitform').prop('type','');
  $('#submitform').html('Check Price');
  $('.trip-info').remove();

});








//create autocomplete objects for all inputs

var center = {lat: 41.881832, lng: -87.623177 };
// Create a bounding box with sides ~80km away from the center point
const defaultBounds = {
  north: center.lat + 1.8,
  south: center.lat - 1.8,
  east: center.lng + 1.8,
  west: center.lng - 1.8,
};
var options = {
  bounds: defaultBounds,
  componentRestrictions: { country: "us" },
  strictBounds: true,

};

var input1 = document.getElementById("from");
var autocomplete1 = new google.maps.places.Autocomplete(input1, options);

var input2 = document.getElementById("to");
var autocomplete2 = new google.maps.places.Autocomplete(input2, options);

//$(document).bind("contextmenu",function(e) {
  //e.preventDefault();
//});
$('#id_passanger_count').val('one');