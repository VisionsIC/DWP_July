###
#  WDD Degree Program
#  Course: DPW
#  Student: Aaron Wilson
#  Student ID: 0004619821
#  Assignment: Project 2: Simple Form - page.py
#  Date: July 04, 2016
###


#  This "Page" class initiates all the page's HTML tags.
class Page:

    #  Defines a __init__ function to induce the head html markup on to the web page.
    def __init__(self):

        #  Writes the doctype, html, head, and body tags; applying the "Page" class "head" attribute.
        self.head = '''<!DOCTYPE>
        <html>
        <head>
            <title>Welcome To Shoeshine Boy Online</title>
            <link rel="stylesheet" href="css/main.css" type="text/css" />
        </head>
        <body>
            <div id="content_wrap">
            <header>
                <h1 id="instruct_h1">Please Fill Out The Form Below: </h1>
            <div id="logo_div">
                <img id="shoe_logo" src="images/bg/shoeshine.png" />
            </div>
            </header>'''

        #  Writes the closing body and html tags applying the "Page" class "close" attribute.
        self.close = '''
        </div>
        <script src="js/jquery-1.6.2.js"></script>
        <script src="js/toggle.js"></script>
        </body>
        </html>'''

    #  This "begin_page" function both initiates and returns the page's "header" variable attribute.
    def begin_page(self):

        #  The "header" variable links together the "head" variable attribute and html to the "begin_page" function.
        header = self.head

        #  This "return" statement returns the "header" variable attribute and html to the "begin_page" function.
        return header

    #  This "close_page" function returns the page's "close" variable attribute.
    def close_page(self):

        #  The "return" statement returns the "close" variable attribute and html of the "begin_page" function.
        return self.close


