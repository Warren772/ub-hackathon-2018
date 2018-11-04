import http.client
import urllib.error
import urllib.parse
import urllib.error
import base64




def wegmanSearchProduct(searchTerm, resultCount, pageCount):
    headers = {
        # Request headers
        'Subscription-Key': 'f97af6ff47bb44128079a219cdff0a08',
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'results': resultCount,
        'page': pageCount,
    })

    try:
        conn = http.client.HTTPSConnection('api.wegmans.io')
        conn.request("GET", "/products/search?query={" + searchTerm + "}&api-version=2018-10-18&%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()

    except Exception as e:
        print("[Error {0}] {1}".format(e.errno, e.strerror))


wegmanSearchProduct("egg", 5, 1)     #sample how to call

