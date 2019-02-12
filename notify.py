#! /usr/local/bin/python3
# Script source: https://stackoverflow.com/a/17651702/1585599
import os

# The notifier function
def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))


# Calling the function
notify(title    = 'Mood Diary',
       subtitle = 'Time to update your mood diary',
       message  = 'Run moody in terminal.')
