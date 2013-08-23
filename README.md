#chromecast-control
##Control a chromecast with python

We got chromecasts at [ltc](http://ltc.io) and I immediately wanted to use them to power our [dashing](http://shopify.github.io/dashing/) dashboards. It is the cheapest route and being that it is just a chrome browser, makes the most sense. 

This script will start, stop get info on a particular appid and a target chromecast (ip).

##REST

Turns out that interacting with the chromecast is just rest. 

You do REST operations on the appid url: `http://CHROMECAST_IP:8008/apps/APPID` 

You stop it by DELETING to the appid URL. You also start by POSTING to it. 


##More interesting 

There are other URLS that show up when you sniff traffic: 

* http://CHROMECAST_IP:8008/ssdp/device-desc.xml
* http://CHROMECAST_IP:8008/apps/ChromeCast
* http://CHROMECAST_IP:8008/apps/

And i am sure there is more. 


#Please help

There is a lot of work to do  (discovery, etc) that would make this useful. The chromecast is very powerful, but it is wrapped in an annoying interaction model (browser extension, etc). 


