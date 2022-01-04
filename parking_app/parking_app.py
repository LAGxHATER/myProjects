#app that takes user location and prints out 3 nearby parking locations
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import re

switch = True
#let the user enter their location via zipcode
while switch:
    user_location = input("Enter your zip code: ")
    #validating zip code with regex
    match = re.search('^\d{5}(-\d{4})?$', user_location)

    if match:
        switch = False
    else:
        print("ERROR: Zip Code Invalid")
        switch = True

#this will be added onto the search link
query = "Parking+" + user_location

url = 'https://www.google.com/maps/search/' + query

#headless makes browser invisible
options = Options()
options.headless = True
#opening connection, grabbing the page with selenium
driver = webdriver.Firefox(options=options)
driver.get(url)

#html parsing using beautifulsoup
page_html = driver.page_source
soup = BeautifulSoup(page_html, "html.parser")

#close all browser windows
driver.quit()

#grabs all parking 
parking = soup.findAll("div", {"class":"MVVflb-haAclf V0h1Ob-haAclf-d6wfac MVVflb-haAclf-uxVfW-hSRGPd"})

#this is a count for loop
counter = 0
for container in parking:

    #stop loop after 3 iterations
    if counter == 3:
        break

    #retrieves title
    name_container = container.findAll("span", {"jstcache":"77"})
    name = name_container[0].text

    #retrieves address
    address_container = container.findAll("span", {"jstcache":"104"})
    #the address is stored as the second value in the array, meaning if the array len is == 1, no address is available
    if len(address_container) == 1:
        address = "*****ERROR: Address not available*****"
    elif len(address_container) > 1:
        address = address_container[1].text

    #update counter
    counter += 1

    #printing 
    print("\n")
    print("Place: " + name)
    print("Address: " + address)

    