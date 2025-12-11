import numpy as np
import pandas as pd

DET = ["the", "a", "an"]

def prepare_data(csv_path: str):
  '''
  Given a csv file path, returns a list of news titles and their corresponding source
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
      url: the link to get the title from

    Returns:
    -----------
      title: the normalized title of the article from the url
      news_source: returns according to what the newsource is; 0 - foxnews | 1 - nbcnews
  '''
  # link pre-processing
  if ".print" in url:
    url = url.replace(".print", "")

  # finds what its news source is  (foxnews - 0 | nbcnews - 1)
  news_source = 0 if "foxnews" in url else 1

  # get the article title
  title = url.split("/")[-1].split("-") 

  # remove articles
  for word in title:
    if word in DET:
      title.remove(word)

  # if source is nbc, chop off identifier(?) at its end
  if news_source == 1:
    title = title[:-1]
  title = " ".join(title).lower()

  return title, news_source

X, y = prepare_data("url_subset.csv")#("url_only_data.csv") #"url_subset.csv")

print(X)
print(y)