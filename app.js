const request = require('request');



function Data(){

  //storeRequest(zip) is the helper function to the getStores(zip) function. Allows a promise to be returned after the request is finished.
  this.storeRequest = function(zip){
    return new Promise(function(resolve, reject){
      request('https://sp1004f27d.guided.ss-omtrdc.net/?q=*&do=location-search&sp_q_location_1='+ zip +'&sp_x_1=zip&sp_q_max_1=5&sp_s=zip_proximity;sp_c=1000', function(error, response, body){
        resolve(body);
      });
    })
  }

  //Converts the requested body from the JSON obtained from Wegman's Query (Not Included in API, Custom Endpoint) and allows us to find stores in the vicinity of the requested Zip Code.
  this.getStores = function(zip, callback){
    this.storeRequest(zip).then(function(body){
      var data = JSON.parse(body);
      var stores = data['results'];
      this.stores = stores;
      callback(this.stores);
    });
  };

  //productRequest(sku) is the helper function to the getProducts(zip) function. Allows promise to be returned after the request is finished.
  productRequest = function(sku){
    return new Promise(function(resolve, reject){
      request("https://api.wegmans.io/products/" + sku + "?api-version=2018-10-18&Subscription-Key=3671d57aac6440d08421b7d1d31cfca5  ",{gzip: true}, function(error, response, body){
        resolve(body);
      });
    })
  }

  //Converts the requested body to JSON obtained from the Wegman's API of the product details.
  getProduct = function(sku,callback){
    productRequest(sku).then(function(body){
      var data = JSON.parse(body);
      if(!data.error){
       var image = data.tradeIdentifiers[0].images[0];
      callback(image);
    }
    });
  }

  //searchProductRequest(searchTerms) uses the Wegmans API to search for products based on the specified search terms.
  this.searchProductRequest = function(searchTerms){
    return new Promise(function(resolve, reject){
      request("https://api.wegmans.io/products/search?query=" + searchTerms + "&api-version=2018-10-18&5&1&Subscription-Key=3671d57aac6440d08421b7d1d31cfca5",{gzip: true}, function(error, response, body){
        resolve(body);
      });
    });
  }

  //Converts the requested body to JSON obtained from the Wegman's API to searching for products. Returns an array of 5 items from the searchTerms.
  this.getProducts = function(searchTerms, callback){
    this.searchProductRequest(searchTerms).then(function(body){
      var data = JSON.parse(body);
      var products = data.results;
      var possibleProds = [];
      products.some(function(element, index){
        if(index == 5){
          return true;
        }

        possibleProds.push(element);
      });
      this.possibleProducts = possibleProds;
      callback(this.possibleProducts);
    });
  }

  //searchProductRequest(searchTerms) uses the Wegmans API to search for products based on the specified search terms.
  this.priceRequest = function(sku, store){
    return new Promise(function(resolve, reject){
      request("https://api.wegmans.io/products/" + sku +"/prices/"+ store +"?api-version=2018-10-18&Subscription-Key=3671d57aac6440d08421b7d1d31cfca5",{gzip: true}, function(error, response, body){
        resolve(body);
      });
    });
  }

  //Converts the requested body to JSON obtained from the Wegman's API by searching for the price of the product based on the store.
  this.searchPrices = function(sku, store, callback){
    this.priceRequest(sku, store).then(function(body){
      var data = JSON.parse(body);
      callback(data);
    })
  }

  //searchProductRequest(searchTerms) uses the Wegmans API to see if the desired product is at the selected store.
  this.requestAvailability = function(sku, store){
    return new Promise(function(resolve, reject){
      request("https://api.wegmans.io/products/" + sku +"/availabilities/"+ store +"?api-version=2018-10-18&Subscription-Key=3671d57aac6440d08421b7d1d31cfca5",{gzip: true}, function(error, response, body){
        resolve(body);
      });
    });
  }

  //Converts the requested body to JSON obtained from the Wegman's API by searching for the availability of the product at the store.
  this.getAvailability = function(sku, store,callback){
    this.requestAvailability(sku, store).then(function(body){
      var data = JSON.parse(body);
      var availability = data['isAvailable'];
      callback(availability)
    });
  }

  //requestAllAvailabilities uses the Wegmans API to see all the stores that have the desired product (sku).
  this.requestAllAvailabilities = function(sku){
    return new Promise(function(resolve, reject){
      request("https://api.wegmans.io/products/" + sku +"/availabilities/?api-version=2018-10-18&Subscription-Key=3671d57aac6440d08421b7d1d31cfca5",{gzip: true}, function(error, response, body){
        resolve(body);
      });
    });
  }

  //Converts the requested body to JSON obtained from the Wegmans API by searching for all stores that have the desired product.
  this.getAllAvailabilities = function(sku){
    this.requestAllAvailabilities(sku).then(function(body){
      var data = JSON.parse(body);
      console.log(data);
    });
  }
}

//Utilizes TheMealDB API
function Meal(){

  this.requestSearch = function(name){
    return new Promise(function(resolve, reject){
      request("https://www.themealdb.com/api/json/v1/1/search.php?s=" + name ,{gzip: true}, function(error, response, body){
        resolve(body);
      });
    });
  }

  this.getSearch = function(name,callback){
    this.requestSearch(name).then(function(body){
      var data = JSON.parse(body);
      var meals = data['meals']
      if (meals === null){
        console.log('No Meals Found!');
      }
      else{
        var keyArray = Object.keys(meals[0]);
        var newArray = [];
        var counter = 1;
        keyArray.forEach(function(key){
          if(key.includes('strIngredient')){
            var measure = 'strMeasure' + counter;
            var ingredient = meals[0][key];
            var amount = meals[0][measure];
            var ingredientObject = {[ingredient]:amount};
            newArray.push(ingredientObject);
            counter = counter +1;
          }
        });
        callback(newArray);
      }

    })
  }

}
