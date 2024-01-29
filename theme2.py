

import streamlit as st
from bs4 import BeautifulSoup
import requests 

st.title ("Shopify Theme Detector : Mudcy")

from urllib.parse import urlparse, urlunparse

def get_page_source(url):
    try:
        # Check if the URL contains a scheme
        parsed_url = urlparse(url)

        # If the scheme is empty, assume 'https://'
        if not parsed_url.scheme:
            url = 'https://' + url

        # Ensure 'www.' is present if not already
        if not url.startswith('https://www.') and not url.startswith('http://www.'):
            parts = url.split("://")
            url = parts[0] + "://www." + parts[1]

        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            # Return a message with the status code for debugging
            return f"Failed with status code: {response.status_code}"
    except requests.RequestException as e:
        # Return the exception message for debugging
        return f"Request exception: {e}"


# Function to Detect Shopify Theme :

import re

def extract_theme_name(page_source):
    match = re.search(r"window\.BOOMR\.themeName\s*=\s*['\"](.*?)['\"]", page_source)
    return match.group(1) if match else None



url= st.text_input("Please Enter the URL of the Shopify Page")
if st.button('Detect Theme'):
  # Theme Detection Logic
  page_source = get_page_source(url)
  if page_source:
      theme_name = extract_theme_name(page_source)
      if theme_name:
          st.success(f"The Shopify Theme is: {theme_name}")
      else:
          st.error("This Website is not using Shopify. Please enter the URL of a Shopify Website")
  else:
      st.error("Failed to fetch the page. Please check the URL.")


  
