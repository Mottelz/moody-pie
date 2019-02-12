# Moody-Pie
A simple mood diary in python and sqlite.

Moods are limited and can only be entered once per day (this is done by setting the date column in the database to unique). I have the notify script set up as a cronjob to remind me daily to fill it out. I've setup the main script as a simple terminal command.

The notify script comes from [here](https://stackoverflow.com/a/17651702/1585599).
