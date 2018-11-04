import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Subscription-Key': '035067fa9c564cb994e182b738b49e04',
}


# This block prompts the user in Pycharm for the values they want
# We want the user to do this part on the front-end, and whatever they enter is stored in a variable/set of variables
# Those variable values are then sent into this python program and whatever is returned is sent to the front-end
# Where it will be displayed for the user to see
searchTerm = input("What would you like to search for?")
resultCount = input("How many results do you want returned?")
pageCount = input("How many pages of results do you want returned?")


params = urllib.parse.urlencode({
    # Request parameters
    'results': resultCount,
    'page': pageCount,
})

try:
    conn = http.client.HTTPSConnection('api.wegmans.io')
    conn.request("GET", "/products/search?query=" + searchTerm + "&api-version=2018-10-18&%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Error {0}] {1}".format(e.errno, e.strerror))

