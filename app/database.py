import re
from app import db


# *******FETCH TABLE FUNCTIONS**********
def fetch_answer_table():
    conn = db.connect()
    query_results = conn.execute("Select * from Answer").fetchall()
    conn.close()
    answer_list = []
    for i in query_results:
        item = {
            'answersID': i[0],
            'userID': i[1],
            'arrangementID': i[2],
            'party_Size': i[3],
            'budget' : i[4],
            'preferred_Flower' : i[5],
            'preferred_Color' : i[6],
            'preferred_Style' : i[7],
            'satisfaction': i[8]
        }
        answer_list.append(item)
    return answer_list

def fetch_user_table():
    conn = db.connect()
    query_results = conn.execute("Select * from User").fetchall()
    conn.close()
    user_list = []
    for i in query_results:
        item = {
            'id': i[0],
            'name': i[1],
            'email': i[2],
            'password': i[3],
        }
        user_list.append(item)
    return user_list

def fetch_wishlist_table():
    conn = db.connect()
    query_results = conn.execute("Select * from Wishlist").fetchall()
    conn.close()
    wishlist_list = []
    for i in query_results:
        item = {
            'wishlistID': i[0],
            'userID': i[1],
            'occasion': i[2],
            'arrangementID': i[3],
        }
        wishlist_list.append(item)
    return wishlist_list

def fetch_arrangement_table():
    conn = db.connect()
    query_results = conn.execute("Select * from Arrangement").fetchall()
    conn.close()
    arrangement_list = []
    for i in query_results:
        item = {
            'arrangementID': i[0],
            'flrName': i[1],
            'quantity': i[2],
            'price': i[3],
            'purpose': i[4],
            'description': i[5]
        }
        arrangement_list.append(item)
    # print(arrangement_list)
    return arrangement_list

def fetch_flower_table():
    conn = db.connect()
    query_results = conn.execute("Select * from Flower").fetchall()
    conn.close()
    flower_list = []
    for i in query_results:
        item = {
            'flowerID': i[0],
            'flowerName': i[1],
            'image': i[2],
            'color': i[3],
            'arrangementID1': i[4],
            'arrangementID2': i[5],
            'arrangementID3': i[6]
        }
        flower_list.append(item)

    return flower_list



# *******ANSWER FUNCTIONS**********
def update_userID_entry_answer(answers_id, user_id):
    conn = db.connect()
    query = 'Update Answer set userID = "{}" where answersID = {};'.format(user_id, answers_id)
    conn.execute(query)
    conn.close()
    
def update_arrangementID_entry_answer(answers_id, arrangement_id):
    conn = db.connect()
    query = 'Update Answer set arrangementID = "{}" where answersID = {};'.format(arrangment_id, answers_id)
    conn.execute(query)
    conn.close()

def update_partySize_entry_answer(answers_id, party_size):
    conn = db.connect()
    query = 'Update Answer set party_Size= "{}" where answersID = {};'.format(party_size, answers_id)
    conn.execute(query)
    conn.close()
    
def update_budget_entry_answer(answers_id, budget):
    conn = db.connect()
    query = 'Update Answer set budget = "{}" where answersID = {};'.format(budget, answers_id)
    conn.execute(query)
    conn.close()
    
def update_preferredFlower_entry_answer(answers_id, preferredFlower):
    conn = db.connect()
    query = 'Update Answer set preferred_Flower = "{}" where answersID = {};'.format(preferredFlower, answers_id)
    conn.execute(query)
    conn.close()
    
def update_preferredColor_entry_answer(answers_id, preferredColor):
    conn = db.connect()
    query = 'Update Answer set preferred_Color = "{}" where answersID = {};'.format(preferredColor, answers_id)
    conn.execute(query)
    conn.close()

def update_preferredStyle_entry_answer(answers_id, preferredStyle):
    conn = db.connect() 
    query = 'Update Answer set preferred_Style = "{}" where answersID = {};'.format(preferredStyle, answers_id)
    conn.execute(query)
    conn.close()
    
def update_satisfaction_entry_answer(answers_id, satisfaction):
    conn = db.connect() 
    query = 'Update Answer set satisfaction = "{}" where answersID = {};'.format(satisfaction, answers_id)
    conn.execute(query)
    conn.close()
    
