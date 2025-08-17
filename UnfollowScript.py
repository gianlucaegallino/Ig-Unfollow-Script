import pyautogui as gui
import numpy as np
import time
import datetime
import sys

'''
Instagram unfollowing script. Select your constants, pass in the user list, and fullscreen Instagram on web.
IMPORTANT: Must use Light mode and english.

For getting the non-follower list, i recommend:
1. Exporting your instagram data, only Followers + Following, as JSON.
2. Upload your file to followsback.com/instagram
3. After thats done, run the following lines in the browser console to get a name array.

let usernodes = document.querySelectorAll("td.break-all > span.font-bold");
let myArray = Array.from(usernodes);
let usernames = [];
console.log(myArray)
myArray.forEach(user => usernames.push(user.__reactProps$INSERTNAMEHERE.children));
console.log(usernames)
'''

####################### CONSTANTS #######################

# Time to prepare when running the script.
BEGINNING_DELAY = 5

# Time to wait for instagram load
FULL_LOAD = 2.5

# Time to wait for loads
LOAD_WAIT = 1

# Other load variables (do not modify)
MID_WAIT = LOAD_WAIT*1.5
MICRO_WAIT = LOAD_WAIT/2

# Set elimination order from oldest to newest.
OLDEST_TO_NEWEST = True

# Enable or disable blocking step
BLOCK = True

# List of users to unfollow.
NAME_LIST = []


###################### FUNCTIONS ########################

# Determines estimated remaining runtime, based on a number of inputs.
def determineEstimatedTime(Amount):
    totalSeconds = (2*MICRO_WAIT+FULL_LOAD+LOAD_WAIT+1.5)*Amount
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
        opt_loc = gui.locateCenterOnScreen(
            f'img/{image}',
            confidence=confidence,
            minSearchTime=search_time,
            grayscale=gray_scale,
            region=region
            )

        if opt_loc:
            gui.click(opt_loc)

            if sleep_time:
                time.sleep(sleep_time)
            
            return True

    except Exception as e:
        print(f"Error locating '{image}': {e}")
        return False

# Opens a new instagram tab while Closing the old one.
def getNewTab():
    gui.hotkey('ctrl', 't')
    gui.write('https://www.instagram.com')
    time.sleep(0.1)
    gui.press('enter')
    gui.hotkey('ctrl', 'tab')
    gui.hotkey('ctrl', 'f4')

# Opens a new instagram tab while Closing the old one.
def getPersonTab(currentUsername):
    gui.hotkey('ctrl', 't')
    gui.write(f'https://www.instagram.com/{currentUsername}/')
    time.sleep(0.1)
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
    print("You have %i seconds to open your browser." % (BEGINNING_DELAY))
    time.sleep(BEGINNING_DELAY)
    print("Running script...")


# Loop over items.

for User in ListToIterate:

    # Status Indicator.
    print("%i out of %i. Current: %s. Est: %s" % (count, totalsize, User, determineEstimatedTime(totalsize-count)))

    #Open new Instagram tab
    getPersonTab(User)

    # Wait for load
    time.sleep(FULL_LOAD)
    
    if BLOCK == True:
        # Click on burger icon.
        threedots_loc = gui.locateCenterOnScreen(f'img/{'threedots.PNG'}', confidence=0.54
        )

        if threedots_loc:
            gui.moveTo(threedots_loc, duration=0.1)
            gui.click()
        else:
            print("Burger icon not found at %s." % (User))
            sys.exit('Closing script...')

        time.sleep(MICRO_WAIT)

        # Click on block icon.
        block_loc = gui.locateCenterOnScreen(f'img/{'block.PNG'}', confidence=0.55
        )

        if block_loc:
            gui.moveTo(block_loc, duration=0.1)
            gui.click()
        else:
            print("Block icon not found at %s." % (User))
            sys.exit('Closing script...')

        time.sleep(MICRO_WAIT)

        # Confirm block icon.
        block2_loc = gui.locateCenterOnScreen(f'img/{'block2.PNG'}', confidence=0.7
        )

        if block2_loc:
            gui.moveTo(block2_loc, duration=0.1)
            gui.click()
        else:
            print("Block icon not found at %s." % (User))
            sys.exit('Closing script...')
    else:
        # Click on "Following".
        following_loc = gui.locateCenterOnScreen(f'img/{'following.PNG'}', confidence=0.54
        )

        if following_loc:
            gui.moveTo(following_loc, duration=0.1)
            gui.click()
        else:
            print("Following icon not found at %s." % (User))
            sys.exit('Closing script...')
        
        # Click on Unfollow.
        unfollow_loc = gui.locateCenterOnScreen(f'img/{'unfollow.PNG'}', confidence=0.54
        )

        if unfollow_loc:
            gui.moveTo(unfollow_loc, duration=0.1)
            gui.click()
        else:
            print("Unfollow icon not found at %s." % (User))
            sys.exit('Closing script...')


    #GO TO SEARCH BAR AND BACK TO INSTAGRAM
    time.sleep(LOAD_WAIT)
    count+=1
    
# Print end message.

print("Script ran successfully. %i accounts unfollowed." % (totalsize))
input("Press any key to exit.")
sys.exit('Closing script...')