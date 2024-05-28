from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from helpers.cleanTitle import clean_title

def find_movies_by_title(movies, title):
  tfidf = vectorizer.fit_transform(movies["clean_title"])
  vectorizer = TfidfVectorizer(ngram_range=(1,2))

  title = clean_title(title)
  query_vec = vectorizer.transform([title])
  similarity = cosine_similarity(query_vec, tfidf).flatten()
  indices = np.argpartition(similarity, -5)[-5:]
  
  results = movies.iloc[indices][::-1]
  return results
