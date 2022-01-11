from re import sub
from dotenv import load_dotenv
import shodan
import random
import os
import urllib

#getting api key and initializing in command line
load_dotenv()
SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")
api = shodan.Shodan(SHODAN_API_KEY)
os.system("shodan init " + SHODAN_API_KEY)

class live_video:

    def ping_ip(ip):

        print("\nAttemting to ping... " + ip + "\n")

        response = os.system("ping -c 1 " + ip)

        if response == 0:
            print("\n" + ip + " is online!")
            return True
            
        else:
            print("\n" + ip + " is offline!")
            return False

    def get_ip_information(ip):

        print("\nGrabbing IP Information...\n")

        response = os.system("shodan host " + ip)

        print(response)

    #User input port number and encode user input
    search_query = input("Input search: ")
    search_query = urllib.parse.quote(search_query)

    #Create array to hold ip results
    ip_list = []

    #Shodan search with port number
    try: 
        results = api.search(search_query)

        print("\nTotal results found: {}".format(results['total']))

        #stores ip results in array
        for result in results['matches']:
            ip_list.append(result['ip_str'])
            
    except shodan.APIError:
        print("Error")


    #Choose a random ip from ip results
    random_ip = random.choice(ip_list)

    #Ping the ip, if it comes back false, pick a new ip
    while ping_ip(random_ip) == False:
        print("\nIP Offline! Generating new IP...\n")
        random_ip = random.choice(ip_list)


    get_ip_information(random_ip)
        
    

        



