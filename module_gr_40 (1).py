import colored,random, sys

def create_map (dictionnary):
    """ This fonction creates the map with the peaks and hubs on it.
    
    Return
    ------
    map = the map with the peaks and hubs

    Version
    -------
    Specification : 
    Implémentation :
    """
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
    #attenton à l'énergie prcq la on a seulement le max

    #write the peaks in the folder 
    fh.write('peaks:\n')
    nb_peaks = random.randint (3,8)
    map ['number_peaks'] = nb_peaks
    while nb_peaks > 0:
        x_coordonate_peak = str (random.randint(2, int(nb_rows)-2))
        y_coordonate_peak = str (random.randint(2, int(nb_cols)-2))
        energy = str (random.randint(200,600))
        fh.write (x_coordonate_peak + ' ' + y_coordonate_peak + ' ' + energy + '\n')
        nb_peaks -= 1
    fh.close ()

    #create the dictionnary 
    fh = open ('energy_quest.txt', 'r')
    lines = fh.readlines()

    #add the sice of the map
    line_map = lines[1]
    xx, yy = str.split(line_map[:-1], ' ')
    map ['sice'] = (int(xx),int(yy))

    #add the first hub
    line_hub1 = lines[3]
    x, y, energi, regenaration, structure_points = str.split(line_hub1[:-1], ' ')
    map ['player1']= {'hub': {'place':(int(x),int(y)),
                                'energy_capacity' : int(energi),
                                'energy':1500,
                                'regeneration_rate': int(regenaration),
                                'structure_points' : int(structure_points)}}

    #add the second hub
    line_hub2 = lines[4]
    x, y, energi, regenaration, structure_points = str.split(line_hub2[:-1], ' ')
    map ['player2']= {'hub': {'place':(int(x),int(y)),
                                'energy_capacity' : int(energi),
                                'energy':1500,
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
    #add tankers and cruisers key
    fh.close ()
    return map 

def showboard ():
    """This fonction displays a board with all the informations

    Version
    -------
    Specification : 
    Implémentation : 
    """
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
            x=0
            for peak in range (1, map ['number_peaks'] + 1):
                if (row, col) == map ['peak' + str(peak)]['place']:
                    board_str += '%s▲%s'%(colored.fg(20), colored.attr('reset'))
                    x=1
            if 'cruisers'in map['player1']:
                for cruiser in map ['player1']['cruisers']:
                    if (row, col) == map['player1']['cruisers'][cruiser]['place']:
                        board_str += '%s◉%s'%(colored.fg(10), colored.attr('reset'))
                        x=1
            if 'cruisers'in map['player2']:
                for cruiser in map ['player2']['cruisers']:
                    if (row, col) == map['player2']['cruisers'][cruiser]['place']:
                        board_str += '%s◉%s'%(colored.fg(11), colored.attr('reset'))
                        x=1
            if 'tankers'in map['player1']:
                for tanker in map ['player1']['tankers']:
                    if (row, col) == map['player1']['tankers'][tanker]['place']:
                        board_str += '%s▩%s'%(colored.fg(10), colored.attr('reset'))
                        x=1
            if 'tankers'in map['player2']:
                for tanker in map ['player2']['tankers']:
                    if (row, col) == map['player2']['tankers'][tanker]['place']:
                        board_str += '%s▩%s'%(colored.fg(11), colored.attr('reset'))
                        x=1
            elif (row, col) == map['player1']['hub']['place']:
                board_str += '%s◈%s'%(colored.fg(5), colored.attr('reset'))
            elif (row, col) == map['player2']['hub']['place']:
                board_str += '%s◈%s'%(colored.fg(1), colored.attr('reset'))
            elif x != 1:
                board_str += fill

        board_str += line + '\n'
        
    board_str += line * nb_cols
    print (board_str)  

def create_cruiser (cruiser_name, player_name):
    """ This fonction creates the cruisers next to the hub.
    Parameters
    ----------
    hub_place : the place of the hub of the player who creates the cruiser (str)
    cruiser_name : the name of the cruiser (str)
    player_name : the name of the player (str)

    Return
    ------
    map : the map with the new cruiser (dict)

    Version
    -------
    Specification : Louis Blaimont (17/02)
    Implémentation : Elodie Fiorentino, Louis Blaimont
    """

    hub_place = map [player_name]['hub']['place']
    map [player_name]['cruisers']= {cruiser_name:{'place': (hub_place[0],hub_place[1]),
                                                    'structure_points':100,
                                                    'energy_capacity':400,
                                                    'energy':400,
                                                    'move_cost': 10,
                                                    'attack_cost' : 10,
                                                    'firing_range':1}}
    #retirer l'énergie dans le bon hub
    return (map)

def create_tanker (tanker_name, player_name):
    """ This fonction creates the tankers next to the hub.
    Parameters
    ----------
    hub_place : the place of the hub of the player who creates the tanker (str)
    tanker_name : the name of the tanker (str)
    player_name : the name of the player (str)

    Return
    ------
    map : the map with the new tanker (dict)

    Version
    -------
    Specification : Louis Blaimont (17/02)
    Implémentation : Camille Hooreman, Louis Blaimont
    """
    hub_place = map [player_name]['hub']['place']
    map [player_name]['tankers']= {tanker_name: {'place': (hub_place[0],hub_place[1]),
                                                'structure_points':50,
                                                'energy_capacity':600,
                                                'energy':600,
                                                'move_cost': 0}}
    #retirer l'énergie dans le bon hub
    
    return map

def move (unity_name, direction, player_name):
    """ Move the different unities where it is asked.
    Parameters
    ----------
    unity_name = the name of the unity that will move (str)
    player_name = the new of the player who moves his unity (str)
    direction = the direction where he wants to move his unity (str)

    Return
    ------
    map = the map with the unity at its new place (dict)

    Version
    -------
    Specification : Louis Blaimont (17/02/20)
    Implementation : 
    """
    if unity_name[:-1] == 'cruiser':
        place = map[player_name]['cruisers'][unity_name]['place']
        if direction == 'right':
            new_place = place[1] 
            new_place += 1
            map[player_name]['cruisers'][unity_name]['place'] = (place[0], new_place)
        elif direction == 'left':
            new_place = place[1] 
            new_place -= 1
            map[player_name]['cruisers'][unity_name]['place'] = (place[0], new_place)
        elif direction == 'up':
            new_place = place[0]
            new_place -= 1
            map[player_name]['cruisers'][unity_name]['place'] = (new_place, place[1])
        elif direction == 'down':
            new_place = place[0] 
            new_place += 1
            map[player_name]['cruisers'][unity_name]['place'] = (new_place, place[1])
    elif unity_name[:-1] == 'tanker':
        place = map[player_name]['tankers'][unity_name]['place']
        if direction == 'right':
            new_place = place[1] 
            new_place += 1
            map[player_name]['tankers'][unity_name]['place'] = (place[0], new_place)
        elif direction == 'left':
            new_place = place[1] 
            new_place -= 1
            map[player_name]['tankers'][unity_name]['place'] = (place[0], new_place)
        elif direction == 'up':
            new_place = place[0]
            new_place -= 1
            map[player_name]['tankers'][unity_name]['place'] = (new_place, place[1])
        elif direction == 'down':
            new_place = place[0] 
            new_place += 1
            map[player_name]['tankers'][unity_name]['place'] = (new_place, place[1])
    return map
    #il faut encore modifier l'énergie des croiseurs lorsqu'ils se déplacent 

def attack (cruiser_attacking, unity_attacked, attack_domaged, player_name):
    """Attack an unity of the other player.
    Parameters
    ----------
    cruiser_attacking = the cruiser who does the attack (str)
    unity_attacked = the unity being attacked (str)
    player_name = the player who attacks (str)
    attack_domaged = the amount of damaged done (int)

    Returns
    -------
    map = the map with the unities with their new structure points (dict)

    Version
    -------
    Specification : Louis Blaimont
    Implementation : 
    """

    #for player1
    if player_name == 'player1':
        tuple_cruiser = map ['player1']['cruisers'][cruiser_attacking]['place']
        if unity_attacked[:-1] == 'cruiser':
            tuple_unity = map ['player2']['cruisers'][unity_attacked]['place']
        elif unity_attacked[:-1] == 'tanker':
            tuple_unity = map ['player2']['tankers'][unity_attacked]['place']
        elif unity_attacked == 'hub':
            tuple_unity = map ['player2']['hub']['place']

        #attack and changethe dictionnary
        energy_used = 10* attack_domaged
        distance = abs(tuple_cruiser[0]-tuple_unity[0]) + abs(tuple_cruiser[1]-tuple_unity[1])
        firing_range = map['player1']['cruisers'][cruiser_attacking]['firing_range']
        energy = map['player1']['cruisers'][cruiser_attacking]['energy']
        if firing_range <= distance and  energy >= energy_used:
            map ['player1']['cruisers'] [cruiser_attacking]['energy'] -= energy_used
            if unity_attacked[:-1] == 'cruiser':
                map ['player2']['cruisers'][unity_attacked]['structure_points']-= attack_domaged
                if map ['player2']['cruisers'][unity_attacked]['structure_points'] <= 0:
                    del map ['player2']['cruisers'][unity_attacked]

            elif unity_attacked[:-1] == 'tanker':
                map ['player2']['tankers'][unity_attacked]['structure_points']-= attack_domaged
                if map ['player2']['tankers'][unity_attacked]['structure_points'] <= 0:
                    del map ['player2']['tankers'][unity_attacked]

            elif unity_attacked == 'hub':
                map ['player2']['hub']['structure_points'] -= attack_domaged

    #for the player2
    elif player_name == 'player2':
        tuple_cruiser = map ['player2']['cruisers'][cruiser_attacking]['place']
        if unity_attacked[:-1] == 'cruiser':
            tuple_unity = map ['player1']['cruisers'][unity_attacked]['place']
        elif unity_attacked[:-1] == 'tanker':
            tuple_unity = map ['player1']['tankers'][unity_attacked]['place']
        elif unity_attacked == 'hub':
            tuple_unity = map ['player1']['hub']['place']

        #attack and changethe dictionnary
        energy_used = 10* attack_domaged
        distance = abs(tuple_cruiser[0]-tuple_unity[0]) + abs(tuple_cruiser[1]-tuple_unity[1])
        if map['player2']['cruisers'][cruiser_attacking]['firing_range'] <= distance and map['player2']['cruisers'][cruiser_attacking]['energy'] >= energy_used:
            map ['player2']['cruisers'] [cruiser_attacking]['energy'] -= energy_used
            if unity_attacked[:-1] == 'cruiser':
                map ['player1']['cruisers'][unity_attacked]['structure_points']-= attack_domaged
                if map ['player1']['cruisers'][unity_attacked]['structure_points'] <= 0:
                    del map ['player1']['cruisers'][unity_attacked]

            elif unity_attacked[:-1] == 'tanker':
                map ['player1']['tankers'][unity_attacked]['structure_points']-= attack_domaged
                if map ['player1']['tankers'][unity_attacked]['structure_points'] <= 0:
                    del map ['player1']['tankers'][unity_attacked]

            elif unity_attacked == 'hub':
                map ['player1']['hub']['structure_points'] -= attack_domaged
        
    return map

def upgrade (upgrade_kind, unity_name, player_name):
    """ All upgrades the player can buy and their effects.
    Parameters
    ----------
    upgrade_kind = which upgrade the player wanna do (str)
    unity_name = the unity being upgraded (str)
    player_name = the player who buy an upgrade (str)

    Return
    ------
    map = the map with the new informations (dict)

    Version
    -------
    Specification :
    Implementation : 
    """
    if unity_name[:-1] == 'cruiser':
        if upgrade_kind == 'firing_range' and map[player_name]['hub']['energy'] >=400 and map[player_name]['cruisers'][unity_name]['firing_range'] < 5:
            map[player_name]['cruisers'][unity_name]['firing_range'] += 1
            map[player_name]['hub']['energy'] -= 400
        
        elif upgrade_kind == 'move_cost' and map[player_name]['hub']['energy'] >=500 and map[player_name]['cruisers'][unity_name]['move_cost'] > 5:
            map[player_name]['cruisers'][unity_name]['move_cost'] -= 1
            map[player_name]['hub']['energy'] -= 500
        else:
            print ()

    elif unity_name[:-1] == 'tanker':
        if upgrade_kind == 'energy_capacity' and map[player_name]['tankers'][unity_name]['energy_capacity'] < 1200 and map[player_name]['hub']['energy'] >= 600:
            map[player_name]['tankers'][unity_name]['energy_capacity'] +=100 
            map[player_name]['hub']['energy'] -= 600
        
    elif unity_name == 'hub':
        if upgrade_kind == 'regenartion_rate' and map[player_name] ['hub']['regeneration_rate'] < 50 and map[player_name]['hub']['energy'] >= 750:
            map[player_name] ['hub']['regeneration_rate'] +=5 
            map[player_name]['hub']['energy'] -= 750
    return map

def give_energy (unit_giving, unit_receiving, energy_amount, player_name):
    """ pick energy of a unit and give it to another one
    Parameters
    ----------
    player_name = the name of the player (str)
    unit_giving = the name of the unit who gaves his energy (str)
    unit_receiving = the name of the unit who receives the energy (str)
    energy_amount = the amount of energy the player wants to give (int)

    Return 
    ------
    map = the map the new informations (dict)  

    Version
    -------
    Specification : Louis Blaimont (17/02/20), Camille Hooreman (06/03/20)
    Implementation :  nadia bouzin, louis blaimont
    """
    if unit_giving[:-1] == 'tanker':
        tuple_tanker = map [player_name]['tankers'][unit_giving]['place']
        if unit_receiving == 'hub':
            tuple_hub = map [player_name]['hub']['place']
            if tuple_tanker == tuple_hub:
                energy_capacity = map [player_name]['hub']['energy_capacity']
                if (map [player_name]['hub']['energy'] + energy_amount) <= energy_capacity and  map [player_name]['tankers'][unit_giving]['energy'] - energy_amount >=0:
                    map [player_name]['tankers'][unit_giving]['energy'] -= energy_amount
                    map [player_name]['hub']['energy'] += energy_amount

        if unit_receiving[:-1] == 'cruiser':
            tuple_cruiser = map [player_name]['cruisers'] [unit_receiving]['place']
            if tuple_tanker == tuple_cruiser:
                energy_capacity = map [player_name]['cruisers'][unit_receiving]['energy_capacity']
                if map [player_name]['cruisers'] [unit_receiving]['energy'] + energy_amount <= energy_capacity and map [player_name]['tankers'][unit_giving]['energy'] - energy_amount >=0:
                    map [player_name]['tankers'][unit_giving]['energy'] -= energy_amount
                    map [player_name]['cruisers'] [unit_receiving]['energy'] += energy_amount

    if unit_giving[:-1] == 'peak':
        tuple_peak = map [unit_giving]['place']
        if unit_receiving[:-1] == 'tanker':
            tuple_tanker = map [player_name]['tankers'] [unit_receiving]['place']
            if tuple_peak == tuple_tanker:
                energy_capacity = map[player_name]['tankers'][unit_receiving]['energy_capacity']
                if map [player_name]['tankers'] [unit_receiving]['energy'] + energy_amount <= energy_capacity and map [unit_giving]['energy'] - energy_amount >=0:
                    map [unit_giving]['energy'] -= energy_amount
                    map [player_name]['tankers'][unit_receiving]['energy'] += energy_amount
    
    if unit_giving == 'hub':
        tuple_hub = map [player_name]['hub']['place']
        if unit_receiving[:-1] == 'tanker':
            tuple_tanker = map [player_name]['tankers'] [unit_receiving]['place']
            if tuple_hub == tuple_tanker:
                energy_capacity = map[player_name]['tankers'][unit_receiving]['energy_capacity']
                if map [player_name]['tankers'] [unit_receiving]['energy'] + energy_amount <= energy_capacity and map [player_name]['hub']['energy'] - energy_amount >=0:
                    map [player_name]['hub']['energy'] -= energy_amount
                    map [player_name]['tankers'][unit_giving]['energy'] += energy_amount
    return map

def regeneration (player_name):

    """Regenerate the energy of a hub 
    
    Parameters
    ----------
    player_name = the name of the player who has his hubs regenerated (str)

    Return
    ------
    map = the map with the new informations (dict)

    Version  
    -------
    Specification : Camille Hooreman (06/03/20)
    Implementation : Elodie Fiorentino
    """
    map [player_name]['hub']['energy'] += map[player_name]['hub']['regeneration_rate']
    return map

def turn_finish (your_turn) : 
    """ allows the other player to play 
    Parameters
    ----------
    your_turn = if its a player's turn or not (bool)

    return
    ------
    your_turn = if its a player's turn or not (bool)

    Version
    -------
    Specification : Camille Hooreman (06/03/20)
    Implementation : 
    """
    your_turn == False
    showboard ()
    return your_turn

def order (player_name):
    """ Orders given by the players.
    Parameters
    ----------
    player_name = the name of the player
    
    Version
    -------
    Specification : 
    Implementation :
    """
    print ('the possible orders you can give are:\n\t- create cruiser\n\t- create tanker\n\t- move\n\t- attack\n\t- give energy\n\t- upgrade\n\t- turn finished')
    your_turn = True
    while your_turn == True:
        orders = str (input ('what do you want to do?: '))
        if orders == 'create cruiser':
            cruiser_name = str(input ('what is your cruiser name?:'))
            create_cruiser (cruiser_name, player_name)

        elif orders == 'create tanker':
            tanker_name = str(input ('what is your tanker name?:'))
            create_tanker (tanker_name, player_name)

        elif orders == 'move':
            moving_unit = str (input ('which unit do you want to move?:'))
            direction = str(input('in what direction do you want to move it?:'))
            move (moving_unit, direction, player_name)
        
        elif orders == 'attack': #si déjà bouger alors ne peut pas attaquer
            attacking_unit = str (input('with which cruiser do you want to attack?:'))
            attacked_unit = str (input ('which unit do you want to attack?:'))
            attack_domaged= int (input ('how much attack domaged do you want to do?:'))
            attack (attacking_unit, attacked_unit, attack_domaged, player_name)

        elif orders == 'give energy':
            giving_unit = str (input ('which unit give the energy?:'))
            receiving_unit = str (input ('which unit reveive the energy?:'))
            energy_amount = int (input ('how much energy do you want to transfer?:'))
            give_energy (giving_unit, receiving_unit, energy_amount, player_name)

        elif orders == 'upgrade':
            kind_of_upgrade = str(input ('what kind of upgrade do you want to do?:'))
            unit_name = str (input ('which unit do you want to upgrade?'))
            upgrade (kind_of_upgrade, unit_name, player_name)
        
        elif orders == 'turn finished':
            showboard ()
            turn_finish (your_turn)
        
        elif orders == 'stop':

            your_turn = False
            map ['player1']['hub']['structure_points'] = 0

map = {}
def energy_quest ():
    """ launch the game to the end 

    Version
    -------
    Specification :
    Implementation : 
    """
    
    create_map (map)
    player_turn = random.randint(1,2)

    while  map ['player1']['hub']['structure_points'] > 0 and map ['player2']['hub']['structure_points'] >0:
        your_turn = True
        while your_turn == True:
            showboard ()
            if player_turn %2 == 0:
                player_name = 'player1'            
            elif player_turn %2 != 0:
                player_name = 'player2'
            player_turn += 1
            regeneration (player_name)
            order (player_name)
    print ('the %s won!! \nWell played!!')