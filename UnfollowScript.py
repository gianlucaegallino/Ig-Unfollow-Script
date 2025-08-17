import pyautogui as gui
import numpy as np
import time
import datetime
import sys
import keyboard as kb

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
NAME_LIST = [
    "valencudly",
    "aylupetrone",
    "vickycazella",
    "claraalcoba",
    "trinisireix",
    "lubertarini",
    "martu_viglione",
    "naisnice__",
    "roproxy",
    "joseline__2.0",
    "dolljm.n",
    "alfocarbajal_",
    "prii.poncee",
    "ilischmid_",
    "cata.bermejo",
    "emii.boccanera",
    "abimendoza__",
    "conyfurla",
    "meli_frndz",
    "ambinunez0",
    "guadadelorenzis",
    "taysa_elena",
    "valeneguen_",
    "nikollramoss",
    "camiimolinaa_",
    "lunastrokera",
    "milegalvann",
    "iaralazarte",
    "camitallerico",
    "juani.biderman",
    "sofiaaoliveraa_",
    "florstroia",
    "avrilmengoni",
    "juliett.mirandaa",
    "cecii_andriossi",
    "violedomi",
    "anita_delibes",
    "solaebi",
    "valencortadello",
    "lupena01_",
    "julibaci",
    "marianela.pepe",
    "vickymheide",
    "ambartorresi",
    "luz.caviglia",
    "candemoreiira",
    "vickxzzs",
    "araborgess",
    "luli_cassagne",
    "marssss_15406",
    "cande_garcia4",
    "ggabdiaz",
    "mdickel_",
    "_iaaara",
    "maitsotelo",
    "anibakker",
    "rafi.seguetti",
    "solbertozzi",
    "camiitalgham",
    "bian_bottino",
    "luusanjuann",
    "belumaudet",
    "abrilgandolfi",
    "jazminfermani",
    "luadavalos",
    "ninixlng",
    "abruulorenzo",
    "laayybarreto",
    "azucebey",
    "_barbara_barrera",
    "belendragonetti",
    "cataliinajimenez",
    "_kirii.k",
    "palonaife_",
    "keikokataoka___",
    "ale.lasala_",
    "raaniaa.er",
    "v.3ralyy",
    "luchi_penia",
    "evaracioppi_",
    "alapo.oi",
    "sofiaqrg",
    "s0pyw",
    "giapv___",
    "sofxiak_",
    "miluu0054_",
    "rojjjit4",
    "tatiianarmas",
    "riisk.kk",
    "catawagnerr",
    "_stipelcovich_",
    "candestagnaro",
    "camiluuna",
    "agusguasch",
    "anngiebianco",
    "_linnisokay",
    "flor.demattei",
    "soffi_portu",
    "ailumunoz_",
    "yenhylucino",
    "camtorres__",
    "abrilvontiuk",
    "diamela.aa",
    "ara_tabares",
    "d0ll.f4c3_",
    "hmniluli",
    "alicia_corral21",
    "miss.duvet",
    "yassgerz",
    "rosevvengeance",
    "juafiig",
    "fatiiguzz",
    "_slay3r.zzz",
    "martinaferrarads",
    "almucorness",
    "aldiii_acn",
    "julietapizarro_",
    "jimerivvv",
    "martinapicouto",
    "luna.stb",
    "camdestroy",
    "zzoe_jaworski",
    "gbrisag_",
    "juanisofer",
    "miraaanda_reca",
    "cata_serue13",
    "miluuuuaguirre",
    "aguscamposr",
    "claranascimbene",
    "cande.cast.illo",
    "lucia_sigot",
    "jez.awada",
    "cataa_jerez",
    "angelesloza54",
    "tizi_anastacioo",
    "i.am.lenn",
    "gzzina",
    "es3ncia__",
    "fffanny.gd",
    "petitechipa",
    "iaelbenitez",
    "meelielizabeth",
    "torrenssofia_",
    "abru_ferra",
    "eveferrari_",
    "bbreenn__",
    "vickkk._",
    "aantoscrocchii",
    "zzzzzoe____",
    "lici_marenda",
    "samidagosta",
    "priscylashantall",
    "catalinarey_",
    "aliidarre",
    "maricarli_",
    "lau_mondino",
    "fausti0119",
    "cortezflorenciaa",
    "nicolluciague02",
    "ironmantri",
    "vaallvera",
    "karenn_clc",
    "victoriahueta1",
    "_arianaalonsoo",
    "ayelen_201",
    "irrriel",
    "ghaliavanlacke",
    "antoo_manentee",
    "nahi_barretoo",
    "claarialoonso",
    "maaiavilaa",
    "sofia.lareu",
    "nahigebel",
    "ro_cafere",
    "_jflow3r__",
    "camimoreira0",
    "fiamatemporetti",
    "_lucii_x1",
    "marabermudess",
    "celeste__labra",
    "ssoffiacs",
    "fiore.beruschi",
    "tiara.rnr",
    "magui.f1",
    "candela.darco",
    "selsparano",
    "zostach",
    "21jullie",
    "onawolk",
    "bri.ojeeda",
    "valenherman_",
    "s4mmass",
    "brissavique",
    "___.vxlwn",
    "kmyramos",
    "mika_coppola",
    "lariblu93k",
    "maiaguiter_",
    "clarivillalbaa_",
    "candee_ayrala",
    "juana.somoza",
    "m3t4tr0nn",
    "emii_rouse",
    "milibtez",
    "biianca0054",
    "lulaau.u",
    "liingmz",
    "so__anyelen",
    "carolinammzz",
    "solmarinelli2",
    "daivillalbaa_",
    "__melirolon",
    "mar_______tina",
    "violehoepnerr",
    "flor.bello24",
    "eugecardi",
    "martinaadiaz",
    "bbcnews",
    "clariita.ra",
    "aldureynoso",
    "llunacristobo",
    "venusqirl",
    "anarcesible",
    "_rosanchezzz",
    "svneei_",
    "kiarapf",
    "juhenricot",
    "matthewolivierx",
    "kyaraapaz",
    "whosaldana",
    "josemerlo1",
    "maidruetta"
]   


###################### FUNCTIONS ########################

# Determines estimated remaining runtime, based on a number of inputs.
def determineEstimatedTime(Amount):
    totalSeconds = (2*MID_WAIT+2*MICRO_WAIT+FULL_LOAD+LOAD_WAIT+0.6+2)*Amount
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
        print("%i out of %i. Current: %s. Est: %s" % (count, totalsize, Current, determineEstimatedTime(totalsize-count)))

        #Open new Instagram tab
        getNewTab()

        # Wait for load
        time.sleep(FULL_LOAD)
        
        # Click on search icon.
        sx, sy = gui.locateCenterOnScreen(f'img/{'search.PNG'}', confidence=0.7
        )

        if sx:
            gui.moveTo(sx, sy, duration=0.1)
            gui.click()
        else:
            print("Browser icon not found at %s." % (User))
            sys.exit('Closing script...')
        
        # Type username.
        gui.write(User)

        # Wait for load
        time.sleep(MID_WAIT+0.6)
        
        # Click first result.
        sx=sx+100
        gui.moveTo(sx, sy, duration=0.1)
        gui.click()


        # Wait for load
        time.sleep(MID_WAIT)

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
            block2_loc = gui.locateCenterOnScreen(f'img/{'block2.PNG'}', confidence=0.62
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

