# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import datetime, timedelta
from http.client import HTTPException
import json
from typing import Union, Optional

from fastapi import FastAPI, Request
import uuid


from dataSeed import userList, userCity

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/sonzLearning/userDetails/")
def get_user():
        return userList

@app.get("/sonzLearning/getAccessToken/")
def get_access_token():
        accessToken = {
            "token": uuid.uuid4()
        }
        f = open("accessToken.json", "w")
        f.write(str(json.dumps(str(accessToken["token"]))))
        f.close()
        return {
            "accessToken": accessToken["token"]
        }

def validateAccessToken():
    f = open("accessToken.json", "r")
    data = json.load(f)
    return data

@app.get("/sonzLearning/userDetails/{user_id}")
def get_user(user_id: Optional[int] = None):
    if user_id is not None:
        for user in userList["userDetails"]:
            if user["id"] == user_id:
                return user
    else:
        return userList


@app.get("/sonzLearning/userCityHistory/")
def read_item(request: Request, user_city: str = None, ):
    headers = request.headers
    accessToken = headers.get('accessToken')
    if accessToken != validateAccessToken():
        return {
            "error": "provide valid access token in the headers with keyName accessToken."
        }
    else:
        if user_city is not None:
            matching_users = []
            for user in userCity["userDetails"]:
                for city in user["city"]:
                    if user_city in city:
                        matching_users.append(user)
            return matching_users
        else:
            return userCity


@app.put("/sonzLearning/update_user/{user_id}", response_model=dict | list)
def update_user(user_id: int, field_data: dict , request: Request):
    headers = request.headers
    update_method = headers.get('update_method')
    if update_method == "single":
        for user in userList["userDetails"]:
            if user["id"] == user_id:

                field = field_data.get("field")
                new_value = field_data.get("new_value")

                if not field or not new_value:
                    return {"field or new_value or both cannot be None"}

                # Check if the specified field exists in the user's data
                if field in user:
                    # Update the user's data field with the new value
                    user[field] = new_value
                    return {
                        "explanation": "You can see a single field has got updated based on the key name which is city, try passing header as multiple with the header name is update_method",
                        "userDetails": user
                    }
                else:
                    raise HTTPException(status_code=400, detail="Field  not found in user data")
        raise HTTPException(status_code=404, detail="User not found")
    elif update_method == "multiple":
        for user in userList["userDetails"]:
            if user["id"] == user_id:
                for update in field_data["updates"]:
                    field = update.get("field")
                    new_value = update.get("new_value")

                    if not field or not new_value:
                        raise HTTPException(status_code=422, detail="Missing required fields")

                    # Check if the specified field exists in the user's data
                    if field in user:
                        # Update the user's data field with the new value
                        user[field] = new_value
                    else:
                        raise HTTPException(status_code=400, detail=f"Field '{field}' not found in user data")

                return {
                    "explanation": "You can see multiple fields have got updated at the same time",
                     "userDetails": user
                }

        raise HTTPException(status_code=404, detail="User not found")
    else:
        return { "explanation": "incorrect header"}

@app.delete("/sonzLearning/delete_user/{user_id}", response_model=list)
def delete_user(user_id: int):
    deleted_user = None
    for index, user in enumerate(userList):
        if user["id"] == user_id:
            # Remove the user from the list and store the deleted user
            deleted_user = userList.pop(index)
            break  # Exit the loop once the user is found and deleted

    if deleted_user:
        # Return the updated user_data list with the deleted user removed
        return userList

    raise HTTPException(status_code=404, detail="User not found")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

