def normalize_recommendations(recommendations):
  recommendations_list = []

  for _, row in recommendations.iterrows():
    movie = {
      "movieId": row["movieId"],
      "title": row["title"],
      "genres": row["genres"].split("|")
    }
    recommendations_list.append(movie)

  return recommendations_list
