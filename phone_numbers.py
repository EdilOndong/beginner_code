import phonenumbers
from phonenumbers import geocoder, carrier


def get_information_about_number(phone_numbers):
    number = phonenumbers.parse(phone_numbers, "en")
    phone_location = geocoder.description_for_number(number, "en")
    phone_carrier = carrier.name_for_number(number, "en")
    print("The Location Of This Phone Number is " + str(phone_location) + " " + "And The Phone Carrier is " + phone_carrier)


if __name__ == '__main__':
    numbers = input("Please Enter The Target Number : ")
    get_information_about_number(numbers)