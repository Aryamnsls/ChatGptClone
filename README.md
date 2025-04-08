# ChatGptClone
A ChatGPT Clone using GPT-4 Turbo is an AI-powered chatbot application that mimics ChatGPT's conversational abilities. It leverages OpenAI’s GPT-4 Turbo API for generating human-like responses, enabling real-time interaction. The clone includes features like chat history, user authentication, and responsive UI
Sure! Here's a **step-by-step guide** to build a **ChatGPT Clone** using 🐍 **Python**, ⚗️ **Flask**, 🌐 **OpenAI**, 🍃 **MongoDB**, and 🧱 **HTML** for the frontend — complete with some beautiful emojis to keep it fun and clear! 🚀

---

### 💡 Step-by-Step Procedure to Build a ChatGPT Clone

---

#### 1️⃣ **Setup Your Project Environment**
- 📁 Create a folder for your project  
- ⚙️ Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

---

#### 2️⃣ **Install Required Libraries**
```bash
pip install flask pymongo dnspython openai python-dotenv
```

---

#### 3️⃣ **Create Your Project Structure**
```
chatgpt_clone/
│
├── app.py                  🧠 Main Flask app
├── templates/
│   └── index.html          🖼️ Frontend HTML
├── static/
│   └── style.css           🎨 CSS Styling
├── .env                    🔐 Store API Keys
└── db.py                   🍃 MongoDB Functions
```

---

#### 4️⃣ **Configure .env File for Security** 🔐
```dotenv
OPENAI_API_KEY=your_openai_api_key
MONGO_URI=your_mongodb_connection_string
```

---

#### 5️⃣ **Connect to MongoDB (db.py)** 🍃
```python
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client.chatgpt_clone
chat_collection = db.chats
```

---

#### 6️⃣ **Create Flask App (app.py)** ⚗️
```python
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import openai
import os
from db import chat_collection

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json['message']

    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": user_input}]
    )

    reply = response['choices'][0]['message']['content']

    # Save to MongoDB
    chat_collection.insert_one({"user": user_input, "bot": reply})

    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
```

---

#### 7️⃣ **Design the HTML (templates/index.html)** 🧱
```html
<!DOCTYPE html>
<html>
<head>
    <title>💬 ChatGPT Clone</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <h1>🤖 ChatGPT Clone</h1>
    <div id="chat-box"></div>
    <input type="text" id="user-input" placeholder="Type your message..." />
    <button onclick="sendMessage()">🚀 Send</button>

    <script>
        async function sendMessage() {
            const input = document.getElementById("user-input").value;
            const res = await fetch('/ask', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({message: input})
            });
            const data = await res.json();
            const chatBox = document.getElementById("chat-box");
            chatBox.innerHTML += `<p>🧑‍💻 You: ${input}</p>`;
            chatBox.innerHTML += `<p>🤖 Bot: ${data.reply}</p>`;
        }
    </script>
</body>
</html>
```

---

#### 8️⃣ **Add Styling (static/style.css)** 🎨
```css
body {
    font-family: 'Segoe UI', sans-serif;
    background-color: #f4f4f9;
    text-align: center;
    padding: 2em;
}

#chat-box {
    border: 1px solid #ccc;
    padding: 1em;
    margin: 1em auto;
    width: 60%;
    height: 300px;
    overflow-y: scroll;
    background-color: #fff;
    border-radius: 10px;
}

input {
    width: 40%;
    padding: 10px;
    margin-top: 10px;
    border-radius: 5px;
}

button {
    padding: 10px 20px;
    margin-left: 10px;
    border-radius: 5px;
    background-color: #007bff;
    color: white;
    cursor: pointer;
}
```

---

#### 9️⃣ **Run Your Application** 🏃‍♂️
```bash
python app.py
```

Visit: [http://localhost:5000](http://localhost:5000) 🌐

---

#### 🔟 **(Optional) Enhance Features**
✨ Add features like:
- Chat history display from MongoDB
- User authentication (Login/Signup)
- Multiple users
- Admin analytics dashboard 📊

---

### ✅ Done! You’ve built a mini ChatGPT clone!  
Let me know if you'd like to deploy it on **Render**, **Vercel**, or **Heroku** 🌍 or if you want to add advanced features!
