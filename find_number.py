
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

num = '+22898678984'

country = phonenumbers.parse(num, "CH")
service_provider = phonenumbers.parse(num, 'RO')

print("country: " + geocoder.description_for_number(country, ("fr")))
print("service: " + carrier.name_for_number(service_provider, "fr"))
