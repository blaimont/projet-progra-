import colored,random, sys
import numpy as np
from itertools import zip_longest

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
    
def create_cruiser (cruiser_name):
    """ create cruisers next to the hub
    parameters
    ----------
    cruiser_name = the name of the cruiser (str)
    
    return
    ------
    energy = energy of the cruiser (int)
    structure_points= the structure points of the cruiser (int)
    distance_attaack = the portée of the attack (int)
    """

def create_ravitailleur (ravitailleur_name):
    """ create ravitailleurs next to the hub
    parameters
    ----------
    ravitailleur_name = the name of the ravitailleur (str)

    return
    ------
    energy = energy of the ravitailleur  (int)
    structure_points= the structure points of the ravitailleur(int)
    capicity_energy = the capicity of energy the ravitailleur can take (int)
    """

def move (unity_name, column_number, line_number):
    """ move the unity's where they want
    parameters
    ----------
    unity_name = the name of the unity that will move (str)
    column_number = the distance in column the unity will do (int)
    line_number = the distance in line the unity will do (int)
    """
def give_energy (hub_name, energy_amount):
    """ give energy to the cruiser
    parameters
    ----------
    hub_name = the name of the cruiser who will recieve the energy (str)
    energy_amount = the amount of energy gived to the cruiser

    return 
    ------
    cruiser_energy = the new energy of the cruiser (int)
    ravitailleur_energy = the new energy of the ravitalleur (int)   
    """
def pick_energy (unity_name):
    """ pick the energy of the hub or peaks 
    parameters 
    ----------
    unity_name = the name of the hub or peak (str)

    return
    ------
    hub_energy = the new energy of the hub (int)
    peak_energy = the new energy of the peak (int)
    ravitailleur_energy = the new energy of the ravitalleur (int)
    """
def attack (unity_name):
    """ attack an unity of the other player
    parameters
    ----------
    unity_name = the name of the unity attacked (str)
    """
def modify_caracter ():
    """ modify the caracter in the folder"""
def regeneration ():
    """regenerate the energy of a hub or a peak"""
def energy_quest ():
    """ launge the game to the end """
    create_map
    if structure_point_hub > 0:
        blabla 
def upgrade (unity_name, upgrade_sort, amount_upgrade):
    """ upgrades the unity with different aspects
    parameters 
    ----------
    """