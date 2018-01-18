import os
import urllib.request

def create_dir(path):
  if not os.path.isdir(path):
    print('Creating directory: %s' % path)
    os.makedirs(path)

def download_file(source, target):
  target = os.path.abspath(os.path.expanduser(target))
  create_dir(os.path.dirname(target))
  print('Downloading: %s' % source)
  remote = urllib.request.urlopen(source)
  with open(target,'wb') as output:
    output.write(remote.read())

## jqueery
download_file('https://code.jquery.com/jquery-3.0.0.min.js', './public_html/ext/jquery/jquery.min.js')

## leaflet
download_file('http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.js', './public_html/ext/leaflet/leaflet.js')
download_file('http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.css', './public_html/ext/leaflet/leaflet.css')
download_file('http://cdn.leafletjs.com/leaflet/v0.7.7/images/layers.png', './public_html/ext/leaflet/images/layers.png')
download_file('http://cdn.leafletjs.com/leaflet/v0.7.7/images/layers-2x.png', './public_html/ext/leaflet/images/layers-2x.png')
download_file('http://cdn.leafletjs.com/leaflet/v0.7.7/images/marker-icon.png', './public_html/ext/leaflet/images/marker-icon.png')
download_file('http://cdn.leafletjs.com/leaflet/v0.7.7/images/marker-icon-2x.png', './public_html/ext/leaflet/images/marker-icon-2x.png')
download_file('http://cdn.leafletjs.com/leaflet/v0.7.7/images/marker-shadow.png', './public_html/ext/leaflet/images/marker-shadow.png')

## leaflet-gpx
download_file('https://raw.githubusercontent.com/mpetazzoni/leaflet-gpx/master/gpx.js', './public_html/ext/leaflet-gpx/gpx.js')
# removed "icon" from filenames below because it conflicts with some AdBlock filters
download_file('https://raw.githubusercontent.com/mpetazzoni/leaflet-gpx/master/pin-icon-end.png', './public_html/ext/leaflet-gpx/pin-end.png')
download_file('https://raw.githubusercontent.com/mpetazzoni/leaflet-gpx/master/pin-icon-start.png', './public_html/ext/leaflet-gpx/pin-start.png')
download_file('https://raw.githubusercontent.com/mpetazzoni/leaflet-gpx/master/pin-shadow.png', './public_html/ext/leaflet-gpx/pin-shadow.png')

## leaflet multi options polyline
download_file('https://raw.githubusercontent.com/hgoebl/Leaflet.MultiOptionsPolyline/master/Leaflet.MultiOptionsPolyline.min.js', './public_html/ext/leaflet-multioptionspolyline/Leaflet.MultiOptionsPolyline.min.js');
