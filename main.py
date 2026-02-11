import os
from datetime import datetime

# file name
file_name = "log.txt"

# write current date time
with open(file_name, "a") as f:
    f.write("Commit on: " + str(datetime.now()) + "\n")

# git commands
os.system("git add .")
os.system('git commit -m "Daily auto commit"')
os.system("git push")

print("Daily commit pushed to GitHub")
