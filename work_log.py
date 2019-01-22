import csv
import datetime
import re

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
    while True:
        print("\na) Add New Entry\nb) Search Existing Entry\nc) Quit Program\n")
        task = input("> ")

        if task.lower() == 'a':
            add_entry()
        elif task.lower() == 'b':
            search_menu()
        elif task.lower() == 'c':
            print("Thanks for using this work log!")
            break
        else:
            print("That was not an option")


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
    """
    Returns user given date as a datetime object
    """
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


def display_entries(rows):
    for row in rows:
        display_entry(row)


def display_entry(row):
    """
    Prints entry in uniform format
    """
    # print("\nTask name: " + row[0])
    # print("Task date: " + row[1])
    # print("Task minutes: " + row[2])
    # print("Task notes: " + row[3])

    print("\nTask name: " + row['name'])
    print("Task date: " + row['date'])
    print("Task minutes: " + row['time'])
    print("Task notes: " + row['note'])


def search_menu():
    """
    Opens menu with different options for searching entries
    """
    while True:
        print("\nWhat would you like to search by?")
        print("\na) By Date\nb) By Minutes\nc) By Keyword\nd) By Pattern\ne) By Range of Dates\nf) Return to Menu\n")
        search_task = input("> ")
        if search_task.lower() == 'a':
            search_date()
        elif search_task.lower() == 'b':
            search_time()
        elif search_task.lower() == 'c':
            search_exact()
        elif search_task.lower() == 'd':
            search_pattern()
        elif search_task.lower() == 'e':
            search_range()
        else:
            print("That was not an option")


def search_date():
    """
    Search based on exact date
    """
    search = input("\nPlease select desired date using YYYY-MM-DD format: ")
    search = (search + ' 00:00:00')
    with open('log.csv', 'r') as csvfile:
        entry_info = ['name', 'date', 'time', 'note']
        log_reader = csv.DictReader(csvfile, fieldnames=entry_info, delimiter=',')
        
        results = []
        for row in log_reader:
            if search == row['date']:
                result = row
                results.append(row)
                break
            else:
                result = None
                    
        if not result:
            print("Sorry, date not found. Please try again.")
        else:
            display_entries(results)


        #search_menu()
    
    # pagenation!
    # idx = 0
    # while True:
    #     display(result[idx])
    #     input("[n] to go to Next")
    #     if usr_input == 'n':
    #         idx +1
    #     elif usr_input == 'p':
    #         idx -=1
    

def search_time():
    """
    Search based on minutes spent on task
    """
    search = input("\nPlease type the minutes spent on desired task: ")
    # with open('log.csv', 'r') as csvfile:
    #     entry_info = ['name', 'date', 'time', 'note']
    #     log_reader = csv.DictReader(csvfile, fieldnames=entry_info, delimiter=',')
    for row in open():
        if search == row['time']:
            found = True
            if found:
                display_entry(row)
            if not found:
                print("Sorry, no entries took that amount of time. Please try again.")

    search_menu()
        
        
def search_range():
    """
    Search based on a range of dates
    """
    date_1 = input("Please first date in range of dates using YYYY-MM-DD format: ")
    date_1 = get_datetime(date_1)
    date_2 = input("Please second date in range of dates using YYYY-MM-DD format: ")
    date_2 = get_datetime(date_2)
    with open('log.csv', 'r') as csvfile:
        entry_info = ['name', 'date', 'time', 'note']
        log_reader = csv.DictReader(csvfile, fieldnames=entry_info, delimiter=',')
        for row in log_reader:
            if date_1 < row['date'] < date_2:
                found = True
                if found:
                    display_entry(row)
                elif not found:
                    print("Sorry, one or both dates not found. Please try again.")
        
        search_menu()


def search_exact():
    """
    Search based on exact keyword
    """
    search = input("Please select desired keyword: ")
    with open('log.csv', 'r') as csvfile:
        entry_info = ['name', 'date', 'time', 'note']
        log_reader = csv.DictReader(csvfile, fieldnames=entry_info, delimiter=',')
        for row in log_reader:
            found = False
            if search.lower() == row['name'].lower():
                found = True
            if found:
                display_entry(row)
                break
            
            elif not found:
                print("\nSorry, keyword not found. Please try again.")

        search_menu()


def search_pattern():
    """
    Search based on regex pattern                                        
    """
    search = input("Please select desired reg.exe pattern: ")
    with open('log.csv', newline='') as csvfile:
        entry_info = ['name', 'date', 'time', 'note']
        log_reader = csv.DictReader(csvfile, fieldnames=entry_info, delimiter=',')
        search = re.findall(r'\w', search)
        for row in log_reader:
            if search == row['name'] or row['date'] or row['time'] or row['note']:
                display_entry(row)
            else:
                print("Sorry, regex pattern not found. Please try again.")
        search_menu()


if __name__ == '__main__':
    welcome()
