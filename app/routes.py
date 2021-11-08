from flask import Flask, render_template, request, jsonify
from app import app
from app import database as db_helper

@app.route("/delete/<int:user_id>", methods=['POST'])
def delete(user_id):
    try:
        db_helper.remove_user_by_id(user_id)
        result = {"success": True, "response": "Removed Task"}
    except:
        result = {"success": False, "response": "Something went wrong"}
        
    return jsonify(result)


@app.route("/edit/<int:user_id>", methods=['POST'])
def update(user_id):
    data = request.get_json()
    try:
        if "username" in data:
            db_helper.update_username_entry(user_id, data["username"])
            result = {"success": True, "response": "Name Updated"}
        if "email" in data:
            db_helper.update_email_entry(user_id, data["email"])
            result = {"success": True, "response": "Email Updated"}
        if "password" in data:
            db_helper.update_password_entry(user_id, data["password"])
            result = {"success": True, "response": "Password Updated"}
        if "username" and "email" and "password" not in data:
            result = {"success": True, "response": "Nothing Updated"}
    except:
        result = {"success": False, "response": "Something went wrong"}
    return jsonify(result)

@app.route("/create", methods=['POST'])
def create():
    data = request.get_json()
    db_helper.insert_new_user(data['username'], data['email'], data['password'])
    result = {"success": True, "response": "Done"}
    return jsonify(result)

# @app.route("/search", methods=['POST'])
# def search():
#     data = request.get_json()
#     items = db_helper.search_user(data['search'])
#     result = {"success": True, "response": "Done"}
#     return jsonify(result)

@app.route("/", methods=['POST', 'GET'])
def homepage():
    if request.method == 'POST':
        data = request.get_json()
        items = db_helper.search_user(data['search'])
        return render_template("index.html", items=items)
    items = db_helper.fetch_todo()
    return render_template("index.html", items=items)