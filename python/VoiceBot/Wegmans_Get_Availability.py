import http.client, urllib.request, urllib.parse, urllib.error, base64


def wegmanGetAvailability(skuNumber, storeNumber):
    headers = {
        # Request headers
        'Subscription-Key': '035067fa9c564cb994e182b738b49e04',
    }

    params = urllib.parse.urlencode({
    })

    try:
        conn = http.client.HTTPSConnection('api.wegmans.io')
        conn.request("GET", "/products/" + skuNumber + "/availabilities/" + storeNumber + "?api-version=2018-10-18&%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return data

    except Exception as e:
        print("[Error {0}] {1}".format(e.errno, e.strerror))


# wegmanGetAvailability("404208", "1")  sample how to call