#  This "Form" class initiates all the page's HTML tags associated with the form element HTML.
class Form:

    #  This "__init__" function initiates the page's form HTML element.
    def __init__(self):

        # This "inputs" variable attribute initiates the page's form HTML element.
        self.inputs = '''

        <form method="GET" action="">
        <div id="info_wrap">
            <label id="f_name" for="first_name">First name:</label>
            <input type="text" name="firstName" id="first_name" />
            <label id="l_name" for="last_name">Last name:</label>
            <input type="text" name="lastName" id="last_name"/>
            <label id="b_date" for="month_select">Enter Your DOB:</label>

            <select name="birthmonth" id="month_select">
                <option value="na">Month</option>
                <option value="January">January</option>
                <option value="February">February</option>
                <option value="March">March</option>
                <option value="April">April</option>
                <option value="May">May</option>
                <option value="June">June</option>
                <option value="July">July</option>
                <option value="August">August</option>
                <option value="September">September</option>
                <option value="October">October</option>
                <option value="November">November</option>
                <option value="December">December</option>
            </select>

            <select name="birthday" id="day_select">
                <option value="na">Day</option>
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
                <option value="6">6</option>
                <option value="7">7</option>
                <option value="8">8</option>
                <option value="9">9</option>
                <option value="10">10</option>
                <option value="11">11</option>
                <option value="12">12</option>
                <option value="13">13</option>
                <option value="14">14</option>
                <option value="15">15</option>
                <option value="16">16</option>
                <option value="17">17</option>
                <option value="18">18</option>
                <option value="19">19</option>
                <option value="20">20</option>
                <option value="21">21</option>
                <option value="22">22</option>
                <option value="23">23</option>
                <option value="24">24</option>
                <option value="25">25</option>
                <option value="26">26</option>
                <option value="27">27</option>
                <option value="28">28</option>
                <option value="29">29</option>
                <option value="30">30</option>
                <option value="31">31</option>
            </select>
            <select name="birthyear" id="year_select">
                <option value="1998">1998</option>
                <option value="1997">1997</option>
                <option value="1996">1996</option>
                <option value="1995">1995</option>
                <option value="1994">1994</option>
                <option value="1993">1993</option>
                <option value="1992">1992</option>
                <option value="1991">1991</option>
                <option value="1990">1990</option>
                <option value="1989">1989</option>
                <option value="1988">1988</option>
                <option value="1987">1987</option>
                <option value="1986">1986</option>
                <option value="1985">1985</option>
                <option value="1984">1984</option>
                <option value="1983">1983</option>
                <option value="1982">1982</option>
                <option value="1981">1981</option>
                <option value="1980">1980</option>
                <option value="1979">1979</option>
                <option value="1978">1978</option>
                <option value="1977">1977</option>
                <option value="1976">1976</option>
                <option value="1975">1975</option>
                <option value="1974">1974</option>
                <option value="1973">1973</option>
                <option value="1972">1972</option>
                <option value="1971">1971</option>
                <option value="1970">1970</option>
                <option value="1969">1969</option>
                <option value="1968">1968</option>
                <option value="1967">1967</option>
                <option value="1966">1966</option>
                <option value="1965">1965</option>
                <option value="1964">1964</option>
                <option value="1963">1963</option>
                <option value="1962">1962</option>
                <option value="1961">1961</option>
                <option value="1960">1960</option>
                <option value="1959">1959</option>
                <option value="1958">1958</option>
                <option value="1957">1957</option>
                <option value="1956">1956</option>
                <option value="1955">1955</option>
                <option value="1954">1954</option>
                <option value="1953">1953</option>
                <option value="1952">1952</option>
                <option value="1951">1951</option>
                <option value="1950">1950</option>
                <option value="1949">1949</option>
                <option value="1948">1948</option>
                <option value="1947">1947</option>
                <option value="1946">1946</option>
                <option value="1945">1945</option>
                <option value="1944">1944</option>
                <option value="1943">1943</option>
                <option value="1942">1942</option>
                <option value="1941">1941</option>
                <option value="1940">1940</option>
            </select>
            <label id="gender_lbl"> Select Your Gender: </label>
                <div id="radio">
                     <input type="radio" name="gender" value="Male" id="male">
                     <label id="male_lbl" for="male">Male:</label>
                     <input type="radio" name="gender" value="Female" id="female">
                     <label id="female_lbl" for="female">Female:</label>
                </div>
        </div>
            <label id="shoe_item" for="shoe_item">Please Fill Out the Form Below:</label>
            <div id="hide_me">
            <h1 id="instruct_h1">Please Fill Out The Form Below: </h1>
            </div>

            <!-- Male DIV HIDDEN at page load -->

            <div id="male_div" style="display:none">
                <div class="checkbox_wrap" id="dm_casual">
                    <input type="checkbox" name="shoe_item" id="im_casual" value=" The Shoeshine Boy Men's Casual Shoe" />
                    <label for="im_casual">
                        <img src="images/shoes/men/m_casual.png" alt="The Shoeshine Boy Men's Casual Shoe"/>
                    </label>
                </div>
                <div class="checkbox_wrap" id="dm_dress">
                    <input type="checkbox" name="shoe_item" id="im_dress" value=" The Shoeshine Boy Men's Dress Shoe" />
                    <label for="im_dress">
                        <img src="images/shoes/men/m_dress.png" alt="The Shoeshine Boy Men's Dress Shoe"/>
                    </label>
                </div>
                <div class="checkbox_wrap" id="dm_work">
                    <input type="checkbox" name="shoe_item" id="im_work" value=" The Shoeshine Boy Men's Work Shoe" />
                    <label for="im_work">
                        <img src="images/shoes/men/m_work.png" alt="The Shoeshine Boy Men's Work Shoe"/>
                    </label>
                </div>
                <div class="checkbox_wrap" id="dm_loafer">
                    <input type="checkbox" name="shoe_item" id="im_loafer" value=" The Shoeshine Boy Men's Loafer" />
                    <label for="im_loafer">
                        <img src="images/shoes/men/m_loafer.png" alt="The Shoeshine Boy Men's Loafer"/>
                    </label>
                </div>
                <div class="checkbox_wrap" id="dm_sandal">
                    <input type="checkbox" name="shoe_item" id="im_sandal" value=" The Shoeshine Boy Men's Sandal" />
                    <label for="im_sandal">
                        <img src="images/shoes/men/m_sandal.png" alt="The Shoeshine Boy Men's Sandal"/>
                    </label>
                </div>
                <div class="checkbox_wrap" id="dm_sneaker">
                    <input type="checkbox" name="shoe_item" id="im_sneaker" value=" The Shoeshine Boy Men's Sneaker" />
                    <label for="im_sneaker">
                        <img src="images/shoes/men/m_sneaker.png" alt="The Shoeshine Boy Men's Sneaker"/>
                    </label>
                </div>

            <input type="submit" class="submit_btn" value="Send Your Selections To Shoeshine Boy" />
            </div>

            <!-- Female DIV HIDDEN at page load -->

            <div id="female_div" style="display:none">
                <div class="checkbox_wrap" id="df_casual">
                    <input type="checkbox" name="shoe_item" id="if_casual" value=" The Shoeshine Boy Women's Casual Shoe" />
                    <label for="if_casual">
                        <img src="images/shoes/women/f_casual.png" alt="The Shoeshine Boy Women's Casual Shoe"/>
                    </label>
                </div>
                <div class="checkbox_wrap" id="df_dress">
                    <input type="checkbox" name="shoe_item" id="if_dress" value=" The Shoeshine Boy Women's Dress Shoe" />
                    <label for="if_dress">
                        <img src="images/shoes/women/f_dress.png" alt="The Shoeshine Boy Women's Dress Shoe"/>
                    </label>
                </div>
                <div class="checkbox_wrap" id="df_work">
                    <input type="checkbox" name="shoe_item" id="if_work" value=" The Shoeshine Boy Women's Work Shoe" />
                    <label for="if_work">
                        <img src="images/shoes/women/f_work.png" alt="The Shoeshine Boy Women's Work Shoe"/>
                    </label>
                </div>
                <div class="checkbox_wrap" id="df_loafer">
                    <input type="checkbox" name="shoe_item" id="if_loafer" value=" The Shoeshine Boy Women's Loafer" />
                    <label for="if_loafer">
                        <img src="images/shoes/women/f_loafer.png" alt="The Shoeshine Boy Women's Loafer"/>
                    </label>
                </div>
                <div class="checkbox_wrap" id="df_sandal">
                    <input type="checkbox" name="shoe_item" id="if_sandal" value=" The Shoeshine Boy Women's Sandal" />
                    <label for="if_sandal">
                        <img src="images/shoes/women/f_sandal.png" alt="The Shoeshine Boy Women's Sandal"/>
                    </label>
                </div>
                <div class="checkbox_wrap" id="df_sneaker">
                    <input type="checkbox" name="shoe_item" id="if_sneaker" value=" The Shoeshine Boy Women's Sneaker" />
                    <label for="if_sneaker">
                        <img src="images/shoes/women/f_sneaker.png" alt="The Shoeshine Boy Women's Sneaker"/>
                    </label>
                </div>

            <input type="submit" class="submit_btn" value="Send Your Selections To Shoeshine Boy" />
            </div>
        </form>

        <div id="announce_div">

            <h1 id="index_h1">Clicking the Male Or Female Radio Button Will Display Appropriate Men's Or Women's Shoe Choices:</h1>
        </div>

        <footer id="index_ftr">
            <h2>&copy; 2016 Shoeshine Boy | A fictitious company for use as an assignment | FULL SAIL UNIVERSITY</h2>
        </footer>

        '''

    # This "begin_form" function holds the "form" variable attribute which initiates the "inputs" variable, and
    #  "returns" that same "form" variable.
    def begin_form(self):

        # This "form" variable stores the "inputs" variable.
        form = self.inputs

        # This "return" statement returns the form variable.
        return form
