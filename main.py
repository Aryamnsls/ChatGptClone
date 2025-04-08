from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import openai
import os

# Load environment variables from .env
load_dotenv()

# Load OpenAI API key from env
openai.api_key = os.getenv("OPENAI_API_KEY")  # also put this in your .env file

app = Flask(__name__)

# MongoDB URI from .env
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)

@app.route("/")
def home():
    chats = mongo.db.chats.find({})
    myChats = [chat for chat in chats]
    print(myChats)
    return render_template("index.html", myChats=myChats)

@app.route("/api", methods=["GET", "POST"])
def qa():
    if request.method == "POST":
        print(request.json)
        question = request.json.get("question")
        chat = mongo.db.chats.find_one({"question": question})
        print(chat)
        if chat:
            data = {"question": question, "answer": f"{chat['answer']}"}
            return jsonify(data)
        else:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=question,
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            print(response)
            answer = response["choices"][0]["text"].strip()
            data = {"question": question, "answer": answer}
            mongo.db.chats.insert_one({"question": question, "answer": answer})
            return jsonify(data)

    # Default response for GET
    data = {"result": "Hello! I'm your AI assistant. Ask me anything."}
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
