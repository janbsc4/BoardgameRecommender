# BoardgameRecommender

This is a python script that ranks boardgames based on bayesian weighted ranking.

You can edit the gameslist.py to your liking. It consists of a games in the following format:

`games = [
    (gamename, average, reviews)
    ]`

If you know what you are doing, you can also change the C and m variables in rank.py.

To get your results just run clone the repository, navigate to the BoardgameRecommender folder and run:

`python3 rank.py`