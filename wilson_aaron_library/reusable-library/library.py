"""
WDD Degree Program
Course: DPW
Student: Aaron Wilson
Student ID: 0004619821
Assignment: Project 3 - Reusable Library - library.py
July 19, 2016
"""


# create a class called "PatientData" and add the attributes.
class PatientData(object):

    # Create the __init__ method to use the below attributes.
    def __init__(self):

        # Create all the python attributes needed to make up multiple aspects of the form.
        self.first_name = ''
        self.last_name = ''
        self.gender = ''
        self.__age = 0
        self.__height = ''
        self.__weight = ''
        self.__diagnosis = ''

    # Getters and setters for the "__age", and "__diagnosis" attribute of the "PatientData()" class.
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):

        # Convert height attribute (by default a string) to an integer for proper use in the IF statement.
        height = int(height)

        # Use the IF conditional to make use of a comparison operator to produce the appropriate outcome.
        if height > 47:
            height = 16
        elif height < 68:
            height = 16
        elif height > 68:
            height = 18
        elif height < 74:
            height = 18
        elif height > 74:
            height = 20
        elif height < 79:
            height = 20
        elif height > 79:
            height = 22
        elif height < 85:
            height = 22

        else:
            height = str("unknown height")

        self.__height = str(height)

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):

        # Convert weight attribute (by default a string) to an integer for proper use in the IF statement.
        weight = int(weight)

        # Use the IF conditional to make use of a comparison operator to produce the appropriate outcome.
        if weight > 50:
            weight = 16
        elif weight < 110:
            weight = 16
        elif weight > 110:
            weight = 18
        elif weight < 220:
            weight = 18
        elif weight > 220:
            weight = 20
        elif weight < 280:
            weight = 20
        elif weight > 280:
            weight = 22
        elif weight < 350:
            weight = 22

        else:
            weight = str("unknown weight")

        self.__weight = str(weight)

    @property
    def diagnosis(self):
        return self.__diagnosis

    @diagnosis.setter
    def diagnosis(self, diagnosis):
        self.__diagnosis = diagnosis


# create a class called "PatientToolbox" and add the attributes.
class PatientToolbox(PatientData):

    # Create an __init__ function to hold key arrays and other methods to make PatientToolbox class work.
    def __init__(self):
        PatientData.__init__(self)

        self.age = 0
        self.__height = ''
        self.__weight = ''

        # Build an array to store patient information data.
        self.__patient_list = []

    # Function to append whole patient list to the library.
    def add_patient(self, patient):

        # This bit of python code "appends" a new patient to the patient_list array.
        self.__patient_list.append(patient)

    # Function to loop through all patients in the list, format, and return for outputting in HTML.
    def output_list(self):

        # Initializing empty string for use below.
        patient_data = ''

        # For each patient in the "patient_list".
        for patient in self.__patient_list:

            # Comment.
            patient_data += '<div id="patient_wrap"><div id="pat_info"><h2 class="string_out"> Patient(s) Name:  ' + patient.first_name + ' ' + patient.last_name + '</h2><h2 class="string_out" >Gender:  ' + patient.gender + '</h2><h2 class="string_out">Age:  ' + str(patient.age) + '</h2><h2 class="string_out">Diagnosis:  ' + patient.diagnosis + '</h2></div><h2 class="string_out"><br /><br />The recommended wheelchair<br /><br /><br />dimensions for this patient are: <br /><br /><br /><br /><bold>' + patient.height + ' X ' + patient.weight + '</bold></h2><div class="img_out"><img class="inside_img" src="images/wc/' + patient.diagnosis + '.png"/ ></div></div>'

        # return the output of patient_data variable that outputs a data string to DynamicOutput class, HTML portion of
        # that class.
        return patient_data

    # Getters and setters for the "__patient_list", and "__diagnosis" attribute of the "PatientToolbox()" class.
    @property
    def patient_list(self):
        return self.__patient_list

    @patient_list.setter
    def patient_list(self, patient):
        self.__patient_list = patient
