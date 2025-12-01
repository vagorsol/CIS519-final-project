import os
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

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
    return None

  soup = BeautifulSoup(response.text, "html.parser")

  title = str(soup.find("h1", class_="headline speakable")).lower()
  title = title.split(">")[1].split("<")[0] # trimming html tags off

  return title

title = from_url("https://www.foxnews.com/sports/juan-soto-sends-yankees-world-series-first-time-15-years")
print(title)

# TODO: data normalization; parse if fox / nbc/ etc