'''
Created on 24/08/2019

@author: Gera e Ian
'''
from flask_restful import Resource, abort
from ston import parser
from ston.gsRetail import services as s


class gsRetail(Resource):

    def __init__(self):
        self.valid_post = []
        self.valid_get = ["getCategories", "getProducts"]

    def get(self, option):
        valid_option = self.valid_get
        if option not in valid_option:
            abort(404, message="Endpoint not found")
        data = self.get_and_post(option)
        if not data or not bool(data):
            abort(404, message="No data available for this endpoint")
        return data

    def get_and_post(self, option, arg_location="args"):
        option_parser = parser.copy()
        response = None
        option_parser.add_argument('page',
                                   required=False,
                                   location=arg_location,
                                   type=int)
        option_parser.add_argument('outputType',
                                   required=False,
                                   location=arg_location)
        option_parser.add_argument('idField',
                                   required=False,
                                   location=arg_location)
        option_parser.add_argument('byField',
                                   required=False,
                                   location=arg_location)
        option_parser.add_argument('byField2',
                                   required=False,
                                   location=arg_location)
        option_parser.add_argument('byField3',
                                   required=False,
                                   location=arg_location)
        args = option_parser.parse_args()
        page = args['page']
        output_type = args['outputType']
        by_field = args['byField']
        by_field2 = args['byField2']
        by_field3 = args['byField3']
        field_value = None
        field_value2 = None
        field_value3 = None
        if by_field:
            option_parser.add_argument('fieldValue',
                                       required=True,
                                       location=arg_location)
            args = option_parser.parse_args()
            field_value = args['fieldValue']
        if by_field2:
            option_parser.add_argument('fieldValue2',
                                       required=True,
                                       location=arg_location)
            args = option_parser.parse_args()
            field_value2 = args['fieldValue2']
        if by_field3:
            option_parser.add_argument('fieldValue3',
                                       required=True,
                                       location=arg_location)
            args = option_parser.parse_args()
            field_value3 = args['fieldValue3']
        by_field = [by_field, by_field2, by_field3]
        field_value = [field_value, field_value2, field_value3]
        id_field = args['idField'] if args['idField'] else "id"
        if option == "getProducts":
            option_parser.add_argument('productId',
                                       required=False,
                                       location=arg_location)
            args = option_parser.parse_args()
            product_id = args['productId'] if 'productId' in args else None
            response = s.get_products(product_id, page, output_type, id_field, by_field, field_value)
        if bool(response):
            return response
        else:
            abort(404, message="No data available")