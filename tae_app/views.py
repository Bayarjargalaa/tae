
import pandas as pd
import os
from django.http import HttpResponse
from django.shortcuts import render
from .connect_db import connect_to_database
from .models import Product

def consql(request):
    conn=connect_to_database()
    cursor=conn.cursor()
    cursor.execute("select * from OpenDataItem")
    result=cursor.fetchall()
    return render(request, 'index.html', {'connect_to_database': result} )
def items_view(request):
    # Get all items from the database (or whatever logic you need)
    data = pd.read_excel('static/files/name.xlsx') # Фолдерын замыг тодорхойлох 
    items = data
    # print(items.head())
    
    
    # Render the template to display items
    return render(request, 'items.html', {'items': items})

def items_view_image(request):
    # Read the image URLs from the text file
    image_urls = []
    try:
        with open('output/image_urls.txt', 'r') as file:
            image_urls = file.readlines()  # Read lines into a list
            image_urls = [url.strip() for url in image_urls]  # Remove extra spaces/newlines
    except FileNotFoundError:
        print("File not found!")
    
    # Pass the list of image URLs to the template
    return render(request, 'image.html', {'image_urls': image_urls})

# def tail(request):
#     # Read the image URLs from the text file
    
    
#     # Pass the list of image URLs to the template
#     return render(request, 'tail.html', )

def import_excel_to_db(request): 
    # Excel файлын замыг тодорхойлох 
    data = pd.read_excel('static/files/name.xlsx') # Фолдерын замыг тодорхойлох 
    items = data.to_dict(orient='records')
    return render(request, 'contact.html', context={'items': items})

