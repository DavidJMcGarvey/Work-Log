import datetime
import csv
import re
import pytz

# TODO:
# Uncomment welcome statement

FMT = '%Y-%m-%d'


def welcome():
	"""
	Asks for their name to be repeated back to them in a personalized welcome
	"""
	# name = input("Welcome to work. What is your name? ")
	# print("Hello, {}. Please choose a task: ".format(name))
	start_menu()


def start_menu():
	"""
	Opens menu with user options
	"""
	print("\na) Add New Entry\nb) Search Existing Entry\nc) Quit Program\n")
	task = input("> ")
	
	if task.lower() == 'a':
		add_entry()
	elif task.lower() == 'b':
		search_menu()
	elif task.lower() == 'c':
		print("Thanks for using this work log!")

		
def write_csv(entry):
	"""
	Writes work log input to a csv file
	"""
	with open('log.csv', 'a') as csvfile:
		entry_info = ['name', 'date', 'time', 'note']
		log_writer = csv.DictWriter(csvfile, fieldnames=entry_info)
		
		log_writer.writerow({
			'name': entry[0],
			'date': entry[1],
			'time': entry[2],
			'note': entry[3],
		})


def entry_date():
	"""
	Ask user for their desired date and if date does not match format an error is raised asking them to try again
	"""
	while True:
		try:
			date = input("What date was the task completed? Please use YYYY-MM-DD format. ")
			return datetime.datetime.strptime(date, FMT)
		except ValueError:
			print("Please try again using proper format")
			
			
def entry_time():
	"""
	Ask user for the time in minutes that their task took, sending back an error message if input is not an integer
	"""
	while True:
		try:
			time = abs(int(input("How many minutes did the task take? ")))
			return time
		except ValueError:
			print("Please try again using an integer to represent minutes spent on task ")


def get_datetime(date):
	return datetime.datetime.strptime(date, FMT)


def add_entry():
	"""
	Takes user input and appends it to an empty list that will be written to CSV upon log completion
	"""
	new_entry = []
	
	# Ask user the desired task name and append that to new_entry
	entry_name = input("What is the title of the task? ")
	new_entry.append(entry_name)
	
	# Append user input from entry_date() to new_entry
	new_entry.append(entry_date())
	
	# Append user input from entry_time() to new_entry
	new_entry.append(entry_time())

	# Ask user the desired notes and append that to new_entry
	entry_notes = input("Would you like to add any additional notes? (optional) ")
	if entry_notes != '':
		new_entry.append(entry_notes)
	else:
		new_entry.append('')
	
	# Write new_entry to log.csv
	write_csv(new_entry)

	# User is brought back to menu upon log completion
	start_menu()


def display_entry(entry):
	with open('log.csv', 'r') as csvfile:
		entry_info = ['name', 'date', 'time', 'note']
		log_reader = csv.DictReader(csvfile, fieldnames=entry_info, delimiter=',')
		for row in log_reader:
			if entry == row['date']:
				print("Task name: " + row['name'])
				print("Task date: " + row['date'])
				print("Task minutes: " + row['time'])
				print("Task notes: " + row['note'])
			else:
				print('Sorry bud')
		search_menu()
		
				
def search_menu():
	"""
	Opens menu with different options for searching entries
	"""
	print("\nWhat would you like to search by?")
	print("\na) By Date\nb) By Range of Dates\nc) By Keyword\nd) By Pattern\ne) Return to Menu\n")
	search_task = input("> ")
	if search_task.lower() == 'a':
		search_date()
	elif search_task.lower() == 'b':
		search_range()
	elif search_task.lower() == 'c':
		search_exact()
	elif search_task.lower() == 'd':
		search_pattern()
	else:
		start_menu()


def search_date():
	"""
	Search based on exact date
	"""
	search = input("\nPlease select desired date using YYYY-MM-DD format: ")
	search = (search + ' 00:00:00')
	with open('log.csv', 'r') as csvfile:
		entry_info = ['name', 'date', 'time', 'note']
		log_reader = csv.DictReader(csvfile, fieldnames=entry_info, delimiter=',')
		while True:
			for row in log_reader:
				if search == row['date']:
					print("\nTask name: " + row['name'])
					print("Task date: " + row['date'])
					print("Task minutes: " + row['time'])
					print("Task notes: " + row['note'])
					break
				else:
					print("Sorry, date not found. Please try again.")
				
			search_menu()


def search_range():
	date_1 = input("Please first date in range of dates using YYYY-MM-DD format: ")
	date_1 = get_datetime(date_1)
	date_2 = input("Please second date in range of dates using YYYY-MM-DD format: ")
	date_2 = get_datetime(date_2)
	with open('log.csv', 'r') as csvfile:
		entry_info = ['name', 'date', 'time', 'note']
		log_reader = csv.DictReader(csvfile, fieldnames=entry_info, delimiter=',')
		for row in log_reader:
			if row['date'] == date_1 or date_2:
				print("\nTask name: " + row['name'])
				print("Task date: " + row['date'])
				print("Task minutes: " + row['time'])
				print("Task notes: " + row['note'])
				break
			else:
				print("Sorry, date not found. Please try again.")
				break

		search_menu()
		
	
def search_exact():
	search = input("Please select desired keyword: ")
	with open('log.csv', 'r') as csvfile:
		entry_info = ['name', 'date', 'time', 'note']
		log_reader = csv.DictReader(csvfile, fieldnames=entry_info, delimiter=',')
		for row in log_reader:
			if search == row['name'] or search == row['note']:
				print("\nTask name: " + row['name'])
				print("Task date: " + row['date'])
				print("Task minutes: " + row['time'])
				print("Task notes: " + row['note'])
			else:
				print("Sorry Bud")
		search_menu()


def search_pattern():
	search = input("Please select desired reg.exe pattern: ")
	with open('log.csv', newline='') as csvfile:
		entry_info = ['name', 'date', 'time', 'note']
		log_reader = csv.DictReader(csvfile, fieldnames=entry_info, delimiter=',')
		search = re.findall(r'\w', search)
		for row in log_reader:
			if search == row['name'] or row['date'] or row['time'] or row['note']:
				print("\nTask name: " + row['name'])
				print("Task date: " + row['date'])
				print("Task minutes: " + row['time'])
				print("Task notes: " + row['note'])
			else:
				print("Sorry Bud")
		search_menu()
				

# Code block to prevent script from executing if imported
if __name__ == '__main__':
	welcome()
