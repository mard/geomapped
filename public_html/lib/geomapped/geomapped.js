var layers = [];

var path_photo = 'example/pics/'
var path_thumb = 'example/pics/thumb/'

function putPhotos()
{
  return $.getJSON(photoData[0].files).then(function(data){ return data; });
}

putPhotos().done(function (items)
{
  var list = "";
  var coords = [];
  var lastcoords = [];
  
  $.each(items, function()
  {
    if ($.isEmptyObject(lastcoords))
    {
        lastcoords = [this.geometry.coordinates[1], this.geometry.coordinates[0]];
    }
    //var thumbname = this.properties.name.slice(0, -4) + '-thumb' + this.properties.name.slice(-4);
    var thumbname = this.properties.name + '-thumb';
    //var thumbname = this.properties.name;
    list = '<li><img id="'+this.properties.name+'" src= "' + path_thumb + thumbname+'.jpg" alt ="'+this.properties.name+'"><\/li>';
    $('#photoslist-' + this.properties.date.substring(0, 10)).append(list);
  });

    //coords.push([lastcoords, [this.geometry.coordinates[1], this.geometry.coordinates[0]]]);
    //lastcoords = [this.geometry.coordinates[1], this.geometry.coordinates[0]];

  $.each(items, function()
  {
    var date = this.properties.date.substring(0, 10);
    if (date)
    {
    createLayerIfNotExists(date)
    layers[date].addLayer(
      L.geoJson(this,
      {
        onEachFeature: onEachFeature,
        pointToLayer: function (feature, latlng)
        {
          return L.marker(latlng,
          {
              icon: L.icon({iconUrl: 'lib/geomapped/dot-black.png', iconSize: [16, 16], iconAnchor: [8, 8],}),
              riseOnHover: true,
              title: feature.properties.name,
          });
        },
      }
    ));
    }
  });
  //.addTo(map);
  //var polyline = L.multiPolyline(coords, {weight: 2, color: '#f00'}).addTo(map);

  L.control.layers(buildOverlaysFromLayers(), null, {collapsed: false}).addTo(map);
});


function onEachFeature(feature, layer) {
  if (feature.properties && feature.properties.name)
  {
      var popupContent =
          '<a target="_blank" href="' + path_photo + feature.properties.name + '.jpg"><img src="' + path_photo + feature.properties.name + '.jpg" style="width: 300px"><\/a><br>' +
           '<p style="padding: 0.5em; font-size: 1.2em; font-weight: bold; text-shadow: 1px 1px #000; color: white;">Day ' + feature.properties.date.substring(9, 10)
            + '<span style="display: block; float: right">' + feature.properties.date.substring(0, 10) + ', ' + feature.properties.date.substring(11, 19) + '<\/span><\/p>';

      layer.bindPopup(popupContent);
      layer.draggable = true;

      var thumb = $("#" + feature.properties.name);

      layer.on("click",function(){
          $('html, body').animate({ scrollTop: thumb.offset().top - ($('body').height() / 2) + (thumb.height() / 2) }, 500);
      });

      if (document.getElementById(feature.properties.name))
      {
        document.getElementById(feature.properties.name).onclick = function() {
          layer.openPopup(); map.setView(layer.getLatLng());
          $('html, body').animate({ scrollTop: thumb.offset().top - ($('body').height() / 2) + (thumb.height() / 2) }, 500);
        }
      }
  }
}

function buildOverlaysFromLayers()
{
  // refactor this amateur shit
  var sortableList = [ ]
  for (var i in layers)
  {
    var item = { }
    item.key = i
    item.val = layers[i]
    sortableList.push(item)
  }
  sortableList.sort(function (a, b) { return a.key.localeCompare( b.key ); } );

  var overlayMaps = { }
  for (var i in sortableList)
  {
    overlayMaps[sortableList[i].key] = sortableList[i].val
  }
  return overlayMaps
}

var markeroptions = {
  startIconUrl: 'ext/leaflet-gpx/pin-start.png',
  endIconUrl: 'ext/leaflet-gpx/pin-end.png',
  shadowUrl: 'ext/leaflet-gpx/pin-shadow.png'
};

var gpxoptions = {async: true, marker_options: markeroptions, polyline_options: {weight: 3, opacity: 0.8}};

function putTracks()
{
  for (var tD in trackData)
    for (var d in trackData[tD].dates)
      for (var f in trackData[tD].files)
      {
        var trackLayer = new L.GPX(trackData[tD].files[f], gpxoptions);
        createLayerIfNotExists(trackData[tD].dates[d])
        if (tD == 0 && d == 0 && f == 0)
        {
          trackLayer.on('loaded', function(e) {map.fitBounds(e.target.getBounds(), { reset: true })})
          layers[trackData[tD].dates[0]].addTo(map)
        }
        layers[trackData[tD].dates[d]].addLayer(trackLayer)
      }
}

putTracks();
putPhotos();

var currentlist = '2015-07-11';

map.on('baselayerchange', function(e)
{
  $( "#photoslist-" + currentlist).addClass( "hidden");
  $( "#photoslist-" + e.name).removeClass( "hidden" );
  currentlist = e.name;
  $("html, body").animate({ scrollTop: "0" });

  var gpx_layer = e.layer.getLayers()[0].getLayers()[0];
  if (gpx_layer.getBounds)
  {
    map.fitBounds(gpx_layer.getBounds(), { pan: { duration: 1 } });
  }
}
);

function createLayerIfNotExists(layerName)
{
  if (!layers[layerName])
  {
    layers[layerName] = L.layerGroup();
  }
}
