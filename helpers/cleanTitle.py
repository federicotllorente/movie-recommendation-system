import re

def clean_title(title):
  return re.sub("[^a-zA-Z0-9 ]", "", title)
