from app import db

def fetch_todo():
    conn = db.connect()
    query_results = conn.execute("Select * from User;").fetchall()
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