def insert_new_answer(userID, arrangementID, party_Size, budget, preferred_Flower, preferred_Color, preferred_Style, satisfaction):
    conn = db.connect()
    results = conn.execute('Select MAX(answersID)+1 From Answer')
    results = [x for x in results]
    max_id = results[0][0]
    query = 'Insert Into Answer (answersID, userID, arrangementID, party_Size, budget, preferred_Flower, preferred_Color, preferred_Style, satisfaction) VALUES ({}, "{}", "{}", "{}", {}, "{}", "{}", "{}", "{}");'.format(max_id, userID, arrangementID, party_Size, budget, preferred_Flower, preferred_Color, preferred_Style, satisfaction)
    conn.execute(query)
    conn.close()
    
def remove_id_answer(answer_id):
    conn = db.connect()
    query = "Delete From User where answerID={};".format(answer_id)
    conn.execute(query)
    conn.close()


# *******WISHLIST FUNCTIONS**********


def update_userID_entry_wishlist(wishlistID, userID):
    conn = db.connect() 
    query = 'Update Wishlist set userID = "{}" where wishlistID = {};'.format(userID, wishlistID)
    conn.execute(query)
    conn.close()

def update_occasion_entry_wishlist(wishlistID, occasion):
    conn = db.connect() 
    query = 'Update Wishlist set occasion = "{}" where wishlistID = {};'.format(occasion, wishlistID)
    conn.execute(query)
    conn.close()

def update_arrangementID_entry_wishlist(wishlistID, arrangementID):
    conn = db.connect() 
    query = 'Update Wishlist set arrangementID = "{}" where wishlistID = {};'.format(arrangementID, wishlistID)
    conn.execute(query)
    conn.close()
    
def insert_new_wishlist(userID, occasion, arrangementID):
    conn = db.connect()
    results = conn.execute('Select MAX(wishlistID)+1 From Wishlist')
    results = [x for x in results]
    max_id = results[0][0]
    query = 'Insert Into Wishlist (wishlistID, userID, occasion, arrangementID) VALUES ({}, "{}", "{}", "{}");'.format(max_id, userID, occasion, arrangementID)
    conn.execute(query)
    conn.close()
    
def remove_id_wishlist(wishlistID):
    conn = db.connect()
    query = "Delete From Wishlist where wishlistID={};".format(wishlistID)
    conn.execute(query)
    conn.close()
    
# *******ARRANGEMENT FUNCTIONS**********

def update_flrName_entry_arrangement(arrangementID, flrName):
    conn = db.connect() 
    query = 'Update Arrangement set flrName = "{}" where arrangementID = {};'.format(flrName, arrangementID)
    conn.execute(query)
    conn.close()
    
def update_quantity_entry_arrangement(arrangementID, quantity):
    conn = db.connect() 
    query = 'Update Arrangement set quantity = "{}" where arrangementID = {};'.format(quantity, arrangementID)
    conn.execute(query)
    conn.close()

def update_price_entry_arrangement(arrangementID, price):
    conn = db.connect() 
    query = 'Update Arrangement set price = "{}" where arrangementID = {};'.format(price, arrangementID)
    conn.execute(query)
    conn.close()
    
def update_purpose_entry_arrangement(arrangementID, purpose):
    conn = db.connect() 
    query = 'Update Arrangement set purpose = "{}" where arrangementID = {};'.format(purpose, arrangementID)
    conn.execute(query)
    conn.close()

def update_description_entry_arrangement(arrangementID, description):
    conn = db.connect() 
    query = 'Update Arrangement set description = "{}" where arrangementID = {};'.format(description, arrangementID)
    conn.execute(query)
    conn.close()
    
def insert_new_arrangement(flrName, quantity, price, purpose, description):
    conn = db.connect()
    results = conn.execute('Select MAX(arrangementID)+1 From Arrangement')
    results = [x for x in results]
    max_id = results[0][0]
    query = 'Insert Into Wishlist (arrangementID, flrName, quantity, price, purpose, description) VALUES ({}, "{}", "{}", "{}", "{}", "{}");'.format(max_id, flrName, quantity, price, purpose, description)
    conn.execute(query)
    conn.close()
    

def remove_id_arrangement(arrangementID):
    conn = db.connect()
    query = "Delete From Arrangement where arrangementID={};".format(arrangementID)
    conn.execute(query)
    conn.close() 
    
# *******FLOWER FUNCTIONS**********

