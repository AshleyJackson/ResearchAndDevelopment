import shodan


def searchShodan(api,pagenum):
    api.search('SHODAN QUERY HERE', page=pagenum) # Modify the query here


api = shodan.Shodan('SHODAN API KEY HERE') # Modify the API KEY here

searchShodan(api,1)
