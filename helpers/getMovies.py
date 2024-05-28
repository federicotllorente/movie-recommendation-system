import pandas as pd
from helpers.cleanTitle import clean_title

def get_movies():
  movies = pd.read_csv("dataset/movies.csv")
  movies["clean_title"] = movies["title"].apply(clean_title)
  return movies
