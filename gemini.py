import google.generativeai as genai

genai.configure(api_key='AIzaSyBQ5GPxoE60butqTMOyZ5I47Fh63aY-3Ng')

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("What does aditya name means?")

print(response.text)