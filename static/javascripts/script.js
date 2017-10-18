function initMap() {
  var learner = {lat: 40.806833, lng: -73.9635};
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 10,
    center: learner
  });
  var marker = new google.maps.Marker({
    position: learner,
    map: map
  });
}
