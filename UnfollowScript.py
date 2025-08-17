import pyautogui as gui
import numpy as np
import time
import datetime
import time
import keyboard as kb
import sys

# Instagram unfollowing script.
# Select your constants, pass in the user list, and fullscreen Instagram on web.
# IMPORTANT: Must use Light mode and english.

####################### CONSTANTS #######################

# Time to prepare when running the script.
BEGINNING_DELAY = 10

# Time to wait for instagram load
LOAD_TIME = 2.5

# Tiem to wait for mini-loads
MINI_LOAD = 1

# Set elimination order from oldest to newest.
OLDEST_TO_NEWEST = True

# Enable or disable blocking step
BLOCK = True

# Amount of seconds per unfollow on average, for time estimation. TODO: Rework
AVERAGE_SECONDS_PER_CYCLE = 18 if BLOCK == True else 10

#Time multiplier, for faster or slower unfollow cycles. 2 is half the speed, each cycle takes double 0.5 would be double speed, each cycle is halved.
TIME_MULTIPLIER = 1.8

# List of users to unfollow.
NAME_LIST = []


###################### FUNCTIONS ########################

# Determines estimated remaining runtime, based on a number of inputs.
def determineEstimatedTime(Amount):
    totalSeconds = (Amount*AVERAGE_SECONDS_PER_CYCLE)*TIME_MULTIPLIER
    return str(datetime.timedelta(seconds=totalSeconds))

# Locates image on screen.
def locate_img(
        image: str,
        sleep_time:float=None,
        search_time:float=0,
        confidence:float=1.0,
        gray_scale:bool=False,
        region:tuple[int,int,int,int]=None
    ):
    """Locate and click on an image. Returns True if successful, False otherwise."""
    try:
        opt_loc = pgui.locateCenterOnScreen(
            f'img/{image}',
            confidence=confidence,
            minSearchTime=search_time,
            grayscale=gray_scale,
            region=region
            )

        if opt_loc:
            pgui.click(opt_loc)

            if sleep_time:
                time.sleep(sleep_time)
            
            return True

    except Exception as e:
        print(f"Error locating '{image}': {e}")
        return False

# Opens a new instagram tab while closing the old one.
def getNewTab():
    #Open new Instagram tab
    gui.hotkey('ctrl', 't')
    gui.write('https://www.instagram.com')
    time.sleep(0.05)
    gui.press('enter')
    gui.hotkey('ctrl', 'tab')
    gui.hotkey('ctrl', 'f4')

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

if (totalsize == 0):
    print("ERROR: No accounts to unfollow.")
    input("Press any key to close.")
    sys.exit()
else:
    print("%i accounts to unfollow." % (totalsize))
    print("Estimated time: %s." % (timeEstimate))
    print("Accounts will be blocked?: %s." % (BLOCK))
    input("Press any key to continue")
    print("You have %i seconds to open Instagram." % (BEGINNING_DELAY))
    time.sleep(BEGINNING_DELAY)
    print("Running script...")


# Loop over items.

for User in ListToIterate:

    # Status Indicator.
    print("%i out of %i. Est: %s" % (count, totalsize, determineEstimatedTime(totalsize-count)))

    #Open new Instagram tab
    getNewTab()

    # Wait for load
    time.sleep(LOAD_TIME)
    
    # Click on search icon.
    searchicon_loc = pgui.locateCenterOnScreen(f'img/{'search.PNG'}', confidence=0.8)

    if searchicon_loc:
    pgui.moveTo(searchicon_loc, duration=0.2)
    pgui.click()
    else:
    print("Browser icon not found at %s." % (User))
    sys.exit('closing script')
    #TODO: Add better messages for logging
    
    # Type username.
    gui.write(User)

    # Wait for load
    time.sleep(MINI_WAIT)
    
    # Click first result.
    gui.press('tab')
    gui.press('tab')
    gui.press('enter')

    # Wait for load
    time.sleep(LOAD_TIME)

    if BLOCK == True:
        # Click on burger icon.
        threedots_loc = pgui.locateCenterOnScreen(f'img/{'threedots.PNG'}', confidence=0.8)

        if threedots_loc:
        pgui.moveTo(threedots_loc, duration=0.2)
        pgui.click()
        else:
        print("Burger icon not found at %s." % (User))
        sys.exit('closing script')

        # Click on block icon.
        block_loc = pgui.locateCenterOnScreen(f'img/{'threedots.PNG'}', confidence=0.8)

        if block_loc:
        pgui.moveTo(block_loc, duration=0.2)
        pgui.click()
        else:
        print("Block icon not found at %s." % (User))
        sys.exit('closing script')

        # Confirm block icon.
        block_loc = pgui.locateCenterOnScreen(f'img/{'threedots.PNG'}', confidence=0.8)

        if block_loc:
        pgui.moveTo(block_loc, duration=0.2)
        pgui.click()
        else:
        print("Block icon not found at %s." % (User))
        sys.exit('closing script')

    else:
        # Click on "Following".
        following_loc = pgui.locateCenterOnScreen(f'img/{'following.PNG'}', confidence=0.8)

        if following_loc:
        pgui.moveTo(following_loc, duration=0.2)
        pgui.click()
        else:
        print("Following icon not found at %s." % (User))
        sys.exit('closing script')
        
        # Click on Unfollow.
        unfollow_loc = pgui.locateCenterOnScreen(f'img/{'unfollow.PNG'}', confidence=0.8)

        if unfollow_loc:
        pgui.moveTo(unfollow_loc, duration=0.2)
        pgui.click()
        else:
        print("Unfollow icon not found at %s." % (User))
        sys.exit('closing script')


    #GO TO SEARCH BAR AND BACK TO INSTAGRAM
    time.sleep(MINI_WAIT)
    count+=1
    
# Print end message.

print("Script ran successfully. %i accounts unfollowed." % (totalsize))
input("Press any key to exit.")

