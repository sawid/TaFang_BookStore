from re import search
from flask import Blueprint , render_template , request
import pandas as pd
from name import Name

route = Blueprint('route', __name__)
def get_blueprint():
    """Return the blueprint for the main app module"""
    return route

def bubbleSort(arr):
    n = len(arr)
 
    for i in range(n):
 
        for j in range(0, n-i-1):
 
            if arr[j][6] > arr[j+1][6] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

def linear_search(word, lst):
    temp_lst = []
    for o in lst :
        if word in o[0]:
            temp_lst.append(o)

    return temp_lst

def linear_search_list(word, lst):
    temp_lst = []
    for i in word:
        for o in lst :
            print(i)
            print(o[7])
            print("------")
            if int(i) == int(o[7]):
                temp_lst.append(o)

    return temp_lst
           


@route.route('/')
def home():
    df = pd.read_csv("DBbookstoreEng.csv",encoding="unicode_escape",usecols=["title","author","category" ,"link" ,"description","prize","sold","bookid"])
    new_df = [] 
    for i in range(0,df.shape[0]) :
        new = list((df.loc[i]))
        new_df.append(new)
    bubbleSort(new_df)
    global book_list
    book_list = new_df
    return  render_template('home.html',data = new_df)

@route.route('/search/<word_search>')
def search_page(word_search):
    res_lst = linear_search(word_search, book_list)
    global search_key
    search_key = word_search
    return  render_template('search_page.html',result = res_lst ,key_word = word_search,username_data = user)

@route.route('/book_detail/<book_id>')
def book_detail(book_id):
    temp_data = []
    print(book_list)
    for i in book_list:
        print(i[7])
        if str(book_id) == str(i[7]):
                    print("Do")
                    temp_data = i
    print(temp_data)
    return  render_template('book_detail.html', data_book = temp_data, username_data = user, search_key = search_key)

@route.route('/payment')
def payment():
    res_lst = linear_search_list(cart_list, book_list)
    print(res_lst)
    sum_cost = 0
    for elem in res_lst:
                sum_cost += elem[5]
    return  render_template('payment.html', user_id = user, list_book = res_lst, total_cost = sum_cost)

@route.route('/addName',methods=['POST'])
def addName():
    username = request.form.get('username','')
    password = request.form.get('password','')
    newName = Name(name=username, password=password)
    result = newName.insert()
    temp = ""
    if result == "Succcess":
            temp = "Can login"
            global user
            global cart_list
            cart_list = []
            user = username
    elif result == "Failed":
            temp = "Cannot Login"
    elif result == "Regist Success":
            temp = "Regist Success"
    print("Success")
    return (temp,200)

@route.route('/paysuccess')
def paysuccess():
    return render_template('pay_success.html')


@route.route('/addCart',methods=['POST'])
def addCart():
    book_id = request.form.get('book_id','')
    cart_list.append(book_id)
    print(cart_list)
    return ("Success",200)

@route.route('/removeCart',methods=['POST'])
def removeCart():
    while cart_list != []:
        cart_list.pop()
    print(cart_list)
    return ("Success",200)