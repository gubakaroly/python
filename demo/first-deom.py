import requests

def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    if response.status_code == 200:
        joke = response.json()
        return f"{joke['setup']} - {joke['punchline']}"
    else:
        return "Failed to fetch a joke."

def main():
    print("Welcome to the Random Joke App!")
    while True:
        input("Press Enter to get a joke (or Ctrl+C to exit)...")
        print(get_random_joke())
        print("-" * 40)

if __name__ == "__main__":
    main()
