from functions.online_ops import search_on_wikipedia
from datetime import datetime
from decouple import config

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

# Greeting the user
def say_hello():
    """ Greets user according to time """

    hour = datetime.now().hour
    if(hour >= 6 and hour < 12):
        print(f"Good morning {USERNAME}")
    elif(hour >= 12 and hour < 16):
        print(f"Good afternoon {USERNAME}")
    elif(hour >= 16 and hour < 22):
        print(f"Good evening {USERNAME}")
    print(f"{BOTNAME} here!! I fetch biological data. What should I fetch for you?")

if __name__ == "__main__":
    say_hello()
    while True:
        query = input("Enter name of the biological entity for which you need me to find info: \n")
        print(f"Fetching information about {query}")

        wikipedia_results = search_on_wikipedia(query)
        print(f"Wikipedia says....\n {wikipedia_results}")
