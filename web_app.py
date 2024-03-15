# -*- coding: utf-8 -*-
"""
@author: admin
"""

import openai
import urllib.request
from PIL import Image
import streamlit as st



from openai import OpenAI
client = OpenAI(api_key = "YOUR API KEY")

def generate_image(image_description):

  img_response = client.images.generate(
  model="dall-e-2",
  prompt= image_description,
  quality="standard",
  n=1,
)
  

  img_url = img_response.data[0].url

  urllib.request.urlretrieve(img_url, 'img.png')

  img = Image.open("img.png")
  
  return img



# page title
st.title('DALL.E - Image Generation - OpenAI')

# text input box for image recognition
img_description = st.text_input('Image Desription')

if st.button('Generate'):
    
    generated_img = generate_image(img_description)
    st.image(generated_img)
    
