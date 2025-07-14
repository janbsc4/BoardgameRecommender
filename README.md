# BoardgameRecommender

This is a python script that ranks boardgames based on bayesian weighted ranking.

You can edit the *gameslist.py* file to your liking. It consists of a games in the following format:

`games = [
    (gamename, average, reviews)
    ]`

`gamename` = name of the boardgame

`average` = average score of the reviewers you trust

`reviews` = number of reviews used to calculate the average score

If you don't know what reviewers match your taste or how to get their review scores, I recommend watching [this video](https://www.youtube.com/watch?v=QFwa6limKSc). What I do once I have the GeekBuddy Game Ratings is to take a screenshot and let an LLM transcribe it into a python tuple in the format shown in *gameslist.py*.

If you know how bayesian weighted ranking works, you can also change the *C* and *m* variables in *rank.py*.


## Getting Started

You need Git and Python installed on your machine.

Then, from the Terminal, clone the repository:

```
git clone https://github.com/janbsc4/BoardgameRecommender.git
```
And navigate to the project folder:
```
cd BoardgameRecommender
```

Then, edit the *gameslist.py* to your liking, adding games you're interested in. 

To run the script just:

```
python3 rank.py
```

The result should look something like this:
![screenshot][/Screenshot.png]

These commands are for Mac and zshell. Adapt them if you are on a different system.