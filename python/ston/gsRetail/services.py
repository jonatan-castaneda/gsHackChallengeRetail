'''
Created on 24/08/2019

@author: Gera e Ian
'''
from ston.gsRetail import config
import requests

def get_products(search, page=None, output_type="full",
                           id_field="id",
                           by_field=None,
                           field_value=None):
    try:
        url = config.api_url + "catalog_system/pub/products/search/" + str(search)
        r = requests.get(url)
        products = r.json()
        for p in products:
            p["name"] = p["productName"].replace('"', '')
            try:
                p["img"] = p["items"][0]["images"][0]["imageUrl"]
            except:
                p["img"] = ""
    except:
        pass    
    return {
        "products": products[0:10]
    }
