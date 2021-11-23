from flask import Flask, render_template, request, jsonify
from app import app
from app import database as db_helper

items = []
user_items = db_helper.search_user('')
answer_items = db_helper.search_answer('')
arrangement_items = db_helper.search_arrangement('')
flower_items = db_helper.search_flower('')
wishlist_items = db_helper.search_wishlist('')
recent_search = ''
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
    print(data)
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
            arrangement_items = db_helper.search_user(recent_search)
        else:
            arrangement_items = db_helper.search_user(data['search'])
            recent_search = data['search']
        # print(items)
    return render_template("arrangement.html", items=arrangement_items)

@app.route("/flower", methods=['POST', 'GET'])
def flower_name():
    global flower_items
    global recent_search
    if request.method == 'POST':
        data = request.get_json()
        # print(data["search"])
        if data == None or 'search' not in data:
            flower_items = db_helper.search_user(recent_search)
        else:
            flower_items = db_helper.search_user(data['search'])
            recent_search = data['search']
        # print(items)
    return render_template("flower.html", items=flower_items)

@app.route('/wishlist')
def wishlist():
    return render_template('wishlist.html')

@app.route('/flower')
def flower():
    return render_template('flower.html')

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

@app.route("/query1", methods=['GET'])
def queryone():
    items = advQueryOne()
    return render_template("query1.html", items = items)

@app.route("/query2", methods=['GET'])
def querytwo():
    data = request.get_json()
    items = db_helper.advQueryTwo()
    return render_template("query2.html", items=items)