def update_flowerName_entry_flower(flowerID, flowerName):
    conn = db.connect() 
    query = 'Update Flower set flowerName = "{}" where flowerID = {};'.format(flowerName, flowerID)
    conn.execute(query)
    conn.close()

def update_image_entry_flower(flowerID, image):
    conn = db.connect() 
    query = 'Update Flower set image = "{}" where flowerID = {};'.format(image, flowerID)
    conn.execute(query)
    conn.close()

def update_color_entry_flower(flowerID, color):
    conn = db.connect() 
    query = 'Update Flower set color = "{}" where flowerID = {};'.format(color, flowerID)
    conn.execute(query)
    conn.close()
    
def update_arrangementID1_entry_flower(flowerID, arrangementID1):
    conn = db.connect() 
    query = 'Update Flower set arrangementID1 = "{}" where flowerID = {};'.format(arrangementID1, flowerID)
    conn.execute(query)
    conn.close()
    
def update_arrangementID2_entry_flower(flowerID, arrangementID2):
    conn = db.connect() 
    query = 'Update Flower set arrangementID2 = "{}" where flowerID = {};'.format(arrangementID2, flowerID)
    conn.execute(query)
    conn.close()

def update_arrangementID3_entry_flower(flowerID, arrangementID3):
    conn = db.connect() 
    query = 'Update Flower set arrangementID3 = "{}" where flowerID = {};'.format(arrangementID3, flowerID)
    conn.execute(query)
    conn.close()
    
def insert_new_flower(flowerName, image, color, arrangementID1, arrangementID2, arrangementID3):
    conn = db.connect()
    results = conn.execute('Select MAX(flowerID)+1 From Flower')
    results = [x for x in results]
    max_id = results[0][0]
    query = 'Insert Into Flower (flowerID, flowerName, image, color, arrangementID1, arrangementID2, arrangementID3) VALUES ({}, "{}", "{}", "{}", "{}", "{}");'.format(max_id, flowerName, image, color, arrangementID1, arrangementID2, arrangementID3)
    conn.execute(query)
    conn.close()
    
def remove_id_flower(flowerID):
    conn = db.connect()
    query = "Delete From Arrangement where flowerID={};".format(flowerID)
    conn.execute(query)
    conn.close() 

# *******USER FUNCTIONS**********
def update_username_entry_user(user_id, username):
    conn = db.connect()
    query = 'Update User set name = "{}" where userID = {};'.format(username, user_id)
    conn.execute(query)
    conn.close()


def update_email_entry_user(user_id, email):
    conn = db.connect()
    query = 'Update User set email = "{}" where userID = {};'.format(email, user_id)
    conn.execute(query)
    conn.close()


def update_password_entry_user(user_id, password):
    conn = db.connect()
    query = 'Update User set password = "{}" where userID = {};'.format(password, user_id)
    conn.execute(query)
    conn.close()


def insert_new_user_user(username, email, password):
    conn = db.connect()
    results = conn.execute('Select MAX(userID)+1 From User')
    results = [x for x in results]
    max_id = results[0][0]
    query = 'Insert Into User (userID, name, email, password) VALUES ({}, "{}", "{}", "{}");'.format(max_id,username,email,password)
    conn.execute(query)
    conn.close()
    
    return max_id

def remove_id_user(user_id):
    conn = db.connect()
    query = "Delete From User where userID={};".format(user_id)
    conn.execute(query)
    conn.close()

#******SEARCH FUNCTIONS******

def search_answer(search_text):
    conn = db.connect()
    if search_text == '':
        query_results = conn.execute("Select * from Answer").fetchall()
    else:
        search_text = "%" + search_text + "%"
        query_results = conn.execute("SELECT * FROM Answer where userID LIKE %s OR arrangementID LIKE %s OR party_Size LIKE %s OR budget LIKE %s OR preferred_Flower LIKE %s OR preferred_Color LIKE %s OR preferred_Style LIKE %s OR satisfaction LIKE %s", (search_text, search_text, search_text, search_text, search_text, search_text, search_text, search_text)).fetchall()
    conn.close()
    answer_list = []
    for i in query_results:
        item = {
            'answersID': i[0],
            'userID': i[1],
            'arrangementID': i[2],
            'party_Size': i[3],
            'budget' : i[4],
            'preferred_Flower' : i[5],
            'preferred_Color' : i[6],
            'preferred_Style' : i[7],
            'satisfaction': i[8]
        }
        answer_list.append(item)
    return answer_list

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
    #print(user_list)
    return user_list

