
# WDD Degree Program
# Course: DPW
# Student: Aaron Wilson
# Student ID: 0004619821
# Assignment: Project 4 - Dynamic Site: pages.py
# Date: July 25, 2016


# Creates the super class Page() to implement all attributes, functions, methods, and variables as HTML tags:
class Page(object):

    # This "__init__" method outputs all the necessary attributes to be inherited by itself as the superclass and also
    # it's subclass ContentPage(); Then is injected as HTML to the browser page.
    def __init__(self):

        # The below mini-compilation of attributes that creates all the necessary HTML tags to be output to the browser
        # page.
        self.__title_tag = "NBA's New Class | Dynamic Site"
        self.__css_file = "css/main.css"
        self.__web_font = "http://fonts.googleapis.com/css?family=Sacramento"

        # This attribute creates the "header_tag" tags.
        self.__header_tag = '''
<!DOCTYPE html>
    <head>
        <title>{self.title_tag}</title>
        <link rel="stylesheet" href="{self.css_file}" />
        <link rel="stylesheet" href="{self.web_font}" />
    </head>

    <body>'''

        # This attribute creates the "body_tag" html.
        self.__body_tag = ""

        # This attribute creates the "closing_tag" html.
        self.__closing_tag = '''
    </body>
</html>'''

    # Getter to create the "header_tag" method for likewise attribute above.
    @property
    def header_tag(self):
        return self.__header_tag

    # Getter to create the "closing_tag" method for likewise attribute above.
    @property
    def closing_tag(self):
        return self.__closing_tag

    # Getter to create the "title_tag" method for likewise attribute above.
    @property
    def title_tag(self):
        return self.__title_tag

    # Setter to set the "title_tag" method for likewise attribute above.
    @title_tag.setter
    def title_tag(self, new_title):
        self.__title_tag = new_title

    # Getter to create the "css_file" method for likewise attribute above.
    @property
    def css_file(self):
        return self.__css_file

    # Setter to set the "css_file" method for likewise attribute above.
    @css_file.setter
    def css_file(self, new_css):
        self.__css_file = new_css

    # Getter to create the "web_font" method for likewise attribute above.
    @property
    def web_font(self):
        return self.__web_font

    # Setter to set the "web_font" method for likewise attribute above.
    @web_font.setter
    def web_font(self, new_font):
        self.__web_font = new_font

    # Getter to create the "body_tag" method for likewise attribute above.
    @property
    def body_tag(self):
        return self.__body_tag

    # Setter to set the "body_tag" method for likewise attribute above.
    @body_tag.setter
    def body_tag(self, new_body):
        self.__body_tag = new_body

    # The "build_markup" method outputs the necessary variables below "strung" together as HTML to the browser page.
    def build_markup(self):
        self.markup = self.header_tag + self.body_tag + self.closing_tag
        self.markup = self.markup.format(**locals())
        return self.markup

    # The "add_image" method adds the "img" variable as a string to be returned and injected into an HTML tag to be
    # output to the browser page.
    def add_image(self, image_url, alt_text):
        img = "<img id='index_img' src='" + image_url + "' alt='" + alt_text + "' />\n"
        return img


# Create ContentPage() a subclass of the Page() class.
class ContentPage(Page):

    # The "__init__" method outputs all the necessary attributes to be inherited by the superclass and itself; Then
    # injected as HTML to the browser page.
    def __init__(self):

        # This "super" triggers the super class to initialize itself, and below attributes/methods through polymorphism
        # for functionality as output to the browser page.
        super(ContentPage, self).__init__()

        # The below compilation of attributes that creates all the necessary HTML tags to be output to the browser page.
        self.__begin_wrapper = "<section id='wrapper'>\n"  # An HTML wrapper attribute to center the content to page.
        self.__end_wrapper = "</section>"  # Attribute that closes the wrapper.
        self.__begin_ul = "<ul>\n"  # The attribute that writes the opening unordered list to the page.
        self.__end_ul = "</ul>\n"  # closes an unordered list
        self.__end_section = "</section>\n"  # closes a section

        # The "page_header" attribute that creates the header HTML tag to be output to the browser page.
        self.__page_header = '''
    <header>
        <h1>NBA's Next Class</h1>
        <img id="logo" src="images/aaron_logo.png" />
        <p>A look at the potential future stars of the NBA!</p>
    </header>\n'''

        # A footer element HTML tag to be output to the browser page.
        self.__page_footer = '''
    <footer>
        <p>&copy; 2016 NBA's Next Class | A fictitious concept for use as an assignment | FULL SAIL UNIVERSITY </p>
    </footer>'''

    # The "build_nav_button" method outputs the "button" variable as HTML to the browser page.
    def build_nav_button(self, link, title):
        button = "<li><a href='" + link + "'>" + title + "</a></li>\n"
        return button

    # The "write_player_data" method outputs the "data" string as HTML to the browser page.
    def write_player_data(self, player):
        data = '''
        <section id="players">
            <h2> {player.team} {player.first} {player.last}</h2>
            <img src="{player.img}" alt="Classic {player.first} {player.last}" />
            <p id="contract">Player's Rookie contract: $ {player.contract}.00</p>
            <p class="total">Buys him {player.total_shoes} pairs of shoes!</p>\n'''

        # The "data" variable that formats all the "local" variables to be injected into the HTML tags to be output to
        # the browser page.
        data = data.format(**locals())

        # The RETURN statement returns the "data" variable that aides in the creation of the "write_player_data" method
        # that is output to the browser page.
        return data

    # The "write_player_jerseys" method that writes the output string that goes into the FOR loop, then outputs as HTML
    # to the browser page.
    def write_player_jerseys(self, player):
        jerseys = player.jerseys
        output = ""
        string = ""

        # A FOR loop that puts together all the data types for the jerseys of each player.
        for logo in jerseys:
            output += "<span id='out'><img id='jersey_img' src='images/jerseys/" + logo + ".png' />,</span>\n"
            string = "<span id='string'>Jersey Colors:  </span>\n"

        return string + output

    # The "write_content" method outputs the content paragraph HTML to the browser page.
    def write_content(self, player):
        info = player.information
        return "<p class='info'>" + info + "</p>"

    # This "build_markup" method creates all the HTML tags for output to the browser page.
    def build_markup(self):
        markup = self.header_tag + self.page_header + self.begin_wrapper + self.body_tag + self.end_wrapper + self.page_footer + self.closing_tag
        markup = markup.format(**locals())
        return markup

    # Getter to create the "begin_ul" method for likewise attribute above.
    @property
    def begin_ul(self):
        return self.__begin_ul

    # Getter to create the "end_ul" method for likewise attribute above.
    @property
    def end_ul(self):
        return self.__end_ul

    # Getter to create the "h1_tag" method for likewise attribute above.
    @property
    def h1_tag(self):
        return self.__h1_tag

    # Setter to set the "h1_tag" method for likewise attribute above.
    @h1_tag.setter
    def h1_tag(self, new_h1):
        self.__h1_tag = new_h1

    # Getter to create the "begin_wrapper" method for likewise attribute above.
    @property
    def begin_wrapper(self):
        return self.__begin_wrapper

    # Getter to create the "end_wrapper" method for likewise attribute above.
    @property
    def end_wrapper(self):
        return self.__end_wrapper

    # Getter to create the "page_header" method for likewise attribute above.
    @property
    def page_header(self):
        return self.__page_header

    # Getter to create the "page_footer" method for likewise attribute above.
    @property
    def page_footer(self):
        return self.__page_footer

    # Getter to create the "end_section" method for likewise attribute above.
    @property
    def end_section(self):
        return self.__end_section