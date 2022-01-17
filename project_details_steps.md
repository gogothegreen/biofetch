# Biofetch: A tool to fetch information on biological entities from various databases

### Background
Biological information is distrubuted across various databases across the web. Googling for information is time consuming. Hence, a tool that fetches relevant information from various sources with one single command is useful.

### Steps in the project
Create a folder with the project name. In our case, this is **biofech**. From within this folder, create a python virtual environment. Navigate to the project folder in the terminal and type the following command.

	$ python -m venv env

Next, activate the virtual environment called **env**. I use the following command on my Mac.

	$ . env/bin/activate

I will initially fetch information only from Wikipedia. For this, the **wikipedia** mnodule should be insdtalled using the command below.
	$ pip install wikipedia

In order to separate the source code from the settings, the **python-decouple** module wil be used.

	$ pip install python-decouple


First let us create a functions folder. In this folder, create a file called *online_ops.py*. Put the following in the file.

	import wikipedia

	def search_on_wikipedia(query):
    		results = wikipedia.summary(query, sentences=2)
    		return(results)

In the **biofetch** folder, create the "main.py" file and add the following code. First, import the necessary functions. 
	from functions.online_ops import search_on_wikipedia
	from datetime import datetime
	from decouple import config

Getting the variables from the **.env** file, and adding a function for user input.

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
 
Now, the __main__() function.

	if __name__ == "__main__":
    	say_hello()
    	while True:
        	query = input("Enter name of the biological entity for which you need me to find info: \n")
        	print(f"Fetching information about {query}")
		
        	wikipedia_results = search_on_wikipedia(query)
        	print(f"Wikipedia says....\n {wikipedia_results}")


