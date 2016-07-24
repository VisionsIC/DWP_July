###
#  WDD Degree Program
#  Course: DPW
#  Student: Aaron Wilson
#  Student ID: 0004619821
#  Assignment: Project 2: Simple Form - main.py
#  Date: July 04, 2016
###

# Import and make use of this webapp2 library.
import webapp2

# Import and make use of "all" the available classes by way of the "*" as a wildcard.
from page import *


# Create Class MainHandler to use the webapp2 library.
class MainHandler(webapp2.RequestHandler):

    # Comment
    def get(self):

        # Creates an instance of the imported class Page.
        page = Page()
        form = Form()

        # if there is a URL variable then print this
        self.response.write(page.begin_page())

        # With a GET array, the IF statement creates a condition which requests to GET each of the variables to be
        # submitted to the simple form, and print out the data to the page.
        if self.request.GET:

            # These variables listed below help get the form inputs, by user choice, delivering the form response.
            first_name = self.request.GET["firstName"]
            last_name = self.request.GET["lastName"]
            gender = self.request.GET["gender"]
            birth_day = self.request.GET["birthday"]
            birth_month = self.request.GET["birthmonth"]
            birth_year = self.request.GET["birthyear"]

            # get_all compiles a working list from "shoe_item" and is stored to the "shoe_list" variable.
            shoe_list = self.request.get_all("shoe_item")

            # separates the list by using <br><p> so that it injects itself inside the "output" variable.
            shoe_choice = '''<br><p>'''.join(shoe_list)

            # The "output" variable houses the the required HTML tags to be send to the browser page.
            output = '''<div id="main_output">
                            <fieldset id="output_fs">
                                <div class="output_div">
                                    <div id="blue_bar"></div>
                                    <header id="output_hdr">
                                        <h1>Thank You, {first_name} {last_name}!</h1><br />
                                    </header>
                                </div>
                                <div id="info_output">
                                    <br />
                                    <h1>Please review your information below:</h1><br /><br />
                                    <h2>Customer: {first_name} {last_name}</h2><br />
                                    <h2>Gender: {gender}</h2><br />
                                    <h2>Date Of Birth: {birth_month}/{birth_day}/{birth_year}</h2><br />
                                </div>
                                <div id="choices_output">
                                    <br />
                                    <h1>Here are your Shoeshine Boy shoe choices:</h1><br /><br />
                                    <h2 id="shoe_choices">{shoe_choice}</h2>
                                </div>
                                <footer id="output_ftr">
                                    <h2>&copy; 2016 Shoeshine Boy | A fictitious company for use as an assignment | FULL SAIL UNIVERSITY</h2>
                                </footer>
                        </div>'''

            # Output variable strings the "output" variable with the "local" variables to output all user pre-selected
            # choices.
            output = output.format(**locals())

            # This self response writes the "output" variable within the GET array to output to the form in the browser.
            self.response.write(output)

        # Else, if form isn't submitted, display initial prior output state of the form.
        else:

            # Write all "form" output to the "Form" class in the "form HTML" tags on the browser page.
            self.response.write(form.begin_form())
            # Write all closing "page" output to the "Page" class in the form of HTML to the browser page.
            self.response.write(page.close_page())


# This piece of code is the code that works with the google app engine!
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
