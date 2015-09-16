## PyGmaps is a python script for the automatic creation of web documents using Google Maps API v3
## Currently it only creates maps with a markers cloud (and tags) based in the attached config file.
## It requieres Python 2.7

## Import variables and libraries
from config import *
from Tkinter import *
import sys
import tkFileDialog

print '=================// PyGmaps 0.2 //================'
print '=================================================='

master = Tk()
master.withdraw()
file_path = tkFileDialog.askopenfilename(title="Open file", filetypes=[("txt file",".txt"),("All files",".*")])

if file_path != "":
   print "Using:", file_path
else:
    a = raw_input("You didn't open anything")
    sys.exit(0)

master.quit()

## First part of HTML file
output = file(FILENAME + '.html', 'w')

print >> output, '<!DOCTYPE html>'
print >> output, '<html>'
print >> output, '  <head>'
print >> output, '    <meta name="viewport" content="initial-scale=1.0, user-scalable=no" />'
print >> output, '    <title>' + TITLE + '</title>'
print >> output, '    <style type="text/css">'
print >> output, '      html { height: ' + HEIGHT_HTML + ' }'
print >> output, '      body { height: ' + HEIGHT_HTML + '; margin: ' + MARGIN + '; padding: ' + PADDING +' }'
print >> output, '      #map_canvas { height: 100% }'
print >> output, '    </style>'
print >> output, '    <script type="text/javascript"'
print >> output, '      src="http://maps.googleapis.com/maps/api/js?key=' + API_KEY + '&sensor=' + SENSOR + '">'
print >> output, '    </script>'
print >> output, '    <script type="text/javascript">'
print >> output, '      function initialize() {'
print >> output, '        var myOptions = {'
print >> output, '          center: new google.maps.LatLng(' + COORD + '),'
print >> output, '          zoom: ' + ZOOM + ','
print >> output, '          mapTypeId: google.maps.MapTypeId.ROADMAP'
print >> output, '        };'
print >> output, '        var map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);'
print >> output, '        var infowindow = new google.maps.InfoWindow();'

# Second part: coordinates from attached file.

data = file(file_path, 'r')
data2 = data.readlines()

for i in data2:
   lineas0 = i.split('\t')
   nom = lineas0[1].strip()
   lineas = lineas0[0].split(',')
   lat = lineas[0].strip()
   lon = lineas[1].strip()
   try:
      if float(lat) and float(lon):
         parte1 = "        var marker = new google.maps.Marker({ position: new google.maps.LatLng("
         parte3 = "), map: map,});"
         parte4 = "         google.maps.event.addListener(marker, 'click', function() {"
         parte5 = '            infowindow.setContent("' + nom + '");'
         parte6 = "            infowindow.open(map, this);});"
        
         print >> output, parte1 + str(lat) + ', ' + str(lon) + parte3
         print >> output, parte4
         print >> output, parte5
         print >> output, parte6
   except Exception, e:
      print str(e)
      continue

## Final part of HTML fuke
print >> output, '      }'
print >> output, '    </script>'
print >> output, '  </head>'
print >> output, '  <body onload="initialize()">'
print >> output, '    <div id="map_canvas" style="width:100%; height:100%"></div>'
print >> output, '  </body>'
print >> output, '</html>'

## Ending
output.close()
data.close()
a = raw_input('File completed. Press any key to exit')
