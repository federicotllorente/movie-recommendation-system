# Movie recommendation system

This is a movie recommendation system made with Python. Also exposing a basic API made with Flask, in order to use it with a frontend app or an API gateway for example

## Get the initial data

You need to download the base dataset from [https://files.grouplens.org/datasets/movielens/ml-25m.zip](https://files.grouplens.org/datasets/movielens/ml-25m.zip). Then, copy and paste the `movies.csv` and `ratings.csv` files into `/dataset` from the project root

## Running this project

To run this project just execute `python app.py` or `python3 app.py` depending on the command you use on your machine (you have to have installed Python previously) in the root of the project. This will start the Flask API server on `http://localhost:5000`.

You will also need to install these dependencies with `pip install` or `pip3 install`:

- `flask`

- `pandas`

- `scikit-learn` (or `sklearn`, but it's deprecated)

## Endpoints

### GET

```
/recommendations/<movieId>
```

Get a list of 10 recommendations given a movie ID. This movie ID should correspond to a movie in the table in `dataset/movies.csv`
