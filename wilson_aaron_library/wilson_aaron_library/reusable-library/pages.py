"""
WDD Degree Program
Course: DPW
Student: Aaron Wilson
Student ID: 0004619821
Assignment: Project 3 - Reusable Library - pages.py
May 18, 2016
"""


# This is the BrowserPage Class. This class is needed in order to create a .py file devoted strictly for handling the
# HTML output to a web browser.
class BrowserPage(object):

    # The __init__ function for the BrowserPage class.
    def __init__(self):

        # The BrowserPage __init__ function's necessary attributes that able code injection to these attributes.
        self.title_tag = ''
        self.css_file = ''
        self.h1_title = ''
        self.html_markup = '''

        <!DOCTYPE HTML>
        <html>
            <head>
                <title>{self.title_tag}</title>
                <link href="{self.css_file}" rel="stylesheet" type="text/css" />
            </head>
        <body>
        <h1 id="title_h1">{self.h1_title}</h1>
        <div id="main_output">
            <div class="default_div">
                <header>
                    <h1>Please Enter Patient Data Into The Form Below:</h1><br />
                </header>
            </div>
            <form method="GET" action="">

            <!-- MAIN DIV ELEMENT TAG -->
            <div id="form_wrap">

                <!-- PATIENT FIRST NAME INPUT TAGS -->
                <label class="label_text" id="fname_lbl" for="first_name">First name:</label>
                <input class="input_field" type="text" name="first_name" id="first_name" />

                <!-- PATIENT LAST NAME INPUT TAGS -->
                <label class="label_text" id="lname_lbl" for="last_name">Last name:</label>
                <input class="input_field" type="text" name="last_name" id="last_name"/>

                <!-- PATIENT GENDER DROPDOWN TAGS -->
                <select class="select_option" name="gender" id="gender_select">
                    <option value="na">Select Patient Gender</option>
                    <option value="Male">Male</option>
                    <option value="Female">Female</option>
                </select>

                <!-- PATIENT AGE INPUT TAGS -->
                <label class="label_text" id="age_lbl" for="age">Age:</label>
                <input class="input_field" type="text" name="age" id="age"/>

                <!-- PATIENT HEIGHT DROPDOWN TAGS -->
                <select  class="select_option" name="height" id="height_select">
                    <option name="select" value="na">Select Patient Height</option>
                    <option name="four_foot" value="48">4' 0"</option>
                    <option name="four_one" value="49">4' 1"</option>
                    <option name="four_two" value="50">4' 2"</option>
                    <option name="four_three" value="51">4' 3"</option>
                    <option name="four_four" value="52">4' 4"</option>
                    <option name="four_five" value="53">4' 5"</option>
                    <option name="four_six" value="54">4' 6"</option>
                    <option name="four_seven" value="55">4' 7"</option>
                    <option name="four_eight" value="56">4' 8"</option>
                    <option name="four_nine" value="57">4' 9"</option>
                    <option name="four_ten" value="58">4' 10"</option>
                    <option name="four_eleven" value="59">4' 11"</option>
                    <option name="five_foot" value="60">5' 0"</option>
                    <option name="five_one" value="61">5' 1"</option>
                    <option name="five_two" value="62">5' 2"</option>
                    <option name="five_three" value="63">5' 3"</option>
                    <option name="five_four" value="64">5' 4"</option>
                    <option name="five_five" value="65">5' 5"</option>
                    <option name="five_six" value="66">5' 6"</option>
                    <option name="five_seven" value="67">5' 7"</option>
                    <option name="five_eight" value="68">5' 8"</option>
                    <option name="five_nine" value="69">5' 9"</option>
                    <option name="five_ten" value="70">5' 10"</option>
                    <option name="five_eleven" value="71">5' 11"</option>
                    <option name="six_foot" value="72">6' 0"</option>
                    <option name="six_one" value="73">6' 1"</option>
                    <option name="six_two" value="74">6' 2"</option>
                    <option name="six_three" value="75">6' 3"</option>
                    <option name="six_four" value="76">6' 4"</option>
                    <option name="six_five" value="77">6' 5"</option>
                    <option name="six_six" value="78">6' 6"</option>
                    <option name="six_seven" value="79">6' 7"</option>
                    <option name="six_eight" value="80">6' 8"</option>
                    <option name="six_nine" value="81">6' 9"</option>
                    <option name="six_ten" value="82">6' 10"</option>
                    <option name="six_eleven" value="83">6' 11"</option>
                    <option name="seven_foot" value="84">7' 0"</option>
                </select>

                <!-- PATIENT WEIGHT DROPDOWN TAGS -->
                <select  class="select_option" name="weight" id="weight_select">
                    <option name="select" value="na">Select Patient Weight</option>
                    <option name="50_pounds" value="50">50 lbs</option>
                    <option name="51_pounds" value="51">51 lbs</option>
                    <option name="52_pounds" value="52">52 lbs</option>
                    <option name="53_pounds" value="53">53 lbs</option>
                    <option name="54_pounds" value="54">54 lbs</option>
                    <option name="55_pounds" value="55">55 lbs</option>
                    <option name="56_pounds" value="56">56 lbs</option>
                    <option name="57_pounds" value="57">57 lbs</option>
                    <option name="58_pounds" value="58">58 lbs</option>
                    <option name="59_pounds" value="59">59 lbs</option>
                    <option name="60_pounds" value="60">60 lbs</option>
                    <option name="61_pounds" value="61">61 lbs</option>
                    <option name="62_pounds" value="62">62 lbs</option>
                    <option name="63_pounds" value="63">63 lbs</option>
                    <option name="64_pounds" value="64">64 lbs</option>
                    <option name="65_pounds" value="65">65 lbs</option>
                    <option name="66_pounds" value="66">66 lbs</option>
                    <option name="67_pounds" value="67">67 lbs</option>
                    <option name="68_pounds" value="68">68 lbs</option>
                    <option name="69_pounds" value="69">69 lbs</option>
                    <option name="70_pounds" value="70">70 lbs</option>
                    <option name="71_pounds" value="71">71 lbs</option>
                    <option name="72_pounds" value="72">72 lbs</option>
                    <option name="73_pounds" value="73">73 lbs</option>
                    <option name="74_pounds" value="74">74 lbs</option>
                    <option name="75_pounds" value="75">75 lbs</option>
                    <option name="76_pounds" value="76">76 lbs</option>
                    <option name="77_pounds" value="77">77 lbs</option>
                    <option name="78_pounds" value="78">78 lbs</option>
                    <option name="79_pounds" value="79">79 lbs</option>
                    <option name="80_pounds" value="80">80 lbs</option>
                    <option name="81_pounds" value="81">81 lbs</option>
                    <option name="82_pounds" value="82">82 lbs</option>
                    <option name="83_pounds" value="83">83 lbs</option>
                    <option name="84_pounds" value="84">84 lbs</option>
                    <option name="85_pounds" value="85">85 lbs</option>
                    <option name="86_pounds" value="86">86 lbs</option>
                    <option name="87_pounds" value="87">87 lbs</option>
                    <option name="88_pounds" value="88">88 lbs</option>
                    <option name="89_pounds" value="89">89 lbs</option>
                    <option name="90_pounds" value="90">90 lbs</option>
                    <option name="91_pounds" value="91">91 lbs</option>
                    <option name="92_pounds" value="92">92 lbs</option>
                    <option name="93_pounds" value="93">93 lbs</option>
                    <option name="94_pounds" value="94">94 lbs</option>
                    <option name="95_pounds" value="95">95 lbs</option>
                    <option name="96_pounds" value="96">96 lbs</option>
                    <option name="97_pounds" value="97">97 lbs</option>
                    <option name="98_pounds" value="98">98 lbs</option>
                    <option name="99_pounds" value="99">99 lbs</option>
                    <option name="100_pounds" value="100">100 lbs</option>
                    <option name="101_pounds" value="101">101 lbs</option>
                    <option name="102_pounds" value="102">102 lbs</option>
                    <option name="103_pounds" value="103">103 lbs</option>
                    <option name="104_pounds" value="104">104 lbs</option>
                    <option name="105_pounds" value="105">105 lbs</option>
                    <option name="106_pounds" value="106">106 lbs</option>
                    <option name="107_pounds" value="107">107 lbs</option>
                    <option name="108_pounds" value="108">108 lbs</option>
                    <option name="109_pounds" value="109">109 lbs</option>
                    <option name="110_pounds" value="110">110 lbs</option>
                    <option name="111_pounds" value="111">111 lbs</option>
                    <option name="112_pounds" value="112">112 lbs</option>
                    <option name="113_pounds" value="113">113 lbs</option>
                    <option name="114_pounds" value="114">114 lbs</option>
                    <option name="115_pounds" value="115">115 lbs</option>
                    <option name="116_pounds" value="116">116 lbs</option>
                    <option name="117_pounds" value="117">117 lbs</option>
                    <option name="118_pounds" value="118">118 lbs</option>
                    <option name="119_pounds" value="119">119 lbs</option>
                    <option name="120_pounds" value="120">120 lbs</option>
                    <option name="121_pounds" value="121">121 lbs</option>
                    <option name="122_pounds" value="122">122 lbs</option>
                    <option name="123_pounds" value="123">123 lbs</option>
                    <option name="124_pounds" value="124">124 lbs</option>
                    <option name="125_pounds" value="125">125 lbs</option>
                    <option name="126_pounds" value="126">126 lbs</option>
                    <option name="127_pounds" value="127">127 lbs</option>
                    <option name="128_pounds" value="128">128 lbs</option>
                    <option name="129_pounds" value="129">129 lbs</option>
                    <option name="130_pounds" value="130">130 lbs</option>
                    <option name="131_pounds" value="131">131 lbs</option>
                    <option name="132_pounds" value="132">132 lbs</option>
                    <option name="133_pounds" value="133">133 lbs</option>
                    <option name="134_pounds" value="134">134 lbs</option>
                    <option name="135_pounds" value="135">135 lbs</option>
                    <option name="136_pounds" value="136">136 lbs</option>
                    <option name="137_pounds" value="137">137 lbs</option>
                    <option name="138_pounds" value="138">138 lbs</option>
                    <option name="139_pounds" value="139">139 lbs</option>
                    <option name="140_pounds" value="140">140 lbs</option>
                    <option name="141_pounds" value="141">141 lbs</option>
                    <option name="142_pounds" value="142">142 lbs</option>
                    <option name="143_pounds" value="143">143 lbs</option>
                    <option name="144_pounds" value="144">144 lbs</option>
                    <option name="145_pounds" value="145">145 lbs</option>
                    <option name="146_pounds" value="146">146 lbs</option>
                    <option name="147_pounds" value="147">147 lbs</option>
                    <option name="148_pounds" value="148">148 lbs</option>
                    <option name="149_pounds" value="149">149 lbs</option>
                    <option name="150_pounds" value="150">150 lbs</option>
                    <option name="151_pounds" value="151">151 lbs</option>
                    <option name="152_pounds" value="152">152 lbs</option>
                    <option name="153_pounds" value="153">153 lbs</option>
                    <option name="154_pounds" value="154">154 lbs</option>
                    <option name="155_pounds" value="155">155 lbs</option>
                    <option name="156_pounds" value="156">156 lbs</option>
                    <option name="157_pounds" value="157">157 lbs</option>
                    <option name="158_pounds" value="158">158 lbs</option>
                    <option name="159_pounds" value="159">159 lbs</option>
                    <option name="160_pounds" value="160">160 lbs</option>
                    <option name="161_pounds" value="161">161 lbs</option>
                    <option name="162_pounds" value="162">162 lbs</option>
                    <option name="163_pounds" value="163">163 lbs</option>
                    <option name="164_pounds" value="164">164 lbs</option>
                    <option name="165_pounds" value="165">165 lbs</option>
                    <option name="166_pounds" value="166">166 lbs</option>
                    <option name="167_pounds" value="167">167 lbs</option>
                    <option name="168_pounds" value="168">168 lbs</option>
                    <option name="169_pounds" value="169">169 lbs</option>
                    <option name="170_pounds" value="170">170 lbs</option>
                    <option name="171_pounds" value="171">171 lbs</option>
                    <option name="172_pounds" value="172">172 lbs</option>
                    <option name="173_pounds" value="173">173 lbs</option>
                    <option name="174_pounds" value="174">174 lbs</option>
                    <option name="175_pounds" value="175">175 lbs</option>
                    <option name="176_pounds" value="176">176 lbs</option>
                    <option name="177_pounds" value="177">177 lbs</option>
                    <option name="178_pounds" value="178">178 lbs</option>
                    <option name="179_pounds" value="179">179 lbs</option>
                    <option name="180_pounds" value="180">180 lbs</option>
                    <option name="181_pounds" value="181">181 lbs</option>
                    <option name="182_pounds" value="182">182 lbs</option>
                    <option name="183_pounds" value="183">183 lbs</option>
                    <option name="184_pounds" value="184">184 lbs</option>
                    <option name="185_pounds" value="185">185 lbs</option>
                    <option name="186_pounds" value="186">186 lbs</option>
                    <option name="187_pounds" value="187">187 lbs</option>
                    <option name="188_pounds" value="188">188 lbs</option>
                    <option name="189_pounds" value="189">189 lbs</option>
                    <option name="190_pounds" value="190">190 lbs</option>
                    <option name="191_pounds" value="191">191 lbs</option>
                    <option name="192_pounds" value="192">192 lbs</option>
                    <option name="193_pounds" value="193">193 lbs</option>
                    <option name="194_pounds" value="194">194 lbs</option>
                    <option name="195_pounds" value="195">195 lbs</option>
                    <option name="196_pounds" value="196">196 lbs</option>
                    <option name="197_pounds" value="197">197 lbs</option>
                    <option name="198_pounds" value="198">198 lbs</option>
                    <option name="199_pounds" value="199">199 lbs</option>
                    <option name="200_pounds" value="200">200 lbs</option>
                    <option name="201_pounds" value="201">201 lbs</option>
                    <option name="202_pounds" value="202">202 lbs</option>
                    <option name="203_pounds" value="203">203 lbs</option>
                    <option name="204_pounds" value="204">204 lbs</option>
                    <option name="205_pounds" value="205">205 lbs</option>
                    <option name="206_pounds" value="206">206 lbs</option>
                    <option name="207_pounds" value="207">207 lbs</option>
                    <option name="208_pounds" value="208">208 lbs</option>
                    <option name="209_pounds" value="209">209 lbs</option>
                    <option name="210_pounds" value="210">210 lbs</option>
                    <option name="211_pounds" value="211">211 lbs</option>
                    <option name="212_pounds" value="212">212 lbs</option>
                    <option name="213_pounds" value="213">213 lbs</option>
                    <option name="214_pounds" value="214">214 lbs</option>
                    <option name="215_pounds" value="215">215 lbs</option>
                    <option name="216_pounds" value="216">216 lbs</option>
                    <option name="217_pounds" value="217">217 lbs</option>
                    <option name="218_pounds" value="218">218 lbs</option>
                    <option name="219_pounds" value="219">219 lbs</option>
                    <option name="220_pounds" value="220">220 lbs</option>
                    <option name="221_pounds" value="221">221 lbs</option>
                    <option name="222_pounds" value="222">222 lbs</option>
                    <option name="223_pounds" value="223">223 lbs</option>
                    <option name="224_pounds" value="224">224 lbs</option>
                    <option name="225_pounds" value="225">225 lbs</option>
                    <option name="226_pounds" value="226">226 lbs</option>
                    <option name="227_pounds" value="227">227 lbs</option>
                    <option name="228_pounds" value="228">228 lbs</option>
                    <option name="229_pounds" value="229">229 lbs</option>
                    <option name="230_pounds" value="230">230 lbs</option>
                    <option name="231_pounds" value="231">231 lbs</option>
                    <option name="232_pounds" value="232">232 lbs</option>
                    <option name="233_pounds" value="233">233 lbs</option>
                    <option name="234_pounds" value="234">234 lbs</option>
                    <option name="235_pounds" value="235">235 lbs</option>
                    <option name="236_pounds" value="236">236 lbs</option>
                    <option name="237_pounds" value="237">237 lbs</option>
                    <option name="238_pounds" value="238">238 lbs</option>
                    <option name="239_pounds" value="239">239 lbs</option>
                    <option name="240_pounds" value="240">240 lbs</option>
                    <option name="241_pounds" value="241">241 lbs</option>
                    <option name="242_pounds" value="242">242 lbs</option>
                    <option name="243_pounds" value="243">243 lbs</option>
                    <option name="244_pounds" value="244">244 lbs</option>
                    <option name="245_pounds" value="245">245 lbs</option>
                    <option name="246_pounds" value="246">246 lbs</option>
                    <option name="247_pounds" value="247">247 lbs</option>
                    <option name="248_pounds" value="248">248 lbs</option>
                    <option name="249_pounds" value="249">249 lbs</option>
                    <option name="250_pounds" value="250">250 lbs</option>
                    <option name="251_pounds" value="251">251 lbs</option>
                    <option name="252_pounds" value="252">252 lbs</option>
                    <option name="253_pounds" value="253">253 lbs</option>
                    <option name="254_pounds" value="254">254 lbs</option>
                    <option name="255_pounds" value="255">255 lbs</option>
                    <option name="256_pounds" value="256">256 lbs</option>
                    <option name="257_pounds" value="257">257 lbs</option>
                    <option name="258_pounds" value="258">258 lbs</option>
                    <option name="259_pounds" value="259">259 lbs</option>
                    <option name="260_pounds" value="260">260 lbs</option>
                    <option name="261_pounds" value="261">261 lbs</option>
                    <option name="262_pounds" value="262">262 lbs</option>
                    <option name="263_pounds" value="263">263 lbs</option>
                    <option name="264_pounds" value="264">264 lbs</option>
                    <option name="265_pounds" value="265">265 lbs</option>
                    <option name="266_pounds" value="266">266 lbs</option>
                    <option name="267_pounds" value="267">267 lbs</option>
                    <option name="268_pounds" value="268">268 lbs</option>
                    <option name="269_pounds" value="269">269 lbs</option>
                    <option name="270_pounds" value="270">270 lbs</option>
                    <option name="271_pounds" value="271">271 lbs</option>
                    <option name="272_pounds" value="272">272 lbs</option>
                    <option name="273_pounds" value="273">273 lbs</option>
                    <option name="274_pounds" value="274">274 lbs</option>
                    <option name="275_pounds" value="275">275 lbs</option>
                    <option name="276_pounds" value="276">276 lbs</option>
                    <option name="277_pounds" value="277">277 lbs</option>
                    <option name="278_pounds" value="278">278 lbs</option>
                    <option name="279_pounds" value="279">279 lbs</option>
                    <option name="280_pounds" value="280">280 lbs</option>
                    <option name="281_pounds" value="281">281 lbs</option>
                    <option name="282_pounds" value="282">282 lbs</option>
                    <option name="283_pounds" value="283">283 lbs</option>
                    <option name="284_pounds" value="284">284 lbs</option>
                    <option name="285_pounds" value="285">285 lbs</option>
                    <option name="286_pounds" value="286">286 lbs</option>
                    <option name="287_pounds" value="287">287 lbs</option>
                    <option name="288_pounds" value="288">288 lbs</option>
                    <option name="289_pounds" value="289">289 lbs</option>
                    <option name="290_pounds" value="290">290 lbs</option>
                    <option name="291_pounds" value="291">291 lbs</option>
                    <option name="292_pounds" value="292">292 lbs</option>
                    <option name="293_pounds" value="293">293 lbs</option>
                    <option name="294_pounds" value="294">294 lbs</option>
                    <option name="295_pounds" value="295">295 lbs</option>
                    <option name="296_pounds" value="296">296 lbs</option>
                    <option name="297_pounds" value="297">297 lbs</option>
                    <option name="298_pounds" value="298">298 lbs</option>
                    <option name="299_pounds" value="299">299 lbs</option>
                    <option name="300_pounds" value="300">300 lbs</option>
                    <option name="301_pounds" value="301">301 lbs</option>
                    <option name="302_pounds" value="302">302 lbs</option>
                    <option name="303_pounds" value="303">303 lbs</option>
                    <option name="304_pounds" value="304">304 lbs</option>
                    <option name="305_pounds" value="305">305 lbs</option>
                    <option name="306_pounds" value="306">306 lbs</option>
                    <option name="307_pounds" value="307">307 lbs</option>
                    <option name="308_pounds" value="308">308 lbs</option>
                    <option name="309_pounds" value="309">309 lbs</option>
                    <option name="310_pounds" value="310">310 lbs</option>
                    <option name="311_pounds" value="311">311 lbs</option>
                    <option name="312_pounds" value="312">312 lbs</option>
                    <option name="313_pounds" value="313">313 lbs</option>
                    <option name="314_pounds" value="314">314 lbs</option>
                    <option name="315_pounds" value="315">315 lbs</option>
                    <option name="316_pounds" value="316">316 lbs</option>
                    <option name="317_pounds" value="317">317 lbs</option>
                    <option name="318_pounds" value="318">318 lbs</option>
                    <option name="319_pounds" value="319">319 lbs</option>
                    <option name="320_pounds" value="320">320 lbs</option>
                    <option name="321_pounds" value="321">321 lbs</option>
                    <option name="322_pounds" value="322">322 lbs</option>
                    <option name="323_pounds" value="323">323 lbs</option>
                    <option name="324_pounds" value="324">324 lbs</option>
                    <option name="325_pounds" value="325">325 lbs</option>
                    <option name="326_pounds" value="326">326 lbs</option>
                    <option name="327_pounds" value="327">327 lbs</option>
                    <option name="328_pounds" value="328">328 lbs</option>
                    <option name="329_pounds" value="329">329 lbs</option>
                    <option name="330_pounds" value="330">330 lbs</option>
                    <option name="331_pounds" value="331">331 lbs</option>
                    <option name="332_pounds" value="332">332 lbs</option>
                    <option name="333_pounds" value="333">333 lbs</option>
                    <option name="334_pounds" value="334">334 lbs</option>
                    <option name="335_pounds" value="335">335 lbs</option>
                    <option name="336_pounds" value="336">336 lbs</option>
                    <option name="337_pounds" value="337">337 lbs</option>
                    <option name="338_pounds" value="338">338 lbs</option>
                    <option name="339_pounds" value="339">339 lbs</option>
                    <option name="340_pounds" value="340">340 lbs</option>
                    <option name="341_pounds" value="341">341 lbs</option>
                    <option name="342_pounds" value="342">342 lbs</option>
                    <option name="343_pounds" value="343">343 lbs</option>
                    <option name="344_pounds" value="344">344 lbs</option>
                    <option name="345_pounds" value="345">345 lbs</option>
                    <option name="346_pounds" value="346">346 lbs</option>
                    <option name="347_pounds" value="347">347 lbs</option>
                    <option name="348_pounds" value="348">348 lbs</option>
                    <option name="349_pounds" value="349">349 lbs</option>
                    <option name="350_pounds" value="350">350 lbs</option>
                </select>

                <!-- PATIENT DIAGNOSIS DROPDOWN TAGS -->
                <select  class="select_option" name="diagnosis" id="diagnosis_select">
                    <option name="select" value="na">Select Patient Diagnosis</option>
                    <option name="bilateral_knee" value="Bilateral Knees">Bilateral Knee Replacement</option>
                    <option name="multiple_sclerosis" value="Multiple Sclerosis">Multiple Sclerosis</option>
                    <option name="cerebral_palsy" value="Cerebral Palsy">Cerebral Palsy</option>
                    <option name="paraplegic" value="Paraplegic">Paraplegic</option>
                    <option name="quadriplegic" value="Quadriplegic">Quadriplegic</option>
                </select>


            <!-- SUBMIT BUTTON HTML TAGS -->
                <input class="input_field" id="wc_button" type="submit" value="Submit Wheelchair Request" />
            </form>
            </div>
            <script src="{self.js_file}"></script>
            </body>
        </html>
        '''

    # This defines the function below as "default_output". The idea of this function is to display and inject the
    # default view when user first opens the page in a web browser. Similar to a "home" page.
    def default_output(self):

        # Output variable strings the "output" variable with the "local" variables to output all user pre-selected
        # choices.
        default_page = self.html_markup
        default_page = default_page.format(**locals())

        # This Return statement, returns the attributes set forth in the "default_page" variable. Thus, executes this
        # function.
        return default_page


