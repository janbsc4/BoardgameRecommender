# BoardgameRecommender

This is a python script that ranks boardgames based on bayesian weighted ranking.

You can edit the *gameslist.py* to your liking. It consists of a games in the following format:

`games = [
    (gamename, average, reviews)
    ]`

gamename = name of the boardgame

average = average score of the reviewers you trust

reviews = number of reviews used to calculate the average score

If you know what you are doing, you can also change the *C* and *m* variables in *rank.py*.

To get your results just clone the repository, navigate to the BoardgameRecommender folder edit the gameslist.py to your liking, adding games youre interested in, for example.

When you are finished, run:

`python3 rank.py`