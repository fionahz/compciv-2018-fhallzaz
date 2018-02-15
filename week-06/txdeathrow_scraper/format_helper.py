from datetime import datetime
from urllib.parse import urljoin
import data_helper

def txdate_to_iso(datestr):
    """
    A helper function that, given a date formatted the way that the
    Texas Dept. of Justice does it,
        i.e. MM/DD/YYYY, e.g. '10/24/1988'
        or even: '10/24/88'

    and returns a ISO-formatted string, i.e. YYYY-MM-DD

    Args:
        datestr: a <str>, ostensibly one that is meant to be a
            date value like '10/24/1988'

    Returns:
        <str>: in 'YYYY-MM-DD' format, e.g. '1988-10-24'
    """
    datearray = datestr.split("/")
    datearray[0], datearray[1], datearray[2] = datearray[2].strip(), datearray[0].strip(), datearray[1].strip()
    if len(datearray[0]) != 4:
        if int(datearray[0]) > 18:
            datearray[0] = "19" + datearray[0]
        else:
            datearray[0] = "20" + datearray[0]
    return_date = '-'.join(datearray)
    print(return_date)
    return return_date

def calc_years_diff(start_date, end_date):
    """
    A helper function that, given 2 ISO-formatted date strings
    returns the difference in fractional years, to the nearest 0.1
    of a year.

    Args:
        start_date: <str> the "older" date, in "YYYY-MM-DD" format
        end_date: <str> the "later" date, in "YYYY-MM-DD" format

    Returns:
        <float> A decimal number representing the number of years
           between dates, e.g. 12.4

    Recommendation:
        This is actually quite complicated, thanks to leap years/days/secs, among
        other complications...

        https://stackoverflow.com/questions/4436957/pythonic-difference-between-two-dates-in-years

        Convert the strings into datetime.datetime objects. Then subtract the
          2 objects to get number of days. Divide by that 365 to get the
          estimated years difference. Rounding to the first decimal place
          will be enough precision. And leap years shouldn't make THAT much
          of a difference...
    """
    #start_array = start_date.split("-")
    #start_datetime = datetime(int(start_array[0]), int(start_array[1]), int(start_array[2]))
    #end_array = end_date.split("-")
    #end_datetime = datetime(int(end_array[0]), int(end_array[1]), int(end_array[2]))
    #diffyears = end_datetime.year - start_datetime.year
    #if start_datetime.month == 2 and start_datetime.day == 29 and !:
    #    start_datetime.day == 28 
    #difference  = end_datetime - start_datetime.replace(end_datetime.year)
    #difference_in_years = float(diffyears) + float(difference.days/365)
    #return difference_in_years
    start_datetime = datetime.strptime(start_date, '%Y-%m-%d')
    end_datetime = datetime.strptime(end_date, '%Y-%m-%d')
    diffyears = end_datetime.year - start_datetime.year
    #if start_datetime.month == 2 and start_datetime.day == 29 and !:
    #    start_datetime.day == 28 
    try:
        difference  = end_datetime - start_datetime.replace(end_datetime.year)
    except ValueError:
        # Must be 2/29!
        difference  = end_datetime - start_datetime.replace(month=2, day=28, year=end_datetime.year)
    difference_in_years = round((float(diffyears) + float(difference.days/365)),1)
    return difference_in_years

def make_absolute_url(href):
    """
    This function uses data_helper.DATA_SRC_URL and the builtin function
      urllib.parse.urljoin() to programmatically join a relative URL with
      the known URL of the source page (DATA_SRC_URL)

    Args:
        href: a <str> object that is a partial URL that looks something like:

           'dr_info/falkjohnjr.html'
    Returns:
        <str>: A fully resolvable URL for a webpage, e.g.

            'https://wgetsnaps.github.io/tdcj-state-tx-us-2018/death_row/dr_info/falkjohnjr.html'


    The TX death penalty page contains URLs for the "Offender Information"
    pages, and these URLs are in relative format, e.g.

    dr_info/falkjohnjr.html

    But we want them in absolute format:



    The absolute form of a URL depends on the URL that the page was
        *scraped* from. In this exercise, it's the value of the
        DATA_SRC_URL which was defined in `data_helper.py`

    e.g.

    https://wgetsnaps.github.io/tdcj-state-tx-us-2018/death_row/dr_offenders_on_dr.html


    A helper function that is "aware" that the data was scraped
        From the DATA_SRC_URL as specified in `data_helper.py`, e.g.

            https://example.com/death_row/dr_offenders_on_dr.html

        and knows that a hyperlink href attribute of

            'dr_info/doejohn.html'

        Should resolve to something like:

            'https://example.com/death_row/dr_info/doejohn.html'

        Note that 'https://example.com/death_row/...' is obviously
         not our data source. I'm using it as a placeholder for
         whatever is in data_helper.py

    Pre-reqs:
      The DATA_SRC_URL is defined in a module accessible to this
        script as:

        from data_helper import DATA_SRC_URL

    Args:
      href: a <str> object

    Returns:
      <str>
    """
    #### fill in yourself
    #### could be a one-liner with proper use of the urljoin() function...
    from data_helper import DATA_SRC_URL
    print(href)
    print("Print working?")
    return urljoin(DATA_SRC_URL, href)