# This is the DynamicOutput Class. This class is needed in order to create a .py file devoted strictly for handling the
# HTML output to a web browser. Also this class focuses on the dynamic content handling of the code and output.
class DynamicOutput(object):

    # The DynamicOutput class __init__ function for the DynamicOutput class.
    def __init__(self):

        # The DynamicOutput class __init__ function's necessary attributes that able code injection to these attributes.
        self.title_tag = ''
        self.css_file = ''
        self.dynamic_data = ''
        self.html_markup = '''

        <!DOCTYPE HTML>

            <html>

                <head>
                    <title>{self.title_tag}</title>
                    <link href="{self.css_file}" rel="stylesheet" type="text/css" />
                </head>
                <body>
                    <div id="main_output">
                        <div id="info_output">
                            <h1>Please review your Patient's information below:</h1>
                        </div>

                        <div id="wc_output">
                        {self.dynamic_data}
                        </div>
                    </div>
                </body>
                  <script src ="{self.js_file}"></script>
            </html>'''

    # Dynamic output function passes the "data_output" argument to the HTML tags. Also controls the locals for code
    # injection into the HTML.
    def dynamic_output(self, data_output):

        # Output variable strings the "output" variable with the "local" variables to output all user pre-selected
        # choices.
        self.dynamic_data = data_output
        dynamic_page = self.html_markup.format(**locals())

        # Returns "dynamic_page" variable so as to "output" the final user input code to the browser.
        return dynamic_page




