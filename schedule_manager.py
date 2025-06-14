import random
from schedule import build_lacrosse_schedule

_default_schedule = None

def get_default_schedule(teams):
    """
    Return the fixed default schedule for Season 1.
    Caches the schedule so it's consistent every time.
    """
    global _default_schedule
    if _default_schedule is None:
        _default_schedule = build_lacrosse_schedule(teams)
    return _default_schedule

def get_randomized_schedule(teams):
    """
    Return a new randomized schedule for subsequent seasons.
    Teams are shuffled to generate new matchups/order.
    """
    shuffled_teams = teams[:]
    random.shuffle(shuffled_teams)
    return build_lacrosse_schedule(shuffled_teams)
