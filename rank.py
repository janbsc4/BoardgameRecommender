# bayesian_ranking.py

from gameslist import games

# Configuration
C = 4                # confidence parameter
m = 6.5              # global average

def bayesian_score(avg: float, v: int, C: float = C, m: float = m) -> float:
    """
    Compute Bayesian-adjusted score.
    avg = average rating for this game
    v   = number of reviews
    """
    S = avg * v
    return (C * m + S) / (C + v)

def rank_games(games):
    # Compute scores
    scored = []
    for name, avg, v in games:
        score = bayesian_score(avg, v)
        scored.append((name, avg, v, round(score, 3)))
    # Sort by Bayesian score descending
    scored.sort(key=lambda x: x[3], reverse=True)
    return scored

if __name__ == "__main__":
    ranking = rank_games(games)
    print(f"{'Rank':<5}{'Game':<25}{'Avg':>6}{'Rev':>6}{'Bayes':>8}")
    for idx, (name, avg, v, score) in enumerate(ranking, start=1):
        print(f"{idx:<5}{name:<25}{avg:6.2f}{v:6d}{score:8.3f}")