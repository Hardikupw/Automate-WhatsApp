from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from pymongo import MongoClient
from datetime import datetime

cluster = MongoClient("mongodb+srv://hardiksharma_upw12:Xyzzxy_12@cluster0.pg7hlyq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = cluster["Bakery"]
users = db["users"]
orders = db["orders"]

app = Flask(__name__)

@app.route("/", methods=["get", "post"])
def reply():
    text = request.form.get("Body")
    number = request.form.get("Form")
    number = number.replace("whatsapp:", " ")
    response = MessagingResponse()
    user = users.find_one({"number": number})
    if bool(user) == false:
        response.message("Hi thanks for contacting *Exam Praxis*. \nYou can choose from one of the options below:"
                         "\n\n*Type*\n\n 1 To *contact* us \n 2 To *order* snacks")
        users.insert_one({"number": number, "status": "main", "messages":[]})
    elif user["status"] == "main":
    users.update_one({"number": number}, {"$push": {"messages": {"text": text, "date": datetime.now()}}})


    return str(response)

if __name__ == "__main__":
    app.run()

