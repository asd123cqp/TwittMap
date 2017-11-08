// init vars
var map, markers, markerCluster, kw, rad, center;
var listener = null, circle = null;
var zoomScale = {0: 3, 100: 7, 500: 5, 1000: 4};

// init the map object
function initMap() {
  kw = 'all', rad = 0, center = { lat: 39.8097343, lng: -98.5556199 };
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 3,
    center: center,
  });

  markers = [];
  markerCluster = new MarkerClusterer(map, markers, {imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'});

  renderMap();
}

// retrive tweets and render markers/marker cluster
function renderMap() {
  clearMarkers();
  var query = 'search/?kw=' + kw;
  if (circle !== null) {
    query += '&rad=' + rad + '&loc=' + center.lat + ',' + center.lng;
  }
  fetch(query)
    .then(function (res) {
      return res.json();
    })
    .then(function (data) {
      createMarkers(data);
      document.getElementById('resultNum').textContent = data.length;
    })
    .catch(function (error) {
      console.log(error);
  });
}

// clear all markers on the map
function clearMarkers() {
  markers.forEach(function(m) {
    m.setMap(null);
  });
  // for (var i = 0; i < markers.length; i++) {
  //   markers[i].setMap(null);
  // }
  markers = [];
  markerCluster.clearMarkers();
}


// given an array of tweets, create markers and marker cluster
function createMarkers(tweets) {

  // map tweets -> markers
  markers = tweets.map(function(t) { return placeMarker(t) });

  // add a marker clusterer to manage the markers.
  markerCluster.addMarkers(markers);
}

// create a marker object
function placeMarker(tweet) {
  var position = {lat: tweet.location.lat, lng: tweet.location.lon};

  var marker = new google.maps.Marker({
    position: position,
    map: map,
  });

  var content =
    '<b>' + tweet.user_name + '</b>' +
    ' ( ' + '<i>' + '@' + tweet.screen_name + '</i>' + ' ):<br>' +
    '<hr>' + tweet.text + '<br>' + '<hr>' +
    '<font size="0.5em" color="grey">' + tweet.date + '</font>';

  var infowindow = new google.maps.InfoWindow({ maxWidth: 200 });
  google.maps.event.addListener(marker, 'click', (
    function(marker, content, infowindow) {
      return function() {
        infowindow.setContent(content);
        infowindow.open(map, marker);
      };
    })(marker, content, infowindow)
  );

  return marker;
}

// change keyword
function changeKeyword(keyword) {
  kw = keyword;
  renderMap();
}

// clear circle object
function clearCircle() {
  if (circle !== null) {
    circle.setMap(null);
    circle = null;
  }
}

// change geospatial search radius
function changeRadius(radius) {
  rad = parseInt(radius);
  clearCircle();

  // reset listener
  if (listener !== null) {
    google.maps.event.removeListener(listener);
  }

  // reset circle
  if (rad !== 0) {
    listener = google.maps.event.addListener(map, 'click', handleClick);
    makeCircle();
  }

  renderMap();
}

// make a circle
function makeCircle() {
  circle = new google.maps.Circle({
    center: center,
    radius: rad * 1000,
    map: map,
    strokeColor: '#FF0000',
    strokeOpacity: 0.8,
    strokeWeight: 2,
    fillColor: '#FF0000',
    fillOpacity: 0.35,
  });
}

// handle click event when geospatial search is enable
function handleClick(event) {
  center.lat = event.latLng.lat();
  center.lng = event.latLng.lng();
  clearCircle();
  makeCircle();
  map.panTo(center);
  map.setZoom(zoomScale[rad]);
  renderMap();
}

// reset
function reset() {
  listener = null, circle = null;
  document.getElementById('kwDropdown').options.selectedIndex = 0;
  document.getElementById('radDropdown').options.selectedIndex = 0;
  initMap();
}
