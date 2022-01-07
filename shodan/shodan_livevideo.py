from re import sub
from dotenv import load_dotenv
import shodan
import random
import os


class live_video:

    def ping_ip(ip):

        response = os.system("ping -c 1 " + ip)


        if response == 0:
            print(ip + " is online!")
            return True
            
        else:
            print(ip + " is offline!")
            return False


    load_dotenv()
    SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")
    api = shodan.Shodan(SHODAN_API_KEY)

    #User input port number and encode user input
    #search_query = input("Input port number: ")
    #search_query = urllib.parse.quote(search_query)

    #Create array to hold ip results
    ip_list = []

    #Shodan search with port number
    try: 
        results = api.search("hipcam+realserver")
        print("\nTotal results found: {}".format(results['total']))

        #stores ip results in array
        for result in results['matches']:
            ip_list.append(result['ip_str'])
            
    except shodan.APIError:
        print("Error")


    #Choose a random ip from ip results
    random_ip = random.choice(ip_list)

    print("\nTrying to connect to... " + random_ip + "\n")

    #Ping the ip, if it comes back false, pick a new ip
    while ping_ip(random_ip) == False:
        print("\nIP Offline! Generating new IP...\n")
        random_ip = random.choice(ip_list)
        
    

        



