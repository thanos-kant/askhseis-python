#askhsh7 python , ari8mos mhtrwou P15050
import urllib2
import json
#eisodos twn gewgrafikwn suntetagmenwn lat & lon
syn=raw_input("Dwse tis gewgrafikes suntetagmenes (lat/lon) : ")
syn=syn.split("/")
lat=syn[0]
lon=syn[1]
#syndesh me thn istoselida openweathermap kai diaxeirhsh tou json 
ud="http://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&appid=d6a48b3784fc499e163e0a4e74696531"
webUrl =urllib2.urlopen(ud)
data= webUrl.read()
theJSON=json.loads(data)
#logikes sun8hkes gia thn die3agwgh twn parakatw sumperasmatwn gia thn 8ermokrasia kai thn periptwsh broxoptwshs!!
if theJSON["main"]["temp"] < 278.15 :
     print "brrrrrrr"
elif theJSON["main"]["temp"]> 293.15 :
    print "nice...."
else:
    print "eeem h thermokrasia den einai tetoia wste na ginei kati !!!"

if theJSON["weather"][0]["main"]== "Rain":
    print "I'm singing in the rain!"
else :
    print "Sadly I'm not singing in the rain!"


   


