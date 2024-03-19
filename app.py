from flask import Flask, render_template, request 
import time
import os
from dotenv import load_dotenv
from IPython.display import Markdown
import textwrap

#Importing Google Generative AI
import google.generativeai as genai 


load_dotenv() 
genai.api_key = os.environ["GOOGLE_API_KEY"]
model = genai.GenerativeModel("gemini-pro")
app = Flask(__name__)

@app.route("/markdown")
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

@app.route("/")
def home():
    return render_template("index.html")

#Define Chatbot Route
@app.route("/chatbot", methods=["POST"])
def chatbot():
    
    #get message from user 
    user_input = request.form["message"]
    prompt = f"User: {user_input}\n ChatBot: "
    
    pmpt = "Act as a happy go lucky guy named ChatBud and give response to the question accordingly. The question: "
    
    final_ip = pmpt + user_input
    
    chat_history=[]
    
    response = model.generate_content(f"{final_ip}")
    
    for chunk in response:
     print(chunk.text)
   
    chat_history.append(f"User: {user_input}\nChatBot: {chunk.text}")
    
    return render_template(
        "bot.html",
        user_input=user_input,
        generated_text=chunk.text,
    )

    
if __name__=="__main__":
  app.run(debug=True)