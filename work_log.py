import datetime
import csv
import re
import pytz


FMT = '%Y-%m-%d'


def welcome():
	"""
	Asks for their name to be repeated back to them in a personalized welcome
	"""
	name = input("Welcome to work. What is your name? ")
	print("Hello, {}. Please choose a task: ".format(name))
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
		search_existing()
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
			time = abs(int(input("How many minutes did the task take? (negative numbers will be converted to positive) ")))
			return time
		except ValueError:
			print("Please try again using an integer to represent minutes spent on task ")


def add_entry():
	new_entry = []
	
	# Ask user the desired task name and append that to new_entry
	entry_name = input("What is the title of the task? ")
	new_entry.append(entry_name)
	
	# Ask user the desired date and append that to new_entry
	new_entry.append(entry_date())
	
	# Ask user the desired time in minutes and append that to new_entry
	new_entry.append(entry_time())

	# Ask user the desired notes and append that to new_entry
	entry_notes = input("Would you like to add any additional notes? (optional) ")
	if entry_notes != '':
		new_entry.append(entry_notes)
	else:
		new_entry.append('')
	
	# Write entry to log.csv
	write_csv(new_entry)
	
	# User is brought back to menu upon log completion
	start_menu()


def search_existing():
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
	search = input("\nPlease select desired date using YYYY-MM-DD format: ")
	with open('log.csv', newline='') as csvfile:
		log_reader = csv.reader(csvfile, delimiter=',')
		rows = list(log_reader)
		search = (search + ' 00:00:00')
		for row in rows:
			if search == row[1]:
				print(rows[0])
			else:
				search_existing()


def search_range():
	search = input("Please select desired range of dates: ")
	pass


def search_exact():
	search = input("Please select desired keyword: ")
	with open('log.csv', newline='') as csvfile:
		log_reader = csv.reader(csvfile, delimiter=',')
		rows = list(log_reader)
		for row in rows:
			if search.lower() == row[0] or row[3]:
				print(rows[0])
			else:
				search_existing()


def search_pattern():
	search = input("Please select desired pattern: ")
	with open('log.csv', newline='') as csvfile:
		data = csvfile.read()
		print(re.search(search, data))


# Code block to prevent script from executing if imported
if __name__ == '__main__':
	welcome()
