from flask import Flask, render_template, request, jsonify, redirect, url_for
from app import app
from app import database as db_helper
import sys

items = []
user_items = db_helper.search_user('')
answer_items = db_helper.search_answer('')
arrangement_items = db_helper.search_arrangement('')
flower_items = db_helper.search_flower('')
wishlist_items = db_helper.search_wishlist('')
query1items = db_helper.advQueryOne()
query2items = db_helper.advQueryTwo()
wishlists = []
rec = []
uinfo = []
wishlists = []
recent_search = ''
page_status = "stay"
page_status2 = "stay"
page_status3 = "stay"
@app.route("/user/delete/<int:user_id>", methods=['POST'])
def delete_user(user_id):
    try:
        db_helper.remove_id_user(user_id)
        result = {"success": True, "response": "Removed Task"}
    except:
        result = {"success": False, "response": "Something went wrong"}
    user_page()
    return jsonify(result)


@app.route("/user/edit/<int:user_id>", methods=['POST'])
def update_user(user_id):
    data = request.get_json()
    try:
        if "username" in data:
            db_helper.update_username_entry_user(user_id, data["username"])
            result = {"success": True, "response": "Name Updated"}
        if "email" in data:
            db_helper.update_email_entry_user(user_id, data["email"])
            result = {"success": True, "response": "Email Updated"}
        if "password" in data:
            db_helper.update_password_entry_user(user_id, data["password"])
            result = {"success": True, "response": "Password Updated"}
        if "username" and "email" and "password" not in data:
            result = {"success": True, "response": "Nothing Updated"}
    except:
        result = {"success": False, "response": "Something went wrong"}
    user_page()
    return jsonify(result)

@app.route("/user/create", methods=['POST'])
def create_user():
    data = request.get_json()
    db_helper.insert_new_user_user(data['username'], data['email'], data['password'])
    result = {"success": True, "response": "Done"}
    user_page()
    return jsonify(result)

# @app.route("/search", methods=['POST'])
# def search():
#     data = request.get_json()
#     items = db_helper.search_user(data['search'])
#     result = {"success": True, "response": "Done"}
#     return jsonify(result)

@app.route("/user", methods=['POST', 'GET'])
def user_page():
    global user_items
    global recent_search
    if request.method == 'POST':
        data = request.get_json()
        # print(data["search"])
        if data == None or 'search' not in data:
            user_items = db_helper.search_user(recent_search)
        else:
            user_items = db_helper.search_user(data['search'])
            recent_search = data['search']
        # print(items)
    return render_template("index.html", items=user_items)

@app.route("/wishlist/delete/<int:wishlist_id>", methods=['POST'])
def delete_wishlist(wishlist_id):
    try:
        db_helper.remove_id_wishlist(wishlist_id)
        result = {"success": True, "response": "Removed Task"}
    except:
        result = {"success": False, "response": "Something went wrong"}
    wishlist_page()
    return jsonify(result)


@app.route("/wishlist/edit/<int:wishlist_id>", methods=['POST'])
def update_wishlist(wishlist_id):
    data = request.get_json()
    # print(data)
    try:
        if "userID" in data:
            db_helper.update_userID_entry_wishlist(wishlist_id, data["userID"])
            result = {"success": True, "response": "userID Updated"}
        if "occasion" in data:
            db_helper.update_occasion_entry_wishlist(wishlist_id, data["occasion"])
            result = {"success": True, "response": "occasion Updated"}
        if "arrangementID" in data:
            db_helper.update_arrangementID_entry_wishlist(wishlist_id, data["arrangementID"])
            result = {"success": True, "response": "arrangementID Updated"}
        if "userID" and "occasion" and "arrangementID" not in data:
            result = {"success": True, "response": "Nothing Updated"}
    except:
        result = {"success": False, "response": "Something went wrong"}
    wishlist_page()
    return jsonify(result)

@app.route("/wishlist/create", methods=['POST'])
def create_wishlist():
    data = request.get_json()
    db_helper.insert_new_wishlist(data['userID'], data['occasion'], data['arrangementID'])
    result = {"success": True, "response": "Done"}
    wishlist_page()
    return jsonify(result)

# @app.route("/search", methods=['POST'])
# def search():
#     data = request.get_json()
#     items = db_helper.search_user(data['search'])
#     result = {"success": True, "response": "Done"}
#     return jsonify(result)

@app.route("/wishlist", methods=['POST', 'GET'])
def wishlist_page():
    global wishlist_items
    global recent_search
    if request.method == 'POST':
        data = request.get_json()
        # print(data["search"])
        if data == None or 'search' not in data:
            wishlist_items = db_helper.search_wishlist(recent_search)
        else:
            wishlist_items = db_helper.search_wishlist(data['search'])
            recent_search = data['search']
        # print(items)
    return render_template("wishlist.html", items=wishlist_items)

@app.route("/answer", methods=['POST', 'GET'])
def answer_page():
    global answer_items
    global recent_search
    if request.method == 'POST':
        data = request.get_json()
        # print(data["search"])
        if data == None or 'search' not in data:
            answer_items = db_helper.search_answer(recent_search)
        else:
            answer_items = db_helper.search_answer(data['search'])
            recent_search = data['search']
        # print(items)
    return render_template("answer.html", items=answer_items)

