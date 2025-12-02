import os
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

def prepare_data(csv_path):
  '''
  Parameters:
  -----------
    csv_path: 
  Returns:
  --------
    X: list of input
    y: list of labels 
  '''
  X, y = [], []
  
  urls = pd.read_csv(csv_path).to_numpy
  
  for row in urls():
    title, news_source = from_url(row)

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
  '''

  response = requests.get(url)
  if response.status_code != 200:
    return "", 2

  # checks which news source it comes from:
  # 0 - foxnews | 1 - nbcnews | 2- other
  news_source = 0 if "foxnews" in url else 1 if "nbcnews" in url else 2

  soup = BeautifulSoup(response.text, "html.parser")
  title = str(soup.find("h1", class_="headline speakable")).lower()
  
  # catching cases where there is no title header (for one reason or another)
  try:
    title = title.split(">")[1].split("<")[0] # trimming html tags off
  except:
    return "", 2
  
  return title, news_source

# title = from_url("https://www.foxnews.com/sports/juan-soto-sends-yankees-world-series-first-time-15-years")
# print(title)
X, y = prepare_data("url_only_data.csv")

# TODO: data normalization; parse if fox / nbc/ etc