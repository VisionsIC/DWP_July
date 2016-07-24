/**
 * Created by aaronrobertwilson on 7/6/16.
 */
             /* Hide the middle #announce_div */

            $('#male').click(function(){
            $('#announce_div').hide();
            });
            $('#female').click(function(){
            $('#announce_div').hide();
            });

            /* Show each of the divs for the appropriate shoe choices */

            $('input[name="gender"]').bind('change',function(){
                var show_male = ($(this).val() == 'Male') ? true : false;
            $('#male_div').toggle(show_male);
                var show_female = ($(this).val() == 'Female') ? true : false;
            $('#female_div').toggle(show_female);
            });