def search_wishlist(search_text):
    conn = db.connect()
    if search_text == '':
        query_results = conn.execute("Select * from Wishlist").fetchall()
    else:
        search_text = "%" + search_text + "%"
        query_results = conn.execute("SELECT * FROM Wishlist where userID LIKE %s OR occasion LIKE %s OR arrangementID LIKE %s", (search_text, search_text, search_text)).fetchall()
    conn.close()
    wishlist_list = []
    for i in query_results:
        item = {
            'wishlistID': i[0],
            'userID': i[1],
            'occasion': i[2],
            'arrangementID': i[3],
        }
        wishlist_list.append(item)
    return wishlist_list

def search_arrangement(search_text):
    conn = db.connect()
    if search_text == '':
        query_results = conn.execute("Select * from Arrangement").fetchall()
    else:
        search_text = "%" + search_text + "%"
        query_results = conn.execute("SELECT * FROM Arrangement where flrName LIKE %s OR quantity LIKE %s OR price LIKE %s OR purpose LIKE %s OR description LIKE %s", (search_text, search_text, search_text, search_text)).fetchall()
    conn.close()
    wishlist_list = []
    for i in query_results:
        item = {
            'arrangementID': i[0],
            'flrName': i[1],
            'quantity': i[2],
            'price': i[3],
            'purpose': i[4],
            'description': i[5]
        }
        wishlist_list.append(item)
    return wishlist_list

def search_flower(search_text):
    conn = db.connect()
    if search_text == '':
        query_results = conn.execute("Select * from Flower").fetchall()
    else:
        search_text = "%" + search_text + "%"
        query_results = conn.execute("SELECT * FROM Flower where flowerName LIKE %s OR image LIKE %s OR color LIKE %s OR arrangementID1 LIKE %s OR arrangementID2 LIKE %s OR arrangementID3 LIKE %s OR arrangementID3 LIKE %s", (search_text, search_text, search_text, search_text, search_text, search_text, search_text)).fetchall()
    conn.close()
    flower_list = []
    for i in query_results:
        item = {
            'flowerID': i[0],
            'flowerName': i[1],
            'image': i[2],
            'color': i[3],
            'arrangementID1': i[4],
            'arrangementID2': i[5],
            'arrangementID3': i[6]
        }
        flower_list.append(item)
    # family_list = []
    # for rows in flower_list:
    #     splitup = rows["flowerName"].split()
    #     flag = 1
    #     for i in splitup:
    #         if "→" in i:
    #             flag = 0
    #             family_list.append(i.split("→")[2])
    #     if flag == 1:
    #         family_list.append(splitup[0])

    # family_list = set(family_list)
    # print(len(family_list))
    return flower_list




    ##############RECOMMENDATIONS##################

# def recommendations(flower, style, color, party_size, budget):
    



def advQueryOne():
    conn = db.connect()
    query_results = conn.execute("SELECT name, budget from Answer a join User u on u.userID = a.userID WHERE budget < 70 and preferred_Flower = %s UNION select name, budget from Answer g join User k on g.userID = k.userID WHERE budget > 150 and preferred_Flower = %s", ("Roses", "Roses")).fetchall()
    conn.close()
    answer_list = []
    for i in query_results:
        item = {
            'name': i[0],
            'budget': i[1],
        }
        answer_list.append(item)
    return answer_list

def advQueryTwo():
    conn = db.connect()
    query_results = conn.execute("SELECT name, budget from Answer a join User u on u.userID = a.userID WHERE budget > 200 and preferred_Flower = %s UNION select name, budget from Answer g join User k on g.userID = k.userID WHERE budget > 200 and preferred_Flower = %s", ("Roses", "Irises")).fetchall()
    
    conn.close()
    query_two_list = []
    for i in query_results:
        item = {
            'name': i[0],
            'budget': i[1],
        }
        query_two_list.append(item)
    # print("query_results")
    return query_two_list

def loginCheck(username, password):
    conn = db.connect()
    query_results = conn.execute("SELECT * FROM User where (email like %s) AND password LIKE %s", (username, password)).fetchall()
    
    conn.close()
    users = []
    if(not len(query_results)):
        return False
    for i in query_results:
        item = {
            'id': i[0],
            'name': i[1],
            'email': i[2],
            'password': i[3]
        }
        users.append(item)

    if len(users) >= 1:
        return True
    else:
        return False
