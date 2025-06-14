from default_teams import get_default_teams
from schedule_manager import get_default_schedule, get_randomized_schedule
from engine import run_season

def main():
    teams = get_default_teams()

    # Season 1 default schedule
    schedule = get_default_schedule(teams)

    champion = run_season(teams, schedule)
    print(f"Season 1 Champion: {champion.name}")

    # Next season randomized schedule
    new_schedule = get_randomized_schedule(teams)

    # Example: run Season 2 with new schedule
    champion2 = run_season(teams, new_schedule)
    print(f"Season 2 Champion: {champion2.name}")

if __name__ == "__main__":
    main()
