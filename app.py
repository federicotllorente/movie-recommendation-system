from flask import Flask, request, jsonify
from recommendations.getRecommendations import get_recommendations as get_recommendations_list

app = Flask(__name__)

@app.route("/recommendations/<int:movie_id>", methods=["GET"])
def get_recommendations(movie_id):
  recommendations = get_recommendations_list(movie_id)
  return jsonify(recommendations)

if __name__ == "__main__":
  app.run(debug=True)
