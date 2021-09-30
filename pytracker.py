#!/usr/bin/env python

import phonenumbers, folium, sys
from phonenumbers import geocoder, timezone, carrier
from opencage.geocoder import OpenCageGeocode


def options():
	print("""\n /$$$$$$$              /$$                                  /$$                          
| $$__  $$            | $$                                 | $$                          
| $$  \ $$ /$$   /$$ /$$$$$$    /$$$$$$  /$$$$$$   /$$$$$$$| $$   /$$  /$$$$$$   /$$$$$$ 
| $$$$$$$/| $$  | $$|_  $$_/   /$$__  $$|____  $$ /$$_____/| $$  /$$/ /$$__  $$ /$$__  $$
| $$____/ | $$  | $$  | $$    | $$  \__/ /$$$$$$$| $$      | $$$$$$/ | $$$$$$$$| $$  \__/
| $$      | $$  | $$  | $$ /$$| $$      /$$__  $$| $$      | $$_  $$ | $$_____/| $$      
| $$      |  $$$$$$$  |  $$$$/| $$     |  $$$$$$$|  $$$$$$$| $$ \  $$|  $$$$$$$| $$      
|__/       \____  $$   \___/  |__/      \_______/ \_______/|__/  \__/ \_______/|__/      
	   /$$  | $$                                                                     
	  |  $$$$$$/                                                                     
	   \______/\n\nkkovacs-github\n\nhttps://github.com/kkovacs-github/pytracker""")
	print("\nOptions:\n1. Internet Protocol Address\n2. Phone Number\n3. Exit\n")


def ip_geolocation(ip, map_name):
	map_name = (map_name + ".html")
	import geocoder
	geocoded_ip = geocoder.ip(ip)
	geocoded_address = geocoded_ip.latlng
	print("\n" + str(geocoded_address))
	geocoded_map = folium.Map(location = geocoded_address, zoom_start = 10)
	folium.CircleMarker(location = geocoded_address, radius = 10, popup = "Location").add_to(geocoded_map)
	folium.Marker(geocoded_address, popup = "Location").add_to(geocoded_map)
	geocoded_map.save(map_name)


def phone_number_geolocation(phone_number, country_code, map_name):
	map_name = (map_name + ".html")
	parsed_number = phonenumbers.parse(phone_number)
	region = geocoder.description_for_number(parsed_number, country_code)
	print(region)
	geocoder_key = OpenCageGeocode(key)
	results = geocoder_key.geocode(region)
	#print(results)
	latitude = results[0]['geometry']['lat']
	longitude = results[0]['geometry']['lng']
	print(latitude, longitude)
	geocoded_map = folium.Map(location = [latitude, longitude], zoom_start = 10)
	folium.CircleMarker(location = [latitude, longitude], radius = 10, popup = "Location").add_to(geocoded_map)
	folium.Marker(location = [latitude, longitude], popup = "Location").add_to(geocoded_map)
	geocoded_map.save(map_name)


while True:
	options()
	option = input("--> ")

	if option == "1":	
		ip = input("IP:\n")
		map_name = input("\nMap Name:\n")
		ip_geolocation(ip, map_name)

	elif option == "2":
		phone_number = input("Phone Number:\n")
		map_name = input("\nMap Name:\n")
		country_code = input("\nCountry Code:\n")
		key = input("\nAPI Key:\n")

		if key == "200":
			key = ''

		elif key != "200":
			key = key

		phone_number_geolocation(phone_number, country_code, map_name)

	elif option == "3":
		sys.exit()

	else:
		print('Invalid option.')
