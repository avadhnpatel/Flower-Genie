from flask import Flask, render_template, request, jsonify
from app import app
from app import database as db_helper

items = db_helper.search_user('')
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
    global items
    global recent_search
    if request.method == 'POST':
        data = request.get_json()
        # print(data["search"])
        if data == None or 'search' not in data:
            items = db_helper.search_user(recent_search)
        else:
            items = db_helper.search_user(data['search'])
            recent_search = data['search']
        # print(items)
    return render_template("index.html", items=items)

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

