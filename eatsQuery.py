# Run a term query against UberEats
# External dependencies: 
# yab https://code.uberinternal.com/w/rpc/yab
# jq  https://stedolan.github.io/jq/

import os, sys, getopt, tempfile, time

helpstr = 'eatsQuery.py --peer=localhost:1234 --lat=37.77493 --long=-122.41942 --cityID=1 --query="pizza" --limit=10'
browser = "Google Chrome.app"

def main(argv):
   peer = "--peer-list /etc/uber/hyperbahn/hosts.json"
   latitude = 37.77493
   longitude = -122.41942
   cityID = 1
   query = "pizza"
   limit = 10

   try:
      opts, args = getopt.getopt(argv,"ha:o:c:q:p:l:",["help","lat=","long=","cityID=","query=","peer=","limit="])
   except getopt.GetoptError:
      print("Cmdline parsing error:")
      print(helpstr)
      sys.exit(1)
   for opt, arg in opts:
      if opt in ('-h', '--help'):
         print("Usage:")
         print(helpstr)
         sys.exit(0)
      elif opt in ("-a", "--lat"):
         latitude = arg
      elif opt in ("-o", "--long"):
         longitude = arg
      elif opt in ("-c", "--cityID"):
         cityID = arg
      elif opt in ("-q", "--query"):
         query = arg
      elif opt in ("-p", "--peer"):
         peer = arg
      elif opt in ("-l", "--limit"):
         limit = arg

   #print 'Peer ', peer
   #print 'Lat ', latitude
   #print 'Long ', longitude
   #print 'City ', cityID
   #print 'Query ', query

   if latitude==0 or longitude==0 or cityID==0 or query=="":
      print("Missing arguments:")
      print(helpstr)
      sys.exit(2)


   host = "adhoc01-dca8"
   yabcmdline='yab  '+peer+'  --thrift /usr/share/uber-idl/code.uber.internal/everything/monostore/storeindex.thrift  --service storeindex  --method StoreIndexService::termSearchQuery  -r \'\\\'\'{"request": { "radiusKm": 16, "maxTotalETASec": 7200, "location": { "latitude": '+str(latitude)+', "longitude": '+str(longitude)+', "cityId": '+str(cityID)+'}, "userQuery": "'+str(query)+'","queryConfig":{"enableFeedResponse":true,"useRichTextMarkup":true,"includeAccessibilityText":false,"isMenuV2Enabled":true}},"offset": 0,"limit": '+str(limit)+'}\' --headers=\'{"x-uber-uuid":"61c6a40a-c2f3-4c3d-aaa3-1d6237582eac", "x-uber-client-name":eats, "x-uber-client-version":"1.145.10001", "x-uber-device":iphone}\'\\\'\'  --timeout=5000'

   #print("ssh "+host+" \'"+yabcmdline+"\'")

   # Show output in terminal
   #os.system("ssh "+host+" \'"+yabcmdline+"\'")

   # Show output in browser
   jsonoutput = os.popen("ssh "+host+" \'"+yabcmdline+"\'").read()
   fd, fname = tempfile.mkstemp()
   os.write(fd, jsonoutput)
   os.close(fd)
   os.system("open -a \'"+browser+"\' "+fname)
   time.sleep(1)
   os.unlink(fname)

if __name__ == "__main__":
   main(sys.argv[1:])

