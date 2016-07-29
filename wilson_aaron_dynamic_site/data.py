# !/usr/bin/env python
# -*- coding: utf-8 -*-

# WDD Degree Program
# Course: DPW
# Student: Aaron Wilson
# Student ID: 0004619821
# Assignment: Project 4 - Dynamic Site: data.py
# Date: July 25, 2016

# citation information:
# All player information from http://www.usatoday.com.


# Defines a new SuperClass called Player() to which sets forth the attributes to be used by its subclasses below.
class Player(object):

    # This is the __init__ method to initiate all the below attributes for the Player() class.
    def __init__(self):
        self.id = 0  # This is the player's dynamic page ID number.
        self.team = ""  # The team for which the player was drafted.
        self.first = ""  # The first name of the player.
        self.last = ""  # The last name of the player.
        self.contract = 0  # The player's current contract.
        self.img = ""  # The url path to the player's image.
        self.jerseys = []  # An array to show all player jerseys.
        self.total_shoes = 0  # Amount of shoes after calculation.
        self.information = ""  # A paragraph about the Automobile.


# Defines a new SubClass called Data() to which inherits the attributes of the Automobile() class.
class Data(object):

    # This is the __init__ method to initiate all the below attributes for the Data() class.
    def __init__(self):

        # Ben Simmons data type content. The "total_shoes" attribute for each player are accurate formulas.
        self.simmons = Player()
        self.simmons.id = 1
        self.simmons.team = "<p id='team_simmons'>Sixers</p>"
        self.simmons.first = "<p id='first_simmons'>Ben</p>"
        self.simmons.last = "<p id='last_simmons'>Simmons</p>"
        self.simmons.contract = 4919300
        self.simmons.total_shoes = self.simmons.contract / 175
        self.simmons.img = "images/simmons.png"
        self.simmons.jerseys = ["simmons_white", "simmons_blue", "simmons_red"]
        self.simmons.information = '''
<span id="simmons_info">Ben Simmons has as much upside as anyone in the draft, and he could wind up a perennial All-Star, but there were legitimate questions about his leadership at LSU. The last time the 76ers had the No. 1 pick they took Allen Iverson. That worked out pretty well. Trust the process, as they say.<br /><br /><br /><br /><br />
</span>
'''

        # Brandon Ingram data type content.
        self.ingram = Player()
        self.ingram.id = 2
        self.ingram.team = "<p id='team_ingram'>Lakers</p>"
        self.ingram.first = "<p id='first_ingram'>Brandon</p>"
        self.ingram.last = "<p id='last_ingram'>Ingram</p>"
        self.ingram.contract = 4401400
        self.ingram.total_shoes = self.ingram.contract / 175
        self.ingram.img = "images/ingram.png"
        self.ingram.jerseys = ["ingram_white", "ingram_yellow", "ingram_purple"]
        self.ingram.information = '''
<span id="ingram_info">Standing at 6-10 with a 7-3 wingspan, the athletically gifted 18-year-old has drawn Kevin Durant comparisons since appearing in the national spotlight during his lone season at Duke. He has all of the tools necessary to become an All-NBA talent, and if he adds some muscle to his sub-200 pound frame, he could just be the next franchise player in Los Angeles.</span>
'''

        # Buddy Hield data type content.
        self.hield = Player()
        self.hield.id = 3
        self.hield.team = "<p id='team_hield'>Pelicans</p>"
        self.hield.first = "<p id='first_hield'>Buddy</p>"
        self.hield.last = "<p id='last_hield'>Hield</p>"
        self.hield.contract = 2931000
        self.hield.total_shoes = self.hield.contract / 175
        self.hield.img = "images/hield.png"
        self.hield.jerseys = ["hield_white", "hield_blue", "hield_red"]
        self.hield.information = '''
<span id="hield_info">Hield was the one of the best players in all of college basketball last season, but now comes a whole new test. He's a knock down shooter who can spread the floor for All-Star forward Anthony Davis, and his year-by-year improvements at Oklahoma are encouraging, but — behind guys like Eric Gordon, Tyrke Evans and Jrue Holiday — is he enough of an all-around talent to make an immediate impact for the lowly Pelicans?</span>
'''

        # Kris Dunn data type content.
        self.dunn = Player()
        self.dunn.id = 4
        self.dunn.team = "<p id='team_dunn'>Timberwolves</p>"
        self.dunn.first = "<p id='first_dunn'>Kris</p>"
        self.dunn.last = "<p id='last_dunn'>Dunn</p>"
        self.dunn.contract = 3227100
        self.dunn.total_shoes = self.dunn.contract / 175
        self.dunn.img = "images/dunn.png"
        self.dunn.jerseys = ["dunn_white", "dunn_blue", "dunn_black"]
        self.dunn.information = '''
<span id="dunn_info">There might not be a better fit than Dunn in Minnesota under first-year coach Tom Thibodeau. Dunn is a versatile, powerful combo guard who will mesh perfectly with Andrew Wiggins on the wing. He was a two-time Big East Player of the Year and was also the two-time Big East Defensive Player of the Year. His effort on defense no doubt caught Thibodeau's eye.</span>

'''

        # Jamal Murray data type content.
        self.murray = Player()
        self.murray.id = 5
        self.murray.team = "<p id='team_murray'>Nuggets</p>"
        self.murray.first = "<p id='first_murray'>Jamal</p>"
        self.murray.last = "<p id='last_murray'>Murray</p>"
        self.murray.contract = 2675700
        self.murray.total_shoes = self.murray.contract / 175
        self.murray.img = "images/murray.png"
        self.murray.jerseys = ["murray_white", "murray_blue", "murray_yellow"]
        self.murray.information = '''
<span id="murray_info">The Nuggets were one of the worst three-point shooting teams in the NBA last season, and Murray's outside shot immediately improves their perimeter game. He's an NBA-ready offensive player, no doubt, but questions persist about his athleticism and defense. Regardless, the Nuggets took the best talent available.</span>

'''

        # Jaylen Brown data type content.
        self.brown = Player()
        self.brown.id = 6
        self.brown.team = "<p id='team_brown'>Celtics</p>"
        self.brown.first = "<p id='first_brown'>Jaylen</p>"
        self.brown.last = "<p id='last_brown'>Brown</p>"
        self.brown.contract = 3952500
        self.brown.total_shoes = self.brown.contract / 175
        self.brown.img = "images/brown.png"
        self.brown.jerseys = ["brown_white", "brown_green", "brown_gray"]
        self.brown.information = '''
<span id="brown_info">The Celtics owned what was arguably the most coveted pick in the draft, and they used it on one of the most athletic frontcourt players available. Despite rumors that the Celtics were shopping the pick to the 76ers and the Chicago Bulls, they took Brown, who provides elite athleticism on the wing. He could also fit perfectly with Brad Stevens' defensive schemes. </span>

'''
