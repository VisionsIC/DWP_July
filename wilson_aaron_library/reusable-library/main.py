"""
WDD Degree Program
Course: DPW
Student: Aaron Wilson
Student ID: 0004619821
Assignment: Project 3 - Reusable Library - main.py
May 18, 2016
"""

import webapp2
from library import PatientData, PatientToolbox
from pages import BrowserPage, DynamicOutput


# Creates multiple instances of all the imported classes listed above.
class MainHandler(webapp2.RequestHandler):

    # This GET function allows for the ability to compile and pull data to any area of the app that is specified.
    def get(self):

        # Store variable gives access to the PatientToolbox class.
        store = PatientToolbox()

        # Build instances of usable patient data to create utilities.
        pt_01 = PatientData()  # Pre-compiled info for patient 1 (pt_01) from the PatientType class data.
        pt_01.first_name = 'Barry'  # Pre-compiled patient 1 (pt_01) first name data.
        pt_01.last_name = 'Welsch'  # Pre-compiled patient 1 (pt_01) last name data.
        pt_01.gender = 'Male'  # Pre-compiled patient 1 (pt_01) gender data.
        pt_01.age = 34  # Pre-compiled patient 1 (pt_01) age data.
        pt_01.height = '76' # Pre-compiled patient 1 (pt_01) height data.
        pt_01.weight = '255' # Pre-compiled patient 1 (pt_01) weight data.
        pt_01.diagnosis = 'Quadriplegic'  # Pre-compiled patient 1 (pt_01) diagnosis data.
        store.add_patient(pt_01)  # Store this data to the "patient_list" array.

        # Build instances of usable patient data to create utilities.
        pt_02 = PatientData()  # Pre-compiled info for patient 2 (pt_02) from the PatientType class data.
        pt_02.first_name = 'Robin'  # Pre-compiled patient 2 (pt_02) first name data.
        pt_02.last_name = 'Teague'  # Pre-compiled patient 2 (pt_02) last name data.
        pt_02.gender = 'Female'  # Pre-compiled patient 2 (pt_02) gender data.
        pt_02.age = 25  # Pre-compiled patient 2 (pt_02) age data.
        pt_02.height = '64' # Pre-compiled patient 2 (pt_02) height data.
        pt_02.weight = '150' # Pre-compiled patient 2 (pt_02) weight data.
        pt_02.diagnosis = 'Paraplegic'  # Pre-compiled patient 2 (pt_02) diagnosis data.
        store.add_patient(pt_02)  # Store this data to the "patient_list" array.

        # This IF statement allows for the ability to utilize the forms and dropdowns on the HTML page to retrieve the
        # necessary input information below by way of their "value" attribute in the HTML.
        if self.request.GET:
            pt_03 = PatientData()
            pt_03.first_name = self.request.GET['first_name']
            pt_03.last_name = self.request.GET['last_name']
            pt_03.gender = self.request.GET['gender']
            pt_03.age = self.request.GET['age']
            pt_03.height = self.request.GET['height']
            pt_03.weight = self.request.GET['weight']
            pt_03.diagnosis = self.request.GET['diagnosis']
            store.add_patient(pt_03)

            # The "dynamic" variable gives access to GET data from the DynamicOutput Class to dynamically add-in the
            # below properties to the HTML output portion of pages.py
            dynamic = DynamicOutput()
            dynamic.title_tag = 'Welcome To The Patient Wheelchair Request Form'
            dynamic.css_file = 'css/styles.css'
            dynamic.js_file = 'js/validation.js'

            # Another variable "tb_output" gives access to GET data from the PatientToolbox Class to dynamically add-in
            # the below "output_list" function and array to the HTML output portion of pages.py
            tb_output = store.output_list()

            # Call methods to produce a functional HTML page to the browser.
            self.response.write(dynamic.dynamic_output(tb_output))

        # An ELSE statement adds a condition to tell app to output the below instructions.
        else:

            # These are the instructed conditions made up of the "" variable. EX. Use BrowserPage class to GET these
            # attributes and inject them into the assigned HTML tags.
            default = BrowserPage()
            default.title_tag = 'Welcome To The Patient Wheelchair Request Form'
            default.css_file = 'css/styles.css'
            default.h1_title = 'Patient Wheelchair Request Form'
            default.js_file = 'js/validation.js'

            # The below methods call for the final write to the page.
            self.response.write(default.default_output())

# Below code is prebuilt for functionality with GAE. Not to be removed!!!
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
