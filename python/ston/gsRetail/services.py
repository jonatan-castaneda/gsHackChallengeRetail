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

def getCategories(level,category_one,category_two):
    text_search = request(conf.api_url+'catalog_system/pub/category/tree/3/',params=entities,method='GET')
    if level == '1':
        categories = [{'id':text_search['id'], 'name':text_search['name']} for text_search]
    if level == '2':
        for cat_one in text_search:
            if cat_one['id'] == category_one:
                categories = [{'id':cat_two['id'], 'name':cat_two['name']} for cat_two in cat_one['children']]
                break
