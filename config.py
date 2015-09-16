## Config file for PyGmaps
## --------------
## It consists in two sections:
## 1st: Needed information to create the visualization
##       API_KEY: Get it from http://code.google.com/apis/console.
##       SENSOR: If user uses geolocalization, for default=false
##       FILENAME: filename to generate
## 2a: Optional information to customize the map
# --------------
## PyGmaps is a script for the automatic creation of web docs using Google Maps
## It generates an HTML file to store into a website or to analyze locally.
################################################################################

##### 1st part: Needed information ####

API_KEY = '' # Api key for Google Maps 3
SENSOR = 'false' # true or false
FILENAME = 'PyGmaps_test' # filename to generate


##### 2nd part: Optional information ####

COORD = '0, 0' # lat. and lon. of initial center
TITLE = 'PyGmaps webpage' # webpage title
ZOOM = '2' # initial zoom
HEIGHT_HTML = '100%' # percentage of screen usage
MARGIN = '0' # margins
PADDING = '0' # padding
