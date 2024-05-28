import pandas as pd

def get_ratings():
  ratings = pd.read_csv("dataset/ratings.csv")
  return ratings
