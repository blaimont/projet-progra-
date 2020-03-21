import colored,random, sys
import numpy as np
from itertools import zip_longest
map = {'player1' : {'hub1':{'energy':int,
                            'regenaration rate':int,
                            'place':int,
                            'strucuture point':int},
                    }
        'player2': {'hub2':{'energy':int,
                            'regenaration rate':int,
                            'place':int,
                            'strucuture point':int},
                    }}
def grande_fonction():
  f = open("datas.txt","w+")
  create_map(f)
def create_map (f):
    """create the map with the hubs and the peaks on it
    """
    
    sys.argv[1]= random.randint(10,30)
    sys.argv[2]= random.randint(50,70)
    nb_rows = int(sys.argv[1])
    nb_cols = int(sys.argv[2])
    f.write("map:")
    f.write(str(nb_rows) +" "+  str(nb_cols) + "\n")

    # https://www.fileformat.info/info/unicode/block/geometric_shapes/images.htm
    line = '▒'
    fill = '●'
    s = []
    #colonnes
    s = [[c for c in '*'*nb_col]]
    for i in range(1,nb_rows):
        s = np.concatenate((s,s))
    
    #s = line * nb_cols + '\n'
    #for col in range(1, nb_rows):
     #   s += line * nb_cols + '\n'
      #  s += colored.fg(random.randint(10, 11))
       # s += colored.attr('reset')

    create_hub(f, s, nb_rows, nb_cols)
    print(s)
    
    
def create_hub (f, s, map_x, map_y):
    """ create 2 hubs of each player
    return
    ------
    energy = energy of the hub (int)
    structure_points= the structure points of the hub (int)
    energy_regeneration = regeneration rate of energy of the hub (float)
    """
    
    hubs = "◈"
    hub_x1 = random.randint(0, map_x-1)
    hub_y1 = random.randint(0, map_y-1)
    hub_x2 = random.randint(0, map_x)
    hub_y2 = random.randint(0, map_y)
    if hub_x2 == hub_x1: #si le 2ème hub a la même coordonnée que le premier, on la modifie
        hub_x2 +=1
    elif hub_y2 == hub_y1:
        hub_y2 +=1
    f.write("peaks:")
    f.write(hub_x1 + " " + hub_y2 + " " + "1500 25\n") #on écrit dans le fichier la coordonnées des hubs
    f.write(hub_x2 + " " + hub_y2 + " " + "1500 25\n")
    s[hub_x1][hub_y1] = hubs
    s[hub_x2][hub_y2] = hubs


 
    
def create_peaks ():
    """ create some peaks on the map
    return
    ------
    energy = energy of the peak (int)
    energy_regeneration = regeneration rate of energy of the peak (float)
    """
    peaks = '◎'
    clonemap = list(s)
    
    peaks_x1 = random.randint(0, map_x)
    peaks_y1 = random.randint(0, map_y)
    peaks_x2 = random.randint(0, map_x)
    peaks_y2 = random.randint(0, map_y)
    while peaks_x2 == peaks_x1 && peaks_peaks_y2 == peaks_y1:
        peaks_x2 = random.randint(0, map_x)
    peaks_x3 = random.randint(0, map_x)
    peaks_y3 = random.randint(0, map_y)
    while peaks_x3 == peaks_x1 && peaks_peaks_y3 == peaks_y1 || peaks_x3 == peaks_x2 && peaks_peaks_y3 == peaks_y2:
        peaks_x3 = random.randint(0, map_x)
    peaks_x4 = random.randint(0, map_x)
    peaks_y4 = random.randint(0, map_y)
    while peaks_x4 == peaks_x1 && peaks_peaks_y4 == peaks_y1 || peaks_x4 == peaks_x2 && peaks_peaks_y4 == peaks_y2 || peaks_x4 == peaks_x3 && peaks_peaks_y4 == peaks_y3:
        peaks_x3 = random.randint(0, map_x)

    f.write("peaks:")
    f.write(peaks_x1 + " " + peaks_y1 + " " + "1500 25\n") #on écrit dans le fichier la coordonnées des hubs
    f.write(peaks_x2 + " " + peaks_y2 + " " + "1500 25\n")
    f.write(peaks_x3 + " " + peaks_y3 + " " + "1500 25\n")
    f.write(peaks_x4 + " " + peaks_y4 + " " + "1500 25\n")
    s[peaks_x1][peaks_y1] = peaks
    s[peaks_x2][peaks_y2] = peaks
    s[peaks_x3][peaks_y3] = peaks
    s[peaks_x4][peaks_y4] = peaks

    
def create_cruiser (cruiser_name, player_name):
    """ This fonction creates the cruisers next to the hub.
    Parameters
    ----------
    cruiser_name : the name of the cruiser (str)
    player_name : the name of the player (str)

    Return
    ------
   all_cruisers : a dico with all the different cruisers (dict)
   cruiser_name : the name of the cruiser (dict)

    Version
    -------
    Specification : Louis Blaimont (17/02)
    Implémentation : Elodie Fiorentino
    """
