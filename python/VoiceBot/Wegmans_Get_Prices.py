import http.client, urllib.request, urllib.parse, urllib.error, base64


def wegmanGetPrices(skuNumber, storeNumber):
    headers = {
        # Request headers
        'Subscription-Key': '035067fa9c564cb994e182b738b49e04',
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'stores': storeNumber,      # Change everything within ''s to the store number selected by user (taken from front-end)
    })

    try:
        conn = http.client.HTTPSConnection('api.wegmans.io')
        conn.request("GET", "/products/" + skuNumber + "/prices?api-version=2018-10-18&%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
        return data

    except Exception as e:
        print("[Error {0}] {1}".format(e.errno, e.strerror))


# wegmanGetPrices("404208", 1)      sample how to call
