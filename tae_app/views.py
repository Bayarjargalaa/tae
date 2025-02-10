
import pandas as pd
import os
from django.http import HttpResponse
from django.shortcuts import render
from .connect_db import connect_to_database
from django.db import connection
from django.http import JsonResponse

def consql(request):
    conn=connect_to_database() # дата баз руу холбогдох
    cursor=conn.cursor()    # курсор үүсгэх
    cursor.execute("select * from OpenDataItem") # sql query ажиллуулах
    result=cursor.fetchall() # бүх мэдээллийг авах
    return render(request, 'index.html', {'connect_to_database': result} ) # index.html руу датагаа дамжуулах


def items_view(request):
    # Get all items from the database (or whatever logic you need)
    data = pd.read_excel('static/files/name.xlsx') # Фолдерын замыг тодорхойлох # Excel файлын замыг тодорхойлох
    items = data # Файлын мэдээллийг хадгалах
    # print(items.head())
    
    
    # Render the template to display items
    return render(request, 'items.html', {'items': items}) # items.html руу датагаа дамжуулах

def items_view_image(request):
    # Read the image URLs from the text file
    image_urls = []
    try:
        with open('output/image_urls.txt', 'r') as file:    # Open the file in read mode
            image_urls = file.readlines()  # Read lines into a list
            image_urls = [url.strip() for url in image_urls]  # Remove extra spaces/newlines
    except FileNotFoundError:
        print("File not found!")
    
    # Pass the list of image URLs to the template
    return render(request, 'image.html', {'image_urls': image_urls}) # image.html руу датагаа дамжуулах



def import_excel_to_db(request):  # Excel файлыг дата баз руу оруулах
    
    data = pd.read_excel('static/files/name.xlsx') # Excel файлыг унших
    items = data.to_dict(orient='records') # Excel файлыг dictionary болгож хадгалах
    return render(request, 'contact.html', context={'items': items}) # contact.html руу датагаа дамжуулах





def get_views(): # view-ийг авах
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT table_name, COUNT(column_name) 
            FROM information_schema.columns 
            WHERE table_name IN (SELECT table_name FROM information_schema.views)
            GROUP BY table_name
        """)
        views = cursor.fetchall()
    return views

def show_views(request): # view-ийг харуулах
    views = get_views() # view-ийг авах
    return render(request, 'views.html', {'views': views}) # views.html руу датагаа дамжуулах





