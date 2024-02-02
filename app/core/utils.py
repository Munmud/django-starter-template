import os
import csv
import datetime
from django.conf import settings

CATEGORY_METADATA_CSV = os.path.join(settings.DATA_DIR, "categories_metadata.csv" )
PRODUCT_METADATA_CSV = os.path.join(settings.DATA_DIR, "products_metadata.csv" )
BOOK_METADATA_CSV = os.path.join(settings.DATA_DIR, "books_metadata.csv" )

def load_book_data():
    with open(BOOK_METADATA_CSV, newline = '', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        dataset = []
        for i, row in enumerate(reader):
            id = row.get("id")
            try: id = int(id)
            except: id = None
            
            title = row.get("title")
            author = row.get("author")
            genre = row.get("genre")
            price = row.get('price')
            try: price = float(price)
            except: price = None

            data = {
                'id' : id,
                'title' : title,
                'author' : author,
                'genre' : genre,
                'price' : price,
            }
            dataset.append(data)
        return dataset

# def load_category_data():
#     with open(CATEGORY_METADATA_CSV, newline = '', encoding="utf8") as csvfile:
#         reader = csv.DictReader(csvfile)
#         dataset = []
#         for i, row in enumerate(reader):
#             category_id = row.get("category_id")
#             try: category_id = int(category_id)
#             except: category_id = None
#             category_name = row.get("category_name")
#             data = {
#                 'category_id' : category_id,
#                 'category_name' : category_name
#             }
#             dataset.append(data)
#         return dataset

# def load_product_data():
#     with open(PRODUCT_METADATA_CSV, newline = '', encoding="utf8") as csvfile:
#         reader = csv.DictReader(csvfile)
#         dataset = []
#         for i, row in enumerate(reader):
#             name = row.get("name")
#             cost = row.get("cost")
#             try : cost = float(cost)
#             except: cost = 0
#             description = row.get("description")
#             category_name_id = row.get("category_name_id")

#             try : category_name_id = int(category_name_id)
#             except: category_name_id = None
#             data = {
#                 'name' : name,
#                 'cost' : cost,
#                 'description' : description,
#                 'category_name_id' : category_name_id,
#             }
#             dataset.append(data)
#         return dataset
