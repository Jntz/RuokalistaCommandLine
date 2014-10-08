# -*- coding: utf-8 -*-
import os, datetime

# Helpers variables
current_week = int(datetime.date.today().isocalendar()[1])
current_week_str = str(current_week)
# Helpers function
def clear():
	os.system('cls' if os.name == 'nt' else 'clear') #http://stackoverflow.com/a/2084628