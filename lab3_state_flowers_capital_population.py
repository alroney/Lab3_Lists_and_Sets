# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 18:43:57 2022

@author: Andrew
Date: 8/26/2022
Description: The program allows the user to view all 50 states of the U.S
    along with their capital, bird, population, flower
"""


import os
import urllib
from io import BytesIO
from PIL import Image
import matplotlib.pyplot as plot
import requests

URL1 = 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/'
URL2 = 'symbol_thumbnail__medium/public/'

url = urllib.parse.urljoin(URL1, URL2)



state_list = []#Create an empty list to then have states added on to it.

#List item order goes as [Name, Capital, Population, Flower, URL img of Flower]


#ALABAMA
state_list.append ( ['Alabama', 'Montgomery', 5024279, 'Camellia',
url +"camellia-flower.jpg"] )

#ALASKA
state_list.append ( ['Alaska', 'Juneau', 733391, 'Forget-Me-Not',
url +"primary-images/Alpineforgetmenot.jpg"] )

#ARIZONA
state_list.append ( ['Arizona', 'Phoenix', 7151502, 'Suguaro Catus Blossom',
url +"saguaroflowersFlickr.jpg"] )

#ARKANSAS
state_list.append ( ['Arkansas', 'Little Rock', 3011524, 'Apple Blossom',
url +"primary-images/AppletreeblossomArkansasflower.JPG"] )

#CALIFORNIA
state_list.append ( ['California', 'Sacramento ', 39538223, 'California Poppy',
url +"primary-images/CAflowerCaliforniaPoppy.jpg"] )

#COLORADO
state_list.append ( ['Colorado', 'Denver', 5773714, 'Rocky Mountain Columbine',
url +"Colorado_columbine2.jpg"] )

#CONNECTICUT
state_list.append ( ['Connecticut', 'Hartford', 3605944, 'Mountain Laurel',
url +"primary-images/Mountain-Laural-flowers2.jpg"] )

#DELAWARE
state_list.append ( ['Delaware', 'Dover', 989948, 'Peach Blossom',
url +"primary-images/peachblossomspeachflowers.jpg"] )

#FLORIDA
state_list.append ( ['Florida', 'Tallahassee', 21538187, 'Orange Blossom',
url +"primary-images/OrangeBlossomsFloridaFlower.jpg"] )

#GEORGIA
state_list.append ( ['Georgia', 'Atlanta', 10711908, 'Cherokee Rose',
url +"primary-images/CherokeeRoseFlower.jpg"] )

#HAWAII
state_list.append ( ['Hawaii', 'Honolulu', 1455271, 'Hinahina',
url +"primary-images/HinahinaKahoolaweLei3.jpg"] )

#IDAHO
state_list.append ( ['Idaho', 'Boise', 1839106, 'Syringa',
url +"primary-images/syringaPhiladelphuslewisiiflower.jpg"] )

#ILLINOIS
state_list.append ( ['Illinois', 'Springfield', 12812508, 'Violet',
url +"primary-images/singlebluevioletflower.jpg"] )

#INDIANA
state_list.append ( ['Indiana', 'Indianapolis', 6785528, 'Peony',
url +"primary-images/PeonyPaeoniaflowers.jpg"] )

#IOWA
state_list.append ( ['Iowa', 'Des Moines', 3190369, 'Wild Rose',
url +"primary-images/WildPrairieRose.jpg"] )

#KANSAS
state_list.append ( ['Kansas', 'Topeka', 2937880, 'Wild Native Sunflower',
url +"primary-images/native-sunflowers.jpg"] )

#KENTUCKY
state_list.append ( ['Kentucky', 'Frankfort', 4505836, 'Goldenrod',
url +"primary-images/stateflowergoldenrod-bloom.jpg"] )

#LOUISIANA
state_list.append ( ['Louisiana', 'Baton Rouge', 4657757, 'Magnolia',
url +"primary-images/MagnoliagrandifloraMagnoliaflower.jpg"] )

#MAINE
state_list.append ( ['Maine', 'Augusta', 1362359, 'Pine Cone & Tassel',
url +"primary-images/whitepinemalecones.jpg"] )

#MARYLAND
state_list.append ( ['Maryland', 'Annapolis', 6177224, 'Black-eyed Susan',
url +"primary-images/FlowerMDBlack-eyedSusan.jpg"] )

#MASSASCHUSETTS
state_list.append ( ['Massachusetts', 'Boston', 7029917, 'Mayflower',
url +"primary-images/MayflowerTrailingArbutus.jpg"] )

#MICHIGAN
state_list.append ( ['Michigan', 'Lansing', 10077331, 'Apple Blossom',
url +"primary-images/appleblossombeauty.jpg"] )

#MINNESOTA
state_list.append ( ['Minnesota', 'St.Paul', 5706494, 'Lady-Slipper',
url +"primary-images/pinkwhiteladysslipperflower1.jpg"] )

#MISSISSIPPI
state_list.append ( ['Mississippi', 'Jackson', 2961279, 'Magnolia',
url +"primary-images/magnoliablossomflower01.jpg"] )

#MISSOURI
state_list.append ( ['Missouri', 'Jefferson City', 6154913, 'Hawthorne Blossom',
url +"primary-images/hawthornflowersblossoms1.jpg"] )

#MONTANA
state_list.append ( ['Montana', 'Helena', 1084225, 'Bitterroot',
url +"primary-images/bitterrootfloweremblem.jpg"] )

#NEBRASKA
state_list.append ( ['Nebraska', 'Lincoln', 1961504, 'Goldenrod',
url +"primary-images/goldenrodflowersyellow4.jpg"] )

#NEVADA
state_list.append ( ['Nevada', 'Carson City', 3104614, 'Sagebrush',
url +"primary-images/Nevada-Sagebrush-Artemisia-tridentata.jpg"] )

#NEW HAMPSHIRE
state_list.append ( ['New Hampshire', 'Concord', 1377529, 'Purple Lilac',
url +"primary-images/lilacflowerspurplelilac.jpg"] )

#NEW JERSEY
state_list.append ( ['New Jersey', 'Trenton', 9288994, 'Violet',
url +"wood-violet.jpg"] )

#NEW MEXICO
state_list.append ( ['New Mexico', 'Santa Fe', 2117522, 'Yucca',
url +"primary-images/YuccaFlowersclose.jpg"] )

#NEW YORK
state_list.append ( ['New York', 'Albany', 20201249, 'Rose',
url +"primary-images/redrosebeautystateflowerNY.jpg"] )

#NORTH CAROLINA
state_list.append ( ['North Carolina', 'Raleigh', 10439388, 'Dogwood',
url +"primary-images/floweringdogwoodflowers2.jpg"] )

#NORTH DAKOTA
state_list.append ( ['North Dakota', 'Bismark', 779094, 'Prairie Rose',
url +"primary-images/flowerwildprairierose.jpg"] )

#OHIO
state_list.append ( ['Ohio', 'Columbus', 11799448, 'Red Carnation',
url +"primary-images/redcarnationOhioflower.jpg"] )

#OKLAHOMA
state_list.append ( ['Oklahoma', 'Oklahoma City', 3959353, 'Mistletoe',
url +"primary-images/mistletoe_phoradendron_serotinum.jpg"] )

#OREGON
state_list.append ( ['Oregon', 'Salem', 4237256, 'Oregon Grape',
url +"primary-images/Oregongrapeflowers2.jpg"] )

#PENNSYLVANIA
state_list.append ( ['Pennsylvania', 'Harrisburg', 13002700, 'Mountain Laurel',
url +"Mt_Laurel_Kalmia_Latifolia.jpg"] )

#RHODE ISLAND
state_list.append ( ['Rhode Island', 'Providence', 1097379, 'Violet',
url +"primary-images/violetsflowers.jpg"] )

#SOUTH CAROLINA
state_list.append ( ['South Carolina', 'Columbia', 5118425, 'Yellow Jessamine',
url +"primary-images/CarolinaYellowJessamine101.jpg"] )

#SOUTH DAKOTA
state_list.append ( ['South Dakota', 'Pierre', 886667, 'American Pasque',
url +"primary-images/Pasqueflower-03.jpg"] )

#TENNESSEE
state_list.append ( ['Tennessee', 'Nashville', 6910840, 'Iris',
url +"primary-images/purpleirisflower.jpg"] )

#TEXAS
state_list.append ( ['Texas', 'Austin', 29145505, 'Bluebonnet',
url +"primary-images/BluebonnetsBlueRed.jpg"] )

#UTAH
state_list.append ( ['Utah', 'Salt Lake City', 3271616, 'Sego Lily',
url +"SegoLily.jpg"] )

#VERMONT
state_list.append ( ['Vermont', 'Montpelier', 643077, 'Red Clover',
url +"primary-images/redcloverstateflowerWV.jpg"] )

#VIRGINIA
state_list.append ( ['Virginia', 'Richmond', 8631393, 'American Dogwood',
url +"primary-images/floweringDogwoodSpring.jpg"] )

#WASHINTON
state_list.append ( ['Washington', 'Olympia', 7705281, 'Coast Rhododendron',
url +"primary-images/flower_rhododendronWeb.jpg"] )

#WEST VIRGINIA
state_list.append ( ['West Virginia', 'Charleston', 1793716, 'Rhododendron',
url +"primary-images/rhododendronWVstateflower.jpg"] )

#WISCONSIN
state_list.append ( ['Wisconsin', 'Madison', 5893718, 'Wood Violet',
url +"wood-violet.jpg"] )

#WYOMING
state_list.append ( ['Wyoming', 'Cheyenne', 576851, 'Indian Paintbrush',
url +"primary-images/indianpaintbrushWYflower.jpg"] )

state_list.sort()#Sorts the list in an ascending order.

#====END OF STATES LIST====#

def table_header():
    """
    Header of the table.
    Returns
    -------
    None.

    """
    print("{:<20} {:<20} {:<20} {:<20}".format("State",
                                               "Capital",
                                               "Population",
                                               "Flower"))

def state_info(i):
    """

    Parameters
    ----------
    i : integer
        The number of loops taken.

    Returns
    -------
    None.

    """
    print("{:<20} {:<20} {:<20} {:<20}".format(state_list[i][0],
                                               state_list[i][1],
                                               state_list[i][2],
                                               state_list[i][3]))

def clear():
    """
    Used to clear the console to prevent clutter.
    Returns
    -------
    None.

    """
    os.system('cls')

def display_states():
    """
    Method used to display the states in a table format.
    Returns
    -------
    None.

    """
    table_header()
    for i, value in enumerate(state_list):#Run through length of state_list.
        state_info(i)#Display state info.
    print("\n")


def search_states():
    """

    Parameters
    ----------
    state_name : string
        The name of the states
    """
    state_isfound = False #Check to see if the state searched is found.
    
    while not state_isfound:
        state_name = input("Enter a state to search: ")

        for i, value in enumerate(state_list):#Run through the length of the list.
            #Compare searched value with the state that i is currently at.
            if state_name.lower() == (state_list[i][0].lower()):

                flower_image_link = state_list[i][4].replace(" ", '')#Get flower image.
                response = requests.get(flower_image_link)
                flower_image = Image.open(BytesIO(response.content))
                table_header()
                state_info(i)#Display state info.
                print("\n")
                flower_image.show()#Display image of the flower.
                state_isfound = True

        if not state_isfound:
            print("\nInvalid input! Please use the full name of a state.\n")

def population_graph():
    """
    Grab population and state name. Sort the population by highest to lowest.
    Display the top 5 and chart it into a bar graph.
    Returns
    -------
    None.

    """
    population_data = []#List for population information per state.

    for i, value in enumerate(state_list):
        population_data.append([-int(state_list[i][2]), state_list[i][0]])

    population_data.sort()#Sort the population data in an ascending order.

    top5_state = []
    top5_population = []
    num = min(len(population_data), 5)#n = minimum of 5 from the length of the list.

   #Take the sorted population list and separate the data into 2 separate lsits.

    for i in range(num):
        top5_population.append(-population_data[i][0])#Get population number.
        top5_state.append(population_data[i][1])#Get state name.
        i += 1

    #Plot and display the bar graph
    plot.xlabel('State')
    plot.ylabel('Population')
    plot.title('Top 5 Population States')
    plot.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.6)
    plot.bar(top5_state, top5_population)
    plot.show()


def update_population():
    """
    Update the population with the value from user input.

    Parameters
    ----------
    state_name : String
        Name of the state given by user.
    population : int
        Updated population number given by user.

    Returns
    -------
    state_isfound : boolean
        Determines that state searched for has been found.

    """
    state_isfound = False
    population_isvalid = False
    while not state_isfound:
        state_name = input("Enter the state name you wish to update population: ")
        
        for i, value in enumerate(state_list):
            if state_name.lower() == (state_list[i][0].lower()):
                while not population_isvalid:
                    try:
                        population = int(input("Enter the new population value: "))
                        if population < 0:
                            print("\nPopulation cannot be a negative number!\n")
                        else:
                            population_isvalid = True
                    except ValueError:
                        print("\nPopulation must be a whole number.\n")

                state_list[i][2] = population #Update the population to the value entered by user.
                state_isfound = True
                
        if not state_isfound:
            print("\nInvalid input! Please use the full name of a state.\n")
        


def main_menu():
    """
    Displays the menu for selection options.
    Returns
    -------
    None.

    """
    print("(1) Display all States.")
    print("(2) Search.")
    print("(3) Display Population Graph.")
    print("(4) Update State Population.")
    print("(5) Exit")
    print("\n")

def menu_selection():
    """
    Allows the user to input a selection from the main menu. It then
    runs the method of choice.
    Returns
    -------
    None.

    """
    selection = '0'#Set default value to go through while loop.

    while selection != '5':#If not told to exit, then just repeat
        main_menu()#Show menu then ask for input
        selection= input("Enter a corresponding numerical menu item: ")

        if selection == '1':
            clear()
            display_states()

        elif selection == '2':
            clear()
            search_states()

        elif selection == '3':
            clear()
            population_graph()

        elif selection == '4':
            clear()
            update_population()

        elif selection == '5':
            clear()
            exit_msg()

        else:
            clear()
            print("\nInvalid response! Please try again")#Back to top.

def exit_msg():
    """
    Message to exit the program.
    Returns
    -------
    None.

    """
    clear()
    print("Thank You for using the program goodbye.")
    input("Press ENTER to exit the program.")

def main():
    """
    Used for running the program. I like main because its used for other langs.
    Returns
    -------
    None.

    """
    menu_selection()

main()#Run
