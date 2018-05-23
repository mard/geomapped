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
  opener = urllib.request.build_opener()
  opener.addheaders = [('User-agent', 'Mozilla/5.0')]
  with opener.open(source) as iinput:
    with open(target,'wb') as output:
      output.write(iinput.read())

## jqueery
download_file('https://code.jquery.com/jquery-3.3.1.min.js', './public_html/ext/jquery/jquery.min.js')

## leaflet
download_file('https://unpkg.com/leaflet@1.3.1/dist/leaflet.js', './public_html/ext/leaflet/leaflet.js')
download_file('https://unpkg.com/leaflet@1.3.1/dist/leaflet.css', './public_html/ext/leaflet/leaflet.css')
download_file('https://unpkg.com/leaflet@1.3.1/dist/images/layers.png', './public_html/ext/leaflet/images/layers.png')
download_file('https://unpkg.com/leaflet@1.3.1/dist/images/layers-2x.png', './public_html/ext/leaflet/images/layers-2x.png')
download_file('https://unpkg.com/leaflet@1.3.1/dist/images/marker-icon.png', './public_html/ext/leaflet/images/marker-icon.png')
download_file('https://unpkg.com/leaflet@1.3.1/dist/images/marker-icon-2x.png', './public_html/ext/leaflet/images/marker-icon-2x.png')
download_file('https://unpkg.com/leaflet@1.3.1/dist/images/marker-shadow.png', './public_html/ext/leaflet/images/marker-shadow.png')

## leaflet-gpx
download_file('https://raw.githubusercontent.com/mpetazzoni/leaflet-gpx/master/gpx.js', './public_html/ext/leaflet-gpx/gpx.js')
# removed "icon" from filenames below because it conflicts with some AdBlock filters
download_file('https://raw.githubusercontent.com/mpetazzoni/leaflet-gpx/master/pin-icon-end.png', './public_html/ext/leaflet-gpx/pin-end.png')
download_file('https://raw.githubusercontent.com/mpetazzoni/leaflet-gpx/master/pin-icon-start.png', './public_html/ext/leaflet-gpx/pin-start.png')
download_file('https://raw.githubusercontent.com/mpetazzoni/leaflet-gpx/master/pin-shadow.png', './public_html/ext/leaflet-gpx/pin-shadow.png')

## leaflet multi options polyline
download_file('https://raw.githubusercontent.com/hgoebl/Leaflet.MultiOptionsPolyline/master/Leaflet.MultiOptionsPolyline.min.js', './public_html/ext/leaflet-multioptionspolyline/Leaflet.MultiOptionsPolyline.min.js')
