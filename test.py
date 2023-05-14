
# import MySQLdb.cursors
from flask import Flask, render_template, request, redirect, url_for, session
from flaskext.mysql import MySQL

import re
import os
import sys
import pymysql
# import MySQLdb.cursors

   


app = Flask(__name__)
app.secret_key = 'abcd2123445'  
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'lancaster123'
app.config['MYSQL_DB'] = 'db'

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'lancaster123'
app.config['MYSQL_DATABASE_DB'] = 'db'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
  
# app.config['MYSQL_CURSORCLASS'] = "DictCursor"
mysql = MySQL(app)

# conn = pymysql.connect(host="localhost", user="root", password="lancaster123", database="db", cursorclass=dict)
# print('conn: ', conn)
# cursor = conn.cursor()
# print('cursor:', cursor)
# dt = cursor.execute("SELECT * FROM user")
# print(dt)       


# cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
# cursor = mysql.connection.cursor()
conn = mysql.connect()
cursor = conn.cursor()


    
def get_header(cursor):
    header = []
    for row in cursor.description:
        header.append(row[0])
        
    return header

def make_dict(columns, list_o_tuples):
    anary = {}
    for j, column in enumerate(columns):
        place = []
        for row in list_o_tuples:
            place.append(row[j])
        anary[column] = place
    return anary

def make_dict1(columns, list_o_tuples):

    final_dict = []
    for row in list_o_tuples:
    # print(row)
        out_dict = {}
        # print({header[i] : data[i] for i, _ in enumerate(row)})
        for i, x in enumerate(row):
            out_dict[columns[i] ] = x
     
        final_dict.append(out_dict)  
    return final_dict
    
    {header[i] : data[i] for i, _ in enumerate(data)}
    
    for j, column in enumerate(columns):
        place = []
        for row in list_o_tuples:
            place.append(row[j])
        anary[column] = place
    return anary
    
cursor.execute('SELECT * FROM book')
        
        
data = cursor.fetchall()

# print(data)
header = get_header(cursor)

# print(header)
# resultDictionary = {header[0] : data[i] for i, _ in enumerate(data)}



resultDictionary = make_dict1(header, data)

print(resultDictionary)

# final_dict = []
# for row in data:
#     # print(row)
#     out_dict = {}
#     # print({header[i] : data[i] for i, _ in enumerate(row)})
#     for i, x in enumerate(row):
#         out_dict[header[i] ] = x
     
#     final_dict.append(out_dict)   
# print(final_dict)


# # {'bookid': [1, 2, 3, 7, 8, 9], 'categoryid': [2, 2, 2, 1, 1, 1], 'authorid': [2, 3, 2, 2, 2, 2], 'rackid': [2, 2, 1, 0, 0, 1], 'name': ['The Joy of PHP Programming', 'Head First PHP &amp; MySQL', 'dsgsdgsd', 'eeeeeebook', 'aaaaaaaaaaaaaa', 'bbbbbbbbbbbbbb'], 'picture': ['joy-php.jpg', 'header-first-php.jpg', '', '', '', ''], 'publisherid': [8, 9, 7, 2, 2, 2], 'isbn': ['B00BALXN70', '0596006306', 'sdfsd2334', 'hfdfhdfhd', 'bbbbbbbbbbbbbbbbbb', '4346436463463'], 'no_of_copy': [10, 10, 23, 2, 2, 2], 'status': ['Enable', 'Enable', 'Enable', '', '', 'Enable'], 'added_on': [datetime.datetime(2022, 6, 12, 11, 12, 48), datetime.datetime(2022, 6, 12, 11, 16, 1), datetime.datetime(2022, 6, 12, 13, 29, 14), datetime.datetime(2023, 3, 19, 16, 27, 17), datetime.datetime(2023, 3, 19, 17, 37, 56), datetime.datetime(2023, 3, 25, 14, 44, 18)], 'updated_on': [datetime.datetime(2022, 6, 12, 11, 13, 27), datetime.datetime(2022, 6, 12, 11, 16, 1), datetime.datetime(2022, 6, 12, 13, 29, 14), datetime.datetime(2023, 3, 19, 16, 27, 17), datetime.datetime(2023, 3, 19, 17, 37, 56), datetime.datetime(2023, 3, 25, 14, 44, 18)]}

# # {name:'', categoryid:''}