@app.route("/arrangement", methods=['POST', 'GET'])
def arrangement_page():
    global arrangement_items
    global recent_search
    if request.method == 'POST':
        data = request.get_json()
        # print(data["search"])
        if data == None or 'search' not in data:
            arrangement_items = db_helper.search_arrangement(recent_search)
        else:
            arrangement_items = db_helper.search_arrangement(data['search'])
            recent_search = data['search']
        # print(items)
    return render_template("arrangement.html", items=arrangement_items)

@app.route("/flower", methods=['POST', 'GET'])
def flower_page():
    global flower_items
    global recent_search
    if request.method == 'POST':
        data = request.get_json()
        # print(data["search"])
        if data == None or 'search' not in data:
            flower_items = db_helper.search_flower(recent_search)
        else:
            flower_items = db_helper.search_flower(data['search'])
            recent_search = data['search']
    return render_template("flower.html", items=flower_items)

@app.route("/query1", methods=['GET'])
def queryone():
    global query1items
    global recent_search
    if request.method == 'POST':
        query1items = db_helper.advQueryOne()
        # print(items)
    return render_template("query1.html", items=query1items)
    
@app.route("/query2", methods=['GET'])
def querytwo():
    global query2items
    global recent_search
    if request.method == 'POST':
        query2items = db_helper.advQueryTwo()
        # print(items)
    return render_template("query2.html", items=query2items)

@app.route('/wishlist')
def wishlist():
    return render_template('wishlist.html')

# @app.route('/flower')
# def flower():
#     return render_template('flower.html')

@app.route('/arrangement')
def arrangement():
    return render_template('arrangement.html')

@app.route('/user')
def user():
    return render_template('index.html')

@app.route('/answer')
def answer():
    return render_template('answer.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/query1')
def query1():
    return render_template('query1.html')

@app.route('/query2')
def query2():
    return render_template('query2.html')

@app.route('/survey', methods=['POST','GET'])
def survey():
    print("reached")
    global page_status2
    if page_status2 == 'leave':
        page_status2 = 'stay'
        # print(rec)
        return redirect('/recommendation')
    print(uinfo)
    h = db_helper.getWishlists(uinfo[2])
    print(h)
    return render_template("survey.html", items=uinfo)

@app.route('/login', methods=['POST','GET'])
def login():
    global page_status
    if page_status == 'leave':
        page_status = 'stay'
        # print(uinfo)
        return redirect('/survey')
    return render_template("login.html")

@app.route("/")
def starting_url():
    return redirect("/intro")

@app.route("/login/create", methods=['POST', 'GET'])
def loginCreate():
    data = request.get_json()
    db_helper.insert_new_user_user(data['username'], data['email'], data['password'])
    result = {"success": True, "response": "Done"}
    return jsonify(result)

@app.route("/login/validate", methods=['POST', 'GET'])
def loginValidate():
    data = request.get_json()
    global uinfo
    y = db_helper.getuid(data['username'], data['password'])
    n = db_helper.getname(data['username'], data['password'])
    uinfo = [data['username'], data['password'], y, n]
    # print(y, n, uinfo)
    x = db_helper.loginCheck(data['username'], data['password'])
    global page_status
    if x:
        # print("test passed", x)
        page_status = 'leave'
    # else:
    #     print("test failed")
    result = {"success": True, "response": "Done"}
    return jsonify(result)

@app.route('/intro')
def intro():
    return render_template('intro.html')

@app.route("/survey/create", methods=['POST', 'GET'])
def create_answer():
    data = request.get_json()
    # print("hit")
    # print(data['preferred_Flower'], data['preferred_Flower1'], data['preferred_Flower2'], data['preferred_Flower3'], data['preferred_Style'], data['preferred_Color'], data['party_Size'], data['budget'])
    global page_status2
    page_status2 = 'leave'
    global rec
    rec = list(db_helper.recommendations(data['preferred_Flower'], data['preferred_Flower1'], data['preferred_Flower2'], data['preferred_Flower3'], data['preferred_Style'], data['preferred_Color'], data['party_Size'], data['budget']))  
    # print(rec)
    # db_helper.insert_new_answer(data['userID'], data['party_Size'], data['budget'], data['preferred_Flower'], data['preferred_Color'], data['preferred_Style'])
    result = {"success": True, "response": "Done"}
    return jsonify(result)

@app.route('/recommendation', methods=['POST','GET'])
def recommendation():
    # global page_status3
    # if page_status3 == 'leave':
    #     page_status3 = 'stay'
    #     # print(rec)
    #     return redirect('/userWishlist')
    # print("uhhhhhh", rec)
    # print("uh", uinfo)
    return render_template('recommendation.html', items=rec, userinfo = uinfo)

@app.route('/final')
def final():
    return render_template('final.html')


@app.route('/userWishlist')
def userWishlist():
    # wishlists = db_helper.getWishlists(999)
    for item in wishlists:
        # for x in item:
        print(item)
    return render_template('userWishlist.html', items = wishlists)
