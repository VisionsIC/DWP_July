##############################################
# WDD Degree Program                         #
# Course: DPW                                #
# Student: Aaron Wilson                      #
# Student ID: 0004619821                     #
# Assignment: Project 1 - Madlib : main.py   #
# Date: June 29, 2016                        #
##############################################

######################################################################################################################

#  PERSONAL DISCLAIMER - I ATTEST THAT ALL CODE BELOW IS MY OWN; IF IN FACT THERE IS CODE THAT APPEARS SIMILAR TO CODE
#  FOUND ONLINE, IT IS OUT OF PURE COINCIDENTAL SIMILARITY.

######################################################################################################################

#  Create a dictionary to hold attributes or characteristics of a subject in the story that a user may enter.
story = dict()
#  Create the variables that will be injected into the story (some input, most raw input).

#  Below are all the KEY variables appended to the story dictionary.
story['my_name'] = raw_input("Please enter your first name:  ")
story['year_picked'] = raw_input("Enter a favorite year:  ")
story['tens_number'] = raw_input("Enter a number in increments of 10 (ex. 10, 20):  ")
story['emotions'] = input("Enter a number between 0 and 5: ")
story['adjective'] = raw_input("Enter an adjective ending in LY:  ")
story['act_verb'] = raw_input("Enter an action verb ending in ING:  ")
story['second_act_verb'] = raw_input("Enter another action verb ending in ING:  ")
story['third_act_verb'] = raw_input("Enter yet another action verb ending in ING:  ")
story['pet'] = raw_input("Enter the pet animal you have, or if none, you would have:  ")
story['pet_num'] = raw_input("How many pets do you have? :  ")
story['disaster'] = raw_input("Enter a natural element; (fire, wind, water, earth, or mountains):  ")
story['plural_act_verb'] = raw_input("Enter your final action verb ending in ING:  ")
story['verbal_emotion'] = raw_input("Enter a verbal emotion (ex. yell, scream):  ")
story['gathering_type'] = raw_input("Enter a gathering of sorts you enjoy attending; (ex. party, banquet):  ")
story['feeling'] = raw_input("Enter a raw feeling to which engages you; (ex. grief, anxiety):  ")

# This next section of code are the Conditionals -

#  This conditional below adds a random year, picked by the user, to get a year in the future by adding the two numbers.

#  Story['year_picked'] is a string, so we need to convert it to an integer so we can add it by 50.
#  This is accomplished by adding the int() method.
random_year = int(story['year_picked']) + 50

#  An array called # EMOTIONS # to create an emotion wheel than when a number is picked it outputs an emotion into the
#  story dict.
emotions = ["panic", "fear", "hysteria", "despair", "uncertainty"]

#  if statement tells the data variable if the EMOTIONS integer is grater than 6, then it IS 6.
if story['emotions'] > 5:
    story['emotions'] = 5

#  if statement tells the data variable if the EMOTIONS integer is less than 1, then it IS 1.
elif story['emotions'] < 0:
    story['emotions'] = 0

#  Incorporate EMOTIONS variable by inserting the STORY variable with the attribute name FEELING to the string.
emotions.insert(0, str(story['feeling']))
#  Loop through emotions variable by inserting it into an blank array
blank_array = []

#  Command a for loop within the "range" of each if statement in the conditionals coded above.
for index in range(story['emotions']):
    #  opens this array and appends a string to the emotions attribute
    blank_array.append(str(emotions[index]))

#  Create EMOTION TYPE variable which is an empty string and open to further injection of conditional functionality.
emotion_type = ""

#  the below for loop inserts the character variable in that "blank_array" variable above, the line of code below that
#  concatenates the character_group variable to equal itself plus character and a grammatical string.
for emotion in blank_array:
    emotion_type = emotion_type + emotion + ", "

#  A List called # INTRUDERS # that has values and keys of intruder types.
nature = {"fire": "Inferno", "wind": "Tornado", "water": "Tsunami", "earth": "Earthquake", "mountain": "Volcano"}

#  Also, I'll create a variable called # SENSE # to eliminate code redundancy.
disaster = story['disaster']

#  Another conditional that loops through using disaster
if disaster in nature:
    add_nature = (nature[disaster] + "s")

#  No indent spacing halts the if statement.

'''
The function below figures out the amount of nature there will be attacking in the story by implementing an equation,
the variable is a string that needs conversion to an integer using int()
'''

#  Create the TENS NUMBER variable to store the 'tens_number' raw_input to minimize code bloat.
tens_number = story['tens_number']


#  Define the method CATASTROPHE AMOUNT that uses TENS NUMBER as an attribute to return the appropriate computation.
def catastrophe_amount(tens_number):

    #  Create a variable called AMOUNT to convert the TENS NUMBER variable to an integer for calculation of AMOUNT.
    amount = int(tens_number) % 2 * 5000
    return amount

#  This is where the catastrophe variable is used to invoke the catastrophe amount method.
catastrophe = catastrophe_amount(tens_number)

#  Invoke the catastrophe amount and show its depicted by its amount with IF and ELSE statements to output a result.
if catastrophe > 25000:
    disaster_amount = "massive band"
else:
    disaster_amount = "small cluster"


#  Print to the screen the story by putting together all the variables, functions, dictionaries, and methods to produce
# a result.

print "\n""\n""\n" " Nature Vs. Humanity: The Battle For Earth" "\n" "By Aaron Wilson" "\n" "\n" "In the wake of increased chatter on the communication super-highway, " + story['my_name'] + " listened very intently at what message was being " "\n" "delivered. In the year " + str(random_year) + ", societal breakdown was beginning to happen due to " + story['feeling'] + " of what was to come..." "\n" + story['my_name'] + " was both anxious, yet determined to continue " + story['adjective'] + " through these trying times. Coming from a hard-nosed,""\n"" blue collar family; " + story['my_name'] + " was accustomed to " + story['second_act_verb'] + " through it and come together to protect the very place his " "\n" " family called home.  Suddenly, In the distance, " + story['my_name'] + " could see a " + disaster_amount + " of " + add_nature + " were " + story['third_act_verb'] + ", and barreling down" "\n" " upon " + story['my_name'] + "'s beloved homeland! " "\n" "\n" + story['my_name'] + " knew this would be the event of a lifetime. Without much time to spare, " + story['my_name'] + " jumped on the " + story['pet'] + " and had " "\n" " to quickly retreat. Now came strength in numbers, to where " + str(story['pet_num']) + " other " + story['pet'] + "s were ready to join the great battle to save humanity from " "\n" " nature's wrath! The " + add_nature + " were " + story['plural_act_verb'] + " in, so with no haste " + story['my_name'] + " turned around and vowed to fight" "\n" "TO THE END! " + story['my_name'] + " began to " + story['verbal_emotion'] + " out... We are told that life is a " + story['gathering_type'] + ", sometimes you just have to go out " + story['act_verb'] + "!" "\n" "\n" "\n"  " THE END"
