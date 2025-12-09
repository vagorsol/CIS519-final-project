import numpy as np
import pandas as pd
import requests
import re
from bs4 import BeautifulSoup

def prepare_data(csv_path: str):
  '''
  given a csv file path, returns a list of news titles and their corresponding source
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
    if not title:
      continue

    X.append(title)
    y.append(news_source)

  return X, y

def from_url(url: str):
  '''
    Given a URL, reads and normalizes the title of the associated article

    Parameters:
    -----------
      url: the link to read from

    Returns:
    -----------
      title: the normalized title of the article from the url
      news_source: returns according to what the newsource is; 0 - foxnews | 1 - nbcnews
  '''
  # link pre-processing
  if ".print" in url:
    url = url.replace(".print", "")

  # try to read the link
  try:
    response = requests.get(url)
  except Exception as e:
    print(e) # this is for debugging
    return "", 2
  
  if response.status_code != 200:
    return "", 2
  
  # finds what its news source is  (foxnews - 0 | nbcnews - 1)
  news_source = 0 if "foxnews" in url else 1

  # which html tag to search headline by based on news source 
  hl_class = "headline speakable" if news_source == 0 else "article-hero-headline__htag"

  # get title (and convert it to a string)
  soup = BeautifulSoup(response.text, "html.parser")
  title = str(soup.find("h1", class_= hl_class))
  
  title = title.lower() # convert all to lowercase
  title = title.split(">")[1].split("<")[0] # trim html tags off  
  title = re.sub(r'[^\w\s]', '', title) # remove punctuation

  return title, news_source

X, y = prepare_data("url_only_data.csv") #"url_subset.csv")

print(X)
print(y)