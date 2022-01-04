#app that takes user location and prints out 3 nearby parking locations
from selenium import webdriver
from bs4 import BeautifulSoup
from googlesearch import search


#let the user enter their location via zipcode
user_location = input("Enter your zip code: ")

#this will be added onto the search link
query = "Parking+" + user_location

url = 'https://www.google.com/maps/search/' + query

#opening connection, grabbing the page
driver = webdriver.Firefox()
driver.get(url)

#html parsing using beautifulsoup
page_html = driver.page_source
soup = BeautifulSoup(page_html, "html.parser")

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
        address = "*****ERROR: Address not listed*****"
    elif len(address_container) > 1:
        address = address_container[1].text

    #update counter
    counter += 1
    
    #printing 
    print("\n")
    print("Place: " + name)
    print("Address: " + address)


    