import google.generativeai as genai
import PIL.Image

img = PIL.Image.open('adi.jpg')

genai.configure(api_key='AIzaSyBQ5GPxoE60butqTMOyZ5I47Fh63aY-3Ng')

model = genai.GenerativeModel('gemini-pro-vision')

response = model.generate_content(["you know who is he?", img])

print(response.text)