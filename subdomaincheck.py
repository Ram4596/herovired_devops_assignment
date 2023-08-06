import requests
import time

from prettytable import PrettyTable

# t = PrettyTable(['Subdomain', 'stattus'])

domain_names = ['en.wikipedia.org','ride.lyft.com','autonomous.lyft.in','mail.google.com','blogs.loc.gov','cooking.nytimes.com']

def domain_scanner(domain_names):

    t = PrettyTable(['Subdomain', 'status'])

    for subdomain in domain_names:
       
        url = f"http://{subdomain}"
         
        try:
           
            var1 = requests.get(url)

            if ( var1.status_code == 200):
                t.add_rows([[ subdomain, 'UP']])
                # print ( subdomain, " subdomain is UP")
            else:
                # print (" not found "  )
                t.add_rows([[ subdomain, 'Down']])
   
        except requests.ConnectionError:
            t.add_rows([[ subdomain, 'down']])
            # print ( " domain not found ")

    print (t)


while True:
    domain_scanner(domain_names)
    time.sleep(60)
    



