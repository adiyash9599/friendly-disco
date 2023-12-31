import google.generativeai as genai

genai.configure(api_key='AIzaSyBQ5GPxoE60butqTMOyZ5I47Fh63aY-3Ng')

model = genai.GenerativeModel('gemini-pro')

chat = model.start_chat()

while True:
    message = input("You: ")
    response = chat.send_message(message)

    print("Gemini: " + response.text)