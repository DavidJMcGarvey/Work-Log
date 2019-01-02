import datetime
import csv
import pytz

ENTRIES = []
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
		
		log_writer.writeheader()
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
	
	write_csv(new_entry)
	
	start_menu()
	
	

def search_existing():
	pass


# Code block to prevent script from executing if imported
if __name__ == '__main__':
	welcome()
