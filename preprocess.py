import os
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

def prepare_data(csv_path):
  '''
  Parameters:
  -----------
    csv_path: path of csv to read
  Returns:
  --------
    X: outputted list of input
    y: outputted list of labels 
  '''
  X, y = [], []
  
  url_df = pd.read_csv(csv_path)
  
  for _, row in url_df.iterrows():
    title, news_source = from_url(row.iloc[0])

    # check for invalid urls / titles 
    if not title or news_source == 2:
      continue

    X.append(title)
    y.append(news_source)

  return X, y

def from_url(url):
  '''
    Given a URL, reads and normalizes the title of the associated article

    Parameters:
    -----------
      url: the link to read from

    Returns:
    -----------
      title: the normalized title of the article from the url
      news_source: returns according to what the newsource is; 0 - foxnews | 1 - nbcnews | 2- other
  '''

  # link pre-processing
  if ".print" in url:
    url = url.replace(".print", "")

  try:
    response = requests.get(url)
  except Exception as e:
    # print(e) # this is for debugging
    return "", 2
  if response.status_code != 200:
    return "", 2
  
  # checks which news source it comes from:
  news_source = 0 if "foxnews" in url else 1 #(1 if "nbcnews" in url else 2)

  hl_class = "headline speakable" if news_source == 0 else "article-hero-headline__htag"
  soup = BeautifulSoup(response.text, "html.parser")

  title = str(soup.find("h1", class_= hl_class)).lower()

  try:
    title = title.split(">")[1].split("<")[0] # trimming html tags off
  except:
    return "", 2
  
  # TODO: lemmatization, etc. (further normalization)
  return title, news_source

# title = from_url("https://www.foxnews.com/sports/juan-soto-sends-yankees-world-series-first-time-15-years")
# print(title)
X, y = prepare_data("url_subset.csv")

print(X)
print(y)