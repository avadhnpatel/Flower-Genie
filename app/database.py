from app import db

def fetch_todo():
    conn = db.connect()
    query_results = conn.execute("Select * from User").fetchall()
    conn.close()
    user_list = []
    for i in query_results:
        item = {
            'id': i[0],
            'name': i[1],
            'email': i[2],
            'password': i[3]
        }
        user_list.append(item)
    return user_list

def update_username_entry(user_id, username):
    conn = db.connect()
    query = 'Update User set name = "{}" where userID = {};'.format(username, user_id)
    conn.execute(query)
    conn.close()


def update_email_entry(user_id, email):
    conn = db.connect()
    query = 'Update User set email = "{}" where userID = {};'.format(email, user_id)
    conn.execute(query)
    conn.close()


def update_password_entry(user_id, password):
    conn = db.connect()
    query = 'Update User set password = "{}" where userID = {};'.format(password, user_id)
    conn.execute(query)
    conn.close()


def insert_new_user(username, email, password):
    conn = db.connect()
    results = conn.execute('Select MAX(userID)+1 From User')
    results = [x for x in results]
    max_id = results[0][0]
    query = 'Insert Into User (userID, name, email, password) VALUES ({}, "{}", "{}", "{}");'.format(max_id,username,email,password)
    conn.execute(query)
    conn.close()
    
    return max_id

def remove_user_by_id(user_id):
    conn = db.connect()
    query = "Delete From User where userID={};".format(user_id)
    conn.execute(query)
    conn.close()

def search_user(search_text):
    conn = db.connect()
    if search_text == '':
        query_results = conn.execute("Select * from User").fetchall()
    else:
        search_text = "%" + search_text + "%"
        query_results = conn.execute("SELECT * FROM User where name LIKE %s OR email LIKE %s OR password LIKE %s", (search_text, search_text, search_text)).fetchall()
    conn.close()
    user_list = []
    for i in query_results:
        item = {
            'id': i[0],
            'name': i[1],
            'email': i[2],
            'password': i[3]
        }
        user_list.append(item)
    print(user_list)
    return user_list
    
    