import colored,random, sys


def create_map ():
    fh = open ('energy_quest.txt', 'w')

    #write the rows and cols of the map 
    fh.write ('map:\n')
    nb_rows =str(random.randint(15,30))
    nb_cols = str (random.randint(25,35))
    fh.write (nb_rows + ' '+ nb_cols +'\n')

    #write the hubs in the folder 
    fh.write ('hubs:\n')
    x_coordonate_hub_1 = str (random.randint(2,7))
    y_coordonate_hub_1 = str (random.randint(2,7))
    x_coordonate_hub_2 = str (random.randint(int(nb_rows)-7, int(nb_rows)-2))
    y_coordonate_hub_2 = str (random.randint(int(nb_cols)-7, int(nb_cols)-2))
    fh.write (x_coordonate_hub_1 + ' ' + y_coordonate_hub_1 + ' ' + '1500 25 750\n')
    fh.write (x_coordonate_hub_2 + ' ' + y_coordonate_hub_2 + ' ' + '1500 25 750\n')

    #write the peaks in the folder 
    fh.write('peaks:\n')
    nb_peaks = random.randint (3,8)
    number_peaks = nb_peaks

    while nb_peaks > 0:
        x_coordonate_peak = str (random.randint(2, int(nb_rows)-2))
        y_coordonate_peak = str (random.randint(2, int(nb_cols)-2))
        energy = str (random.randint(200,600))
        fh.write (x_coordonate_peak + ' ' + y_coordonate_peak + ' ' + energy + '\n')
        nb_peaks -= 1
    fh.close ()

    #create the dictionnary 
    fh = open ('energy_quest.txt', 'r')
    map = {}
    lines = fh.readlines()

    #add the sice of the map
    line_map = lines[1]
    xx, yy = str.split(line_map[:-1], ' ')
    map ['sice'] = (int(xx),int(yy))

    #add the first hub
    line_hub1 = lines[3]
    x, y, energi, regenaration, structure_points = str.split(line_hub1[:-1], ' ')
    map ['player1']= {'hub': {'place':(int(x),int(y)),
                                'energy' : int(energi),
                                'regeneration_rate' : int(regenaration),
                                'structure_points' : int(structure_points)}}

    #add the second hub
    line_hub2 = lines[4]
    x, y, energi, regenaration, structure_points = str.split(line_hub2[:-1], ' ')
    map ['player2']= {'hub': {'place':(int(x),int(y)),
                                'energy' : int(energi),
                                'regeneration_rate' : int(regenaration),
                                'structure_points' : int(structure_points)}}
    #add the peaks
    line_peaks = lines[6:]
    peak=1
    for line in line_peaks:
        x, y, energi = str.split(line[:-1], ' ')
        peak_key = 'peak' + str(peak)
        map [peak_key] = {'place':(int(x),int(y)),
                            'energy' : int(energi)}
        peak+=1
    fh.close ()
    print (map)

    #show the board
    sice = map ['sice']
    sys.argv[1]= sice[0]
    sys.argv[2] = sice[1]
    nb_rows = int(sys.argv[1])
    nb_cols = int(sys.argv[2])

    line = '□'
    fill = '■'

    board_str = line * nb_cols + '\n'
    for row in range(1, nb_rows-1):
        board_str += line
        for col in range(1, nb_cols-1):
            if (row, col) == map['player1']['hub']['place']:
                board_str += '%s◈%s'%(colored.fg(5), colored.attr('reset'))
            elif (row, col) == map['player2']['hub']['place']:
                board_str += '%s◈%s'%(colored.fg(1), colored.attr('reset'))
            for peak in range (1, number_peaks + 1):
                if (row, col) == map ['peak' + str(peak)]['place']:
                    board_str += '%s▲%s'%(colored.fg(20), colored.attr('reset'))
            else:
                board_str += fill

        board_str += line + '\n'
        
    board_str += line * nb_cols
    print (board_str)
create_map ()



def grande_fonction():
  f = open("datas.txt","w+")
  create_map(f)
    
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
    Implémentation : Elodie Fiorentino, Louis Blaimont
    """
    create_map ()
    print (map [player_name]['hub']['place'])
    hub_place = map [player_name]['hub']['place']
    map [player_name][cruiser_name]= {'place': (hub_place[0],hub_place[1]+1),
                                                'structure_points':100,
                                                'energy':400,
                                                'moves_cost': 10,
                                                'attack_cost' : 10,
                                                'firing_range':1} 
    print (map)
    return (map)
create_cruiser ('cruiser1', 'player1')


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
    Implémentation : Camille Hooreman, Louis Blaimont
    """
    create_map ()
    hub_place = map [str(player_name)]['hub']['place']
    map [str(player_name)][str(tanker_name)]= {'place': (hub_place[0] + 1,hub_place[1]),
                                                'structure_points':50,
                                                'energy':600,
                                                'moves_cost': 0} 
    print (map)
    return map

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
    Implementation : Elodie Fiorentino
    """
    if hub1["energy"] == 1500 :
        energy = 1500
    else :
         hub1["energy"] +=10

    if hub2 ["energy"] == 1500 :
        energy = 1500
    else :
         hub2["energy"] +=10
    
    if all_peaks["peakn"] == int :
        peakn = int
    else:
        all_peaks["peakn"] +=10

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
    Implementation : Camille Hooreman
    """
    if tanker_name["energy_capacity"] >= 1200 : 
        tanker_name ["energy_capacity"] = 1200
    else  : 
        tanker_name["energy_capacity"] += 100
        player_hub["energy"] -= 600

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
    Implementation : Camille Hooreman
    """
    if cruiser_name ["move_cost"] > 5 : 
        cruiser_name["move_cost"] -= 1 
        player_hub["energy"] -= 500
    else : 
        cruiser_name ["move_cost"] = 5

def upgrade_cruiser_range(cruiser_name) :
    """Upgrades the range of a cruiser
    Parameters
    ----------
    cruiser_name : the name of the cruiser we want to upgrade (str)
    Return
    ------
    cruiser_name : the cruiser with his new range (dict)
    Version
    -------
    """

def upgrade_regen_hub (player_name) :
    """ Upgrades the percentage of regeneration of a hub.
    Parameters
    ----------
    player_name : the name of the player who wants to upgrade his hub (str)
    Return
    ------
    player_name : the name of the player with his new hub (dict)
    Version
    -------
    Specification : Camille Hooreman
    Implementation : Camille Hooreman
    """
    if player_name ["regenaration rate"] >= 50 :
        player_name ["regenaration rate"] = 50
    else :
        player_name["regenaration rate"] += 5
        player_hub ["energy"] -= 750

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
