
# WDD Degree Program
# Course: DPW
# Student: Aaron Wilson
# Student ID: 0004619821
# Assignment: Project 4 - Dynamic Site: main.py
# Date: July 25, 2016

# Import the webapp2 library.
import webapp2

# Import ContentPage class.
from pages import ContentPage

# Imports the Data Class.
from data import Data


# MainHandler Class.
class MainHandler(webapp2.RequestHandler):
    def get(self):

        # Instantiate the ContentPage class.
        cpc = ContentPage()

        # Instantiate the Data class.
        doc = Data()

        # IF a button below is clicked then GET:
        if self.request.GET:

            # IF the id is equal to 0; GET this "Home" page, dynamically.
            if self.request.GET['id'] == "0":

                # Manipulation of the "Home" HTML title_tag tag.
                cpc.title_tag = "NBA's Next Class | Home"

                # Display "Home" information to the "body_tag" content area of the dynamic page.

                # Opening HTML UL tag.
                cpc.body_tag += cpc.begin_ul

                # Incorporate navigation buttons for this "Home" dynamic page to the UL tag.
                cpc.body_tag += cpc.build_nav_button("?id=1", "Ben Simmons")
                cpc.body_tag += cpc.build_nav_button("?id=2", "Brandon Ingram")
                cpc.body_tag += cpc.build_nav_button("?id=3", "Buddy Hield")
                cpc.body_tag += cpc.build_nav_button("?id=4", "Kris Dunn")
                cpc.body_tag += cpc.build_nav_button("?id=5", "Jamal Murray")
                cpc.body_tag += cpc.build_nav_button("?id=6", "Jaylen Brown")

                # Closing HTML UL tag.
                cpc.body_tag += cpc.end_ul

                # Home page information HTML tags consisting of H1 and p tags.
                cpc.body_tag += "<h1 id='home_h1'>NBA's Future Stars!</h1>\n"
                cpc.body_tag += "<p id='home_p1'>This web page is dedicated to the basketball fans that share the excitement to see all the future talent of today!</p>\n"
                cpc.body_tag += "<p id='home_p2'>If you follow the links above, you'll enjoy all the wonderful information on each of these future stars.</p>\n"

                # GET the associated image for the "Home" dynamic page.
                cpc.body_tag += cpc.add_image("/images/index.png", "Awesome Chevy Background Image")

                # Write "Home" dynamic HTML page.
                self.response.write(cpc.build_markup())

            # IF the id is equal to 1; GET this "Simmons" page, dynamically.
            elif self.request.GET["id"] == "1":

                # Use this variable to shorten up the "doc" Data() class with the attribute of "simmons".
                player = doc.simmons

                # Manipulation of the player "Simmons" HTML title_tag, tag.
                cpc.title_tag = "NBA's Next Class | " + player.last

                # Display "Ben Simmons" information to the "body_tag" content area of the dynamic page.

                # Opening HTML UL tag.
                cpc.body_tag += cpc.begin_ul

                # Incorporate navigation buttons for this player "Simmons" dynamic page to the UL tag.
                cpc.body_tag += cpc.build_nav_button("?id=0", "Home")
                cpc.body_tag += cpc.build_nav_button("?id=1", "Ben Simmons")
                cpc.body_tag += cpc.build_nav_button("?id=2", "Brandon Ingram")
                cpc.body_tag += cpc.build_nav_button("?id=3", "Buddy Hield")
                cpc.body_tag += cpc.build_nav_button("?id=4", "Kris Dunn")
                cpc.body_tag += cpc.build_nav_button("?id=5", "Jamal Murray")
                cpc.body_tag += cpc.build_nav_button("?id=6", "Jaylen Brown")

                # Closing HTML UL tag.
                cpc.body_tag += cpc.end_ul

                # Incorporate all the "Simmons" player "body_tag" dynamic content.
                cpc.body_tag += cpc.write_player_data(player)
                cpc.body_tag += cpc.write_player_jerseys(player)
                cpc.body_tag += cpc.write_content(player)

                # Close this section of the dynamic HTML page.
                cpc.body_tag += cpc.end_section

                # Write player "Simmons" dynamic HTML page.
                self.response.write(cpc.build_markup())

            # IF the id is equal to 0; GET this player "Ingram" page, dynamically.
            elif self.request.GET["id"] == "2":

                # Use this variable to shorten up the "doc" Data() class with the attribute of "ingram".
                player = doc.ingram

                # Manipulation of the player "Ingram" HTML title_tag, tag.
                cpc.title_tag = "NBA's Next Class | " + player.last

                # Display "Brandon Ingram" information to the "body_tag" content area of the dynamic page.

                # Opening HTML UL tag.
                cpc.body_tag += cpc.begin_ul

                # Incorporate navigation buttons for this player "Ingram" dynamic page to the UL tag.
                cpc.body_tag += cpc.build_nav_button("?id=0", "Home")
                cpc.body_tag += cpc.build_nav_button("?id=1", "Ben Simmons")
                cpc.body_tag += cpc.build_nav_button("?id=2", "Brandon Ingram")
                cpc.body_tag += cpc.build_nav_button("?id=3", "Buddy Hield")
                cpc.body_tag += cpc.build_nav_button("?id=4", "Kris Dunn")
                cpc.body_tag += cpc.build_nav_button("?id=5", "Jamal Murray")
                cpc.body_tag += cpc.build_nav_button("?id=6", "Jaylen Brown")

                # Closing HTML UL tag.
                cpc.body_tag += cpc.end_ul

                # Incorporate all "Ingram" player "body_tag" dynamic content.
                cpc.body_tag += cpc.write_player_data(player)
                cpc.body_tag += cpc.write_player_jerseys(player)
                cpc.body_tag += cpc.write_content(player)

                # Close this section of the dynamic HTML page.
                cpc.body_tag += cpc.end_section

                # Write player "Ingram" dynamic HTML page.
                self.response.write(cpc.build_markup())

            # IF the id is equal to 3; GET this player "Hield" page, dynamically.
            elif self.request.GET["id"] == "3":

                # Use this variable to shorten up the "doc" Data() class with the attribute of player "Hield".
                player = doc.hield

                # Manipulation of the player "Hield" HTML title_tag, tag.
                cpc.title_tag = "NBA's Next Class | " + player.last

                # Display "Buddy Hield" information to the "body_tag" content area of the dynamic page.

                # Opening HTML UL tag.
                cpc.body_tag += cpc.begin_ul

                # Incorporate navigation buttons for this player "Hield" dynamic page to the UL tag.
                cpc.body_tag += cpc.build_nav_button("?id=0", "Home")
                cpc.body_tag += cpc.build_nav_button("?id=1", "Ben Simmons")
                cpc.body_tag += cpc.build_nav_button("?id=2", "Brandon Ingram")
                cpc.body_tag += cpc.build_nav_button("?id=3", "Buddy Hield")
                cpc.body_tag += cpc.build_nav_button("?id=4", "Kris Dunn")
                cpc.body_tag += cpc.build_nav_button("?id=5", "Jamal Murray")
                cpc.body_tag += cpc.build_nav_button("?id=6", "Jaylen Brown")

                # Closing HTML UL tag.
                cpc.body_tag += cpc.end_ul

                # Incorporate all "Hield" player "body_tag" dynamic content.
                cpc.body_tag += cpc.write_player_data(player)
                cpc.body_tag += cpc.write_player_jerseys(player)
                cpc.body_tag += cpc.write_content(player)

                # Close this section of the dynamic HTML page.
                cpc.body_tag += cpc.end_section

                # Write player "Hield" dynamic HTML page.
                self.response.write(cpc.build_markup())

            # IF the id is equal to 4; GET this "Dunn" page, dynamically.
            elif self.request.GET["id"] == "4":

                # Use this variable to shorten up the "doc" Data() class with the attribute of "Dunn".
                player = doc.dunn

                # Manipulation of the "Dunn" HTML title_tag tag.
                cpc.title_tag = "NBA's Next Class | " + player.last

                # Display "Kris Dunn" information to the "body_tag" content area of the dynamic page.

                # Opening HTML UL tag.
                cpc.body_tag += cpc.begin_ul

                # Incorporate navigation buttons for this "Dunn" dynamic page to the UL tag.
                cpc.body_tag += cpc.build_nav_button("?id=0", "Home")
                cpc.body_tag += cpc.build_nav_button("?id=1", "Ben Simmons")
                cpc.body_tag += cpc.build_nav_button("?id=2", "Brandon Ingram")
                cpc.body_tag += cpc.build_nav_button("?id=3", "Buddy Hield")
                cpc.body_tag += cpc.build_nav_button("?id=4", "Kris Dunn")
                cpc.body_tag += cpc.build_nav_button("?id=5", "Jamal Murray")
                cpc.body_tag += cpc.build_nav_button("?id=6", "Jaylen Brown")

                # Closing HTML UL tag.
                cpc.body_tag += cpc.end_ul

                # Incorporate all "Dunn" player "body_tag" dynamic content.
                cpc.body_tag += cpc.write_player_data(player)
                cpc.body_tag += cpc.write_player_jerseys(player)
                cpc.body_tag += cpc.write_content(player)

                # Close this section of the dynamic HTML page.
                cpc.body_tag += cpc.end_section

                # Write "Dunn" dynamic HTML page.
                self.response.write(cpc.build_markup())

            # IF the id is equal to 5; GET this player "Murray" page, dynamically.
            elif self.request.GET["id"] == "5":

                # Use this variable to shorten up the "doc" Data() class with the attribute of player "Murray".
                player = doc.murray

                # Manipulation of the "Murray" HTML title_tag tag.
                cpc.title_tag = "NBA's Next Class | " + player.last

                # Display "Jamal Murray" information to the "body_tag" content area of the dynamic page.

                # Opening HTML UL tag.
                cpc.body_tag += cpc.begin_ul

                # Incorporate navigation buttons for this player "Murray" dynamic page to the UL tag.
                cpc.body_tag += cpc.build_nav_button("?id=0", "Home")
                cpc.body_tag += cpc.build_nav_button("?id=1", "Ben Simmons")
                cpc.body_tag += cpc.build_nav_button("?id=2", "Brandon Ingram")
                cpc.body_tag += cpc.build_nav_button("?id=3", "Buddy Hield")
                cpc.body_tag += cpc.build_nav_button("?id=4", "Kris Dunn")
                cpc.body_tag += cpc.build_nav_button("?id=5", "Jamal Murray")
                cpc.body_tag += cpc.build_nav_button("?id=6", "Jaylen Brown")

                # Closing HTML UL tag.
                cpc.body_tag += cpc.end_ul

                # Incorporate all player "Murray" automobile "body_tag" dynamic content.
                cpc.body_tag += cpc.write_player_data(player)
                cpc.body_tag += cpc.write_player_jerseys(player)
                cpc.body_tag += cpc.write_content(player)

                # Close this section of the dynamic HTML page.
                cpc.body_tag += cpc.end_section

                # Write player "Murray" dynamic HTML page.
                self.response.write(cpc.build_markup())

            # IF the id is equal to 6; GET this player "Brown" page, dynamically.
            elif self.request.GET["id"] == "6":

                # Use this variable to shorten up the "doc" Data() class with the attribute of "Brown".
                player = doc.brown

                # Manipulation of the player "Brown" HTML title_tag tag.
                cpc.title_tag = "NBA's Next Class | " + player.last

                # Display "Brown" player information to the "body_tag" content area of the dynamic page.

                # Opening HTML UL tag.
                cpc.body_tag += cpc.begin_ul

                # Incorporate navigation buttons for this player "Brown" dynamic page to the UL tag.
                cpc.body_tag += cpc.build_nav_button("?id=0", "Home")
                cpc.body_tag += cpc.build_nav_button("?id=1", "Ben Simmons")
                cpc.body_tag += cpc.build_nav_button("?id=2", "Brandon Ingram")
                cpc.body_tag += cpc.build_nav_button("?id=3", "Buddy Hield")
                cpc.body_tag += cpc.build_nav_button("?id=4", "Kris Dunn")
                cpc.body_tag += cpc.build_nav_button("?id=5", "Jamal Murray")
                cpc.body_tag += cpc.build_nav_button("?id=6", "Jaylen Brown")

                # Closing HTML UL tag.
                cpc.body_tag += cpc.end_ul

                # Incorporate all player "Brown" automobile "body_tag" dynamic content.
                cpc.body_tag += cpc.write_player_data(player)
                cpc.body_tag += cpc.write_player_jerseys(player)
                cpc.body_tag += cpc.write_content(player)

                # Close this section of the dynamic HTML page.
                cpc.body_tag += cpc.end_section

                # Write player "Brown" dynamic HTML page.
                self.response.write(cpc.build_markup())

        # Else statement exists to tell python to load these code settings as if it were a HTML default "index" page.
        else:

            # Manipulation of the "Home" HTML title_tag, tag (the default setting).
            cpc.title_tag = "NBA's Next Class | Home"

            # Display "Chevy Home" information to the "body_tag" content area of the dynamic page (the default setting).

            # Opening HTML UL tag (the default setting).
            cpc.body_tag += cpc.begin_ul

            # Incorporate navigation buttons for this "Home" dynamic page to the UL tag (the default setting).
            cpc.body_tag += cpc.build_nav_button("?id=1", "Ben Simmons")
            cpc.body_tag += cpc.build_nav_button("?id=2", "Brandon Ingram")
            cpc.body_tag += cpc.build_nav_button("?id=3", "Buddy Hield")
            cpc.body_tag += cpc.build_nav_button("?id=4", "Kris Dunn")
            cpc.body_tag += cpc.build_nav_button("?id=5", "Jamal Murray")
            cpc.body_tag += cpc.build_nav_button("?id=6", "Jaylen Brown")

            # Closing HTML UL tag (the default setting).
            cpc.body_tag += cpc.end_ul

            # Home page information HTML tags consisting of H1 and p tags (the default setting).
            cpc.body_tag += "<h1 id='home_h1'>Welcome To Chevypalooza!</h1>\n"
            cpc.body_tag += "<p id='home_p1'>This web page is dedicated to all the classic Chevy enthusiasts out there that display the same passion and energy for chevys' like I do!</p>\n"
            cpc.body_tag += "<p id='home_p2'>If you follow the links above, you'll enjoy all the wonderful information on each of these Chevy choices</p>\n"

            # GET the associated image for the "Home" dynamic page (the default setting).
            cpc.body_tag += cpc.add_image("/images/index.png", "Awesome Chevy Background Image")

            # Write "Home" dynamic HTML page (the default setting).
            self.response.write(cpc.build_markup())


# Don't remove this, it's the code that makes Google App Engine work.
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

