import pandas as pd
from helpers.getMovies import get_movies
from helpers.getRatings import get_ratings
from helpers.normalizeRecommendations import normalize_recommendations
import helpers.constants as constants

def get_recommendations(movie_id):
  movies = get_movies()
  ratings = get_ratings()

  similar_users = ratings[(ratings["movieId"] == movie_id) & (ratings["rating"] >= constants.rating_weight)]["userId"].unique()
  similar_users_recs = ratings[(ratings["userId"].isin(similar_users)) & (ratings["rating"] >= constants.rating_weight)]["movieId"]

  similar_users_recs = similar_users_recs.value_counts() / len(similar_users)
  similar_users_recs = similar_users_recs[similar_users_recs > constants.similar_user_quantity]

  all_users = ratings[(ratings["movieId"].isin(similar_users_recs.index)) & (ratings["rating"] >= constants.rating_weight)]
  all_users_recs = all_users["movieId"].value_counts() / len(all_users["userId"].unique())

  rec_percentages = pd.concat([similar_users_recs, all_users_recs], axis=1)
  rec_percentages.columns = ["similar", "all"]
  rec_percentages["score"] = rec_percentages["similar"] / rec_percentages["all"]

  rec_percentages = rec_percentages.sort_values("score", ascending=False)
  rec_percentages = rec_percentages[rec_percentages.index != movie_id]
  rec_percentages = rec_percentages.head(constants.recommendations_quantity).merge(movies, left_index=True, right_on="movieId")
  
  return normalize_recommendations(rec_percentages)
