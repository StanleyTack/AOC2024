import os
import requests

def fetch_input(day, session_cookie):
    """Fetches the input for a given day from Advent of Code."""
    year = 2024
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = {"session": session_cookie}
    
    response = requests.get(url, cookies=cookies)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch input for day {day}. Status code: {response.status_code}")
        return None

def save_input(day, data, directory="input"):
    """Saves the input data to a file for the specified day."""
    if not os.path.exists(directory):
        os.makedirs(directory)
    filepath = os.path.join(directory, f"day{day}.txt")
    with open(filepath, 'w') as file:
        file.write(data)
    print(f"Saved input for day {day} to {filepath}")

def main():
    session_cookie = "SESSION_COOKIE"  # Replace with your session cookie from the browser
    
    for day in range(1, 26):  # Advent of Code has 25 days of challenges
        data = fetch_input(day, session_cookie)
        if data:
            save_input(day, data)

if __name__ == "__main__":
    main()
