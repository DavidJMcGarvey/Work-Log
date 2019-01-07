import datetime
import csv
import pytz


FMT = '%m/%d/%Y'


def welcome():
	name = input("Welcome to work. What is your name? ")
	print("Hello, {}. Please choose a task: ".format(name))
	start_menu()


def start_menu():
	print("\na) Add New Entry\nb) Search Existing Entry\nc) Quit Program\n")
	task = input("> ")
	
	if task.lower() == 'a':
		add_entry()
	elif task.lower() == 'b':
		search_existing()
	else:
		print("Thanks for using this work log!")

		
def write_csv(entry):
	with open('log.csv', 'a') as csvfile:
		entry_info = ['name', 'date', 'time', 'note']
		log_writer = csv.DictWriter(csvfile, fieldnames=entry_info)
		
		log_writer.writerow({
			'name': entry[0],
			'date': entry[1],
			'time': entry[2],
			'note': entry[3],
		})
		
	
def add_entry():
	new_entry = []
	
	# Ask user the desired task name and append that to new_entry
	entry_name = input("What is the title of the task? ")
	new_entry.append(entry_name)
	
	# Ask user the desired date and append that to new_entry
	e_date = input("What date was the task completed? Please use MM/DD/YYYY format. ")
	entry_date = datetime.datetime.strptime(e_date, FMT)
	new_entry.append(entry_date)
	
	# Ask user the desired time in minutes and append that to new_entry
	entry_time = input("How many minutes did the task take? ")
	new_entry.append(int(entry_time))
	
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
	print("What would you like to search by?")
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
	search = input("\nPlease select desired date: ")
	with open('log.csv', newline='') as csvfile:
		log_reader = csv.reader(csvfile, delimiter='|')
		rows = list(log_reader)
		for row in rows:
			if search == row:
				print(row)
			else:
				search_existing()


def search_range():
	search = input("Please select desired range of dates: ")


def search_exact():
	search = input("Please select desired keyword: ")


def search_pattern():
	search = input("Please select desired pattern: ")



# Code block to prevent script from executing if imported
if __name__ == '__main__':
	welcome()
