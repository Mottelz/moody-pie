import sqlite3
import datetime
import inquirer

# Database connection
connection = sqlite3.connect('moods.db')
cursor = connection.cursor()

now = datetime.datetime.now().strftime('%Y-%m-%d')

# Setup the query
moods = [
  inquirer.List('mood',
                message="What was your mood today?",
                choices=['sad', 'anger', 'happy', 'anxious', 'proud'],  # Add new moods here.
                ),
]

# Ask for the mood
mood = inquirer.prompt(moods)['mood']

# Try/catch is because the database only allows one mood per day. 
try:
    cursor.execute("INSERT INTO moods(mood, date) VALUES ('" + mood + "', '" + now + "')")
except:
    print("You already added your mood for today.")
    connection.commit()
    connection.close()

# Save and close database connection
connection.commit()
connection.close()
