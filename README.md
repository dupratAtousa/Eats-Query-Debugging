# Eats-Query-Debugging
<LI> Download precompiled binaries of yab from Releases</LI>
<LI>Download jq</LI>
<LI>Download the eatsquery.py</LI>
<LI>Install JSON VIEWER and make sure the “Allow access to file URLs option” is ticked</LI>
<P>For a list of cmdline options, run:
$ python eatsquery.py --help</P> 

You can query dim_city table with the city name to get all the info including city_id 
For example SF: 1 , and Toronto: 13 

Example query:
<CODE>$ eatsQuery.py --lat=37.77493 --long=-122.41942 --cityID=1 --starttime=1582722000 --endtime=1582729200 --query="tapas" --limit=10</CODE>
<P>This query will run with the same x-uber-uuid, it means the user profile is the same.</P>
The delivery window is between start and end time and it is epoch time. 
