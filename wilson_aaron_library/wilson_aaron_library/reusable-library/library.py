"""
WDD Degree Program
Course: DPW
Student: Aaron Wilson
Student ID: 0004619821
Assignment: Project 3 - Reusable Library - library.py
May 18, 2016
"""


# create a class called "PatientData" and add the attributes.
class PatientData(object):

    # Comment.
    def __init__(self, patient_toolbox):

        # Comment.
        self.first_name = ''
        self.last_name = ''
        self.gender = ''
        self.__age = 0

        # Comment.
        self.__patient_toolbox = PatientToolbox()

        # Comment.
        patient_toolbox.__height = ''
        patient_toolbox.__weight = ''

        # Comment
        self.__diagnosis = ''

    # Getters and setters for the "__age", and "__diagnosis" attribute of the "PatientData()" class.
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def patient_toolbox(self):
        return self.__patient_toolbox

    @patient_toolbox.setter
    def patient_toolbox(self, patient_toolbox):
        self.__patient_toolbox = patient_toolbox

    @property
    def diagnosis(self):
        return self.__diagnosis

    @diagnosis.setter
    def diagnosis(self, diagnosis):
        self.__diagnosis = diagnosis


# create a class called "PatientToolbox" and add the attributes.
class PatientToolbox(object):

    # Create an __init__ function to hold key arrays and other methods to make PatientToolbox class work.
    def __init__(self):

        self.__height = ''
        self.__weight = ''

        # Build an array to store patient information data.
        self.__patient_list = []

    # Added class method "pat_height" so that the below functions can be properly used by the class.
    @classmethod
    def pat_height(cls, height):

        # Change the height variable into an integer to be processed in the conditional below.
        height = int(height)

        # IF and ELIF Conditionals for "pat_height" function that compare a patient's height to determine the proper wheelchair size.
        if height >= 47:
            return 16
        elif height <= 68:
            return 16
        elif height >= 68:
            return 18
        elif height <= 74:
            return 18
        elif height >= 74:
            return 20
        elif height <= 79:
            return 20
        elif height >= 79:
            return 22
        elif height <= 85:
            return 22

    # Pat_height method will output the appropriate wheelchair width based upon the patients height.
    pat_height = pat_height(height=0)

    # Added class method "pat_weight" so that the below functions can be properly used by the class.
    @classmethod
    def pat_weight(cls, weight):

        # Change the weight variable into an integer to be processed in the conditional below.
        weight = int(weight)

        # IF and ELIF Conditionals for "pat_weight" function that compare a patient's weight to determine the proper wheelchair size.
        if weight >= 50:
            return 16
        elif weight <= 110:
            return 16
        elif weight >= 110:
            return 18
        elif weight <= 220:
            return 18
        elif weight >= 220:
            return 20
        elif weight <= 280:
            return 20
        elif weight >= 280:
            return 22
        elif weight <= 350:
            return 22

    # Pat_weight method will output the appropriate wheelchair width based upon the patients weight.
    pat_weight = pat_weight(weight=0)

    # Added class method "wc_dimensions" so that the below functions can be properly used by the class.
    @classmethod
    def wc_dimensions(cls, pat_height, pat_weight):

        # The function "calc_dimensions" returns a string to be injected into the "patient_data" string below.
        calc_dimensions = 'The recommended wheelchair dimensions for this patient are:' + str(pat_height) + ' X ' + str(
            pat_weight)
        return calc_dimensions

    wc_dimensions = wc_dimensions(pat_height='', pat_weight='')

    # Function to append whole patient list to the library.
    def add_patient(self, patient):

        # This bit of python code "appends" a new patient to the patient_list array.
        self.__patient_list.append(patient)

    # Function to loop through all patients in the list, format, and return for outputting in HTML.
    def output_list(self, wc_dimensions):

        # Initializing empty string for use below.
        patient_data = ''

        # For each patient in the "patient_list".
        for patient in self.__patient_list:

            # This is the patient data string to output to the self.dynamic_data section on pages.py.
            patient_data += '<div id="patient_wrap"><div id="pat_info"><h2 class="string_out"> Patient(s) Name:  ' + patient.first_name + ' ' + patient.last_name + '</h2><h2 class="string_out"></h2><h2 class="string_out" >Gender:  ' + patient.gender + '</h2><h2 class="string_out">Age:  ' + str(patient.age) + '</h2><h2 class="string_out">' + wc_dimensions + '</h2><h2 class="string_out">Diagnosis:  ' + patient.diagnosis + '</h2></div><div class="img_out"><img class="inside_img" src="images/wc/' + patient.diagnosis + '.png"/ ></div></div>'

        # return the output of patient_data variable that outputs a data string to DynamicOutput class, HTML portion of
        # that class.
        return patient_data

    # Getters and setters for the "__patient_list", and "__diagnosis" attribute of the "PatientToolbox()" class.
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def patient_list(self):
        return self.__patient_list

    @patient_list.setter
    def patient_list(self, patient):
        self.__patient_list = patient