#là il faut une liste pour l'emplacement du tanker (hub1 ou hub2) mais j'ai pas tout compris
cruiser_name = {"name" : cruiser_name, "y_coordinate" : y_coordinate, "x_coordonate" : x_coordonnate,
                "stucture_points" : 100, "energy_capacity" : 400, "moves_cost" : 10, "attack_cost" : 10,"cost_purchase" : 750} 
all_cruisers = cruiser_name #faut le déclarer dans la fct principale
return all_cruisers, cruiser_name

def create_tanker (tanker_name, player_name):
    """ This fonction creates the tankers next to the hub.
    Parameters
    ----------
    tanker_name : the name of the tanker (str)
    player_name : the name of the player (str)

    Return
    ------
    all_tankers : a dico with all the different tankers (dict)
    tanker_name : the name of the tanker (dict)

    Version
    -------
    Specification : Louis Blaimont (17/02)
    Implémentation : Camille Hooreman 
    """
#là il faut une liste pour l'emplacement du tanker (hub1 ou hub2) mais j'ai pas tout compris
tanker_name = {"name" : tanker_name, "y_coordinate" : y_coordinate, "x_coordonate" : x_coordonnate,
                "stucture_points" : 50, "energy_capacity" : 600, "moves_cost" : 0, "cost_purchase" : 1000} 
all_tankers = tanker_name #faut le déclarer dans la fonction principale
return all_tankers, tanker_name

def move (unity_name, column_number, line_number):
    """ Move the different unities where it is asked.
    Parameters
    ----------
    unity_name = the name of the unity that will move (str)
    column_number = the distance in column the unity will do (int)
    line_number = the distance in line the unity will do (int)

    Version
    -------
    Specification : Louis Blaimont (17/02/20)
    Implementation : 
    """
def give_energy (player_name, tanker_name, cruiser_name, energy_amount):
    """ Give energy to a cruiser.
    Parameters
    ----------
    player_name = the name of the player
    tanker_name = the name of the tanker who will give the energy (str)
    cruiser_name = the name of the cruiser who will recieve the energy (str)
    energy_amount = the amount of energy gived to the cruiser (int)

    Return 
    ------
    energy_cruiser = the new energy of the cruiser (int)
    energy_tanker = the new energy of the tanker (int)   

    Version
    -------
    Specification : Louis Blaimont (17/02/20), Camille Hooreman (06/03/20)
    Implementation :  
    """
def pick_energy (unity_name):
    """  Pick the energy out of the hub or peaks.
    Parameters 
    ----------
    unity_name = the name of the hub or peak where the tanker take the energy (str)

    Return
    ------
    hub_energy = the new energy of the hub (int)
    peak_energy = the new energy of the peak (int)
    energy_tanker = the new energy of the tanker (int)

    Version
    -------
    Specification : Louis Blaimont (17/02/20)
    Implementation : 
    """
def attack (unity_name):
    """Attack an unity of the other player.
    Parameters
    ----------
    unity_name = the name of the attacked unity (str)

    Returns
    -------
    energy_unity = the new energy of the unity after being attacked (int)

    Version
    -------
    Specification : Louis Blaimont
    Implementation : 
    """
def modify_caracter ():
    """ Modify the caracter in the folder
    
    Version
    -------
    Specification : Louis Blaimont (17/02/20)
    Implementation : """
def regeneration (percentage_regen_hubs, percentage_regen_peaks):
    """Regenerate the energy of a hub or a peak.
    
    Parameters
    ----------
    percentage_regen_hubs = how much the hubs regenerate after every turn (float)
    percentage_regen_peaks = how much the peaks regenerate after every turn (float)

    Return
    ------
    energy_hub = the new energy of the hubs (int)
    energy_peaks = the new energy of the peaks (int)

    Version  
    -------
    Specification : Camille Hooreman (06/03/20)
    Implementation : 
    """

def upgrade_tanker_energy (tanker_name):
    """ Upgrades the capacity of energy of a tanker

    Parameters 
    ----------
    tanker_name : the name of the tanker we want to upgrade (str)

    Return
    ------
    tanker_name : the tanker with his new capacity (dict)

    Version
    -------
    Specification : Louis Blaimont (17/02/20)
    Implementation : 
    """
if tanker_name["energy_capacity"] = 1200 : 
    #ne rien faire
else  : 
    tanker_name["energy_capacity"] += 100
    # -600 énergie dans le hub

def upgrade_cruiser_move (cruiser_name):
    """ Upgrades the moves costs of a cruiser

    Parameters 
    ----------
    cruiser_name : the name of the cruiser we want to upgrade (str)

    Return
    ------
    cruiser_name : the cruiser with his new move cost (dict)

    Version
    -------
    Specification : Louis Blaimont (17/02/20)
    Implementation : 
    """

if cruiser_name ["move_cost"] > 5 : 
    cruiser_name["move_cost"] -= 1
    #-500 énergie dans le hub
else : 
    #ne rien faire

def end_game () : 
    """ Finish the game and tell who's the winner.
    
    Version
    -------
    Specification : Camille Hooreman (06/03/20)
    Implementation : 
    """


def energy_quest ():
    """ launge the game to the end """
    create_map
    if structure_point_hub > 0:
        blabla 
