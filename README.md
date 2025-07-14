# BoardgameRecommender

This is a python script that ranks boardgames based on bayesian weighted ranking. 

The input is a list of games and their review scores.

## 1) Edit the Games List

 If you don't know what reviewers match your taste or how to get their review scores, I recommend watching [this video](https://www.youtube.com/watch?v=QFwa6limKSc). What I do once I have the GeekBuddy Game Ratings is to take a screenshot and let an LLM transcribe it into the format below.

The *gameslist.py* file uses the following format (python tuple):

```python
games = [
    (game_name, average_score, reviews_nbr)
    (game_name, average_score, reviews_nbr)
    (game_name, average_score, reviews_nbr)
    ]
```


- `game_name` is the name of the boardgame
- `average_score` is the average score of the reviewers that you trust
- `reviews_nbr` is number of reviews used to calculate the `average_score`

Once you have the data for your games in this format, you can paste it into the *gameslist.py* file.

If you know how bayesian weighted rankings work, you can also change the *C* and *m* variables in *rank.py* to your liking.


## 2) Running the script

You need Git and Python installed on your machine. The commands below are for Mac Terminal and zshell (default Mac). Adapt them if you are using a different system.

Then, from the Terminal, clone the repository:

```
git clone https://github.com/janbsc4/BoardgameRecommender.git
```
And navigate to the project folder:
```
cd BoardgameRecommender
```

Then, edit the *gameslist.py* to your liking, as described in step 1). 

To run the script just:

```
python3 rank.py
```

The result should look something like this:

![screenshot](/Screenshot.png)
