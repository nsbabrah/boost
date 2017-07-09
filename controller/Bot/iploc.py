import json
import urllib


def main():
     ip = raw_input("Enter the IP: ")
     url = "http://instagram.com/ip?ip=" + ip
     info = str(urllib.urlopen(url).read())
     data = json.loads(info)
     isValid = True
     if (data['status'] == 404):
         isValid = False
         print("Invalid IP!")
     else:
        display(data)

def display(data):
    print("\nResult\n------\n")
    print("IP: " + data['ip'])
    print("ISP: " + data['isp'])
    print("ORG: " + data['org'])
    print("Country: " + data['country'])
    print("City: " + data['city'])
    print("Region: " + data['region'])
    print("TimeZone: " + data['timezone'])
    print("ZipCode: " + data['zip'])
    print("Country Code: " + data['countryCode'])
    print("Latitude: " + data['latitude'])
    print("Longitude: " + data['longitude'])
    print("Currency Code: " + data['currencyCode'])
