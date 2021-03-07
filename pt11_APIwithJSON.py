from flask import Flask, jsonify
import random, json
#from flask.json.tag import JSONTag

class User():
  def __init__(self, username, theme, image):   
    self.username = username  
    self.theme = theme
    self.image =  image
  


# def to_jsons(the_list):
#   dictionary_concat = {}
#   for list_item in the_list:
#     dictionary_item = list_item
#     print(type(list_item))
#     if type(list_item) == User:
#       dictionary_item = list_item.__dict__
#       print("dictionary conversion")

#     #dictionary_concat = dict(dictionary_concat.items()+ dictionary_item.items())
#     #dictionary_concat = {key: value for (key, value) in (dictionary_concat.items() + dictionary_item.items())}
#     dictionary_concat = dictionary_concat.copy()
#     dictionary_concat.update(dictionary_item)
#     print(dictionary_concat)

userList = [
  User("clopez", "dark", "static/img1"),
  User("Alex", "dark", "static/img2"),
  User("jess", "light", "static/img3")]


def get_current_user():
  user_selected = random.randint(0,2)
  #list_length = len(userList)

  return userList[user_selected]

def get_all_users():
  #converts obj to dict?
  
  # dict_list = []
  # for user in userList:
  #   #alt? dict_user = vars(user)
  #   dict_user = user.__dict__
  #   dict_list.append(dict_user)

  # return dict_list
  return userList

app = Flask(__name__)

#in flask return a dict from a view, it will be converted to a JSON response.
#JSON is common response format when writing an API 
@app.route("/me")
def me_api():
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": user.image
        #"image": url_for("user_image", filename=user.image),
    }

#Depending on API design,  may want to create JSON responses for types other than dict. 
#Can use the jsonify() function, which will serialize any supported JSON data type
@app.route("/users")
def users_api():
    users = get_all_users()
    #return jsonify([user.to_json() for user in users])
    return jsonify([user.to_json() for user in users])


# "username": user.username,
# "theme": user.theme,
# "image": user.image

#                   username=g.user.username,
#                    email=g.user.email,
#                   id=g.user.id
    #return jsonify([JSONTag.to_json(user) for user in users])
    
    #return jsonify([json.dumps(user) for user in users]) 

    #tried doing a workaround
    # json_users = ([json.dumps(user) for user in users])  
    # str_json_users = str(json_users)
    # cleaned_up_str_json_users = str_json_users.replace("[", "")
    # cleaned_up_str_json_users2 = cleaned_up_str_json_users.replace("]", "")
    # cleaned_up_str_json_users3 = cleaned_up_str_json_users2.replace("'", "")
    # return cleaned_up_str_json_users3


if __name__ == '__main__':
   #app.run(debug = True)
  app.debug = True
  app.run(host='0.0.0.0',
  port=random.randint(2000, 9000))
