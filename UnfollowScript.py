# Instagram unfollowing script.
# Made for 1920x1080 resolution monitors, probably wont work elsewhere.
# Select your constants, pass in the user list, and fullscreen Instagram on web.

######################## IMPORTS ########################

import pyautogui as gui
import numpy as np
import time
import datetime

####################### CONSTANTS #######################

# Time to prepare when running the script.
BEGINNING_DELAY = 10

# Set elimination order from oldest to newest.
OLDEST_TO_NEWEST = True

# Amount of seconds per unfollow on average, for time estimation. 
AVERAGE_SECONDS_PER_CYCLE = 10

#Time multiplier, for faster or slower unfollow cycles. 2 is double speed, 0.5 would be half speed.
TIME_MULTIPLIER = 1

# List of users to unfollow.
NAME_LIST = []

###################### FUNCTIONS ########################

# Determines "Following" button X position roughly. 11 being roughly the amount of button movement per username character.

def determineXPosition(NameLength):
    return 998 + (11*NameLength)
        
# Determines estimated remaining runtime, based on a number of inputs.

def determineEstimatedTime(Amount):
    totalSeconds = Amount*AVERAGE_SECONDS_PER_CYCLE
    return str(datetime.timedelta(seconds=totalSeconds))


####################### MAIN LOOP ########################

# Define variables.

count = 1
totalsize = len(NAME_LIST)
timeEstimate = determineEstimatedTime(totalsize)

# List flipping code

if (OLDEST_TO_NEWEST == True):
    ListToIterate = np.flip(NAME_LIST)
else:
    ListToIterate = NAME_LIST

# Beginning messages.

print("%i accounts to unfollow." % (totalsize))
print("Estimated time: %s." % (timeEstimate))
input("Press any key to continue")
print("You have %i seconds to open Instagram." % (BEGINNING_DELAY))
time.sleep(BEGINNING_DELAY)
print("Running script...")

    

# Loop over items.

for User in ListToIterate:

    # Status Indicator.
    print("%i out of %i. Est: %s" % (count, totalsize, determineEstimatedTime(totalsize-count)))
    
    # Click on search icon.
    time.sleep(1.1*TIME_MULTIPLIER)
    gui.click(x=40, y=300)
    
    # Click on search bar.
    time.sleep(1.5*TIME_MULTIPLIER)
    gui.click(x=175, y=223)
    
    # Type username.
    time.sleep(0.5*TIME_MULTIPLIER)
    gui.write(User)
    
    # Click first result.
    time.sleep(1.3*TIME_MULTIPLIER)
    gui.click(x=189, y=290)
    
    # Click on "Following".
    time.sleep(1.8*TIME_MULTIPLIER)
    gui.click(determineXPosition(len(User)), y=156)
    
    # Click on Unfollow.
    time.sleep(1.5*TIME_MULTIPLIER)
    gui.click(x=912, y=786)
    count+=1;
    
# Print end message.

print("Script ran successfully. %i accounts unfollowed." % (totalsize))
input()

