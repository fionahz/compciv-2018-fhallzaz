import requests

def print_hedz(url='https://www.stanford.edu/news/'):
    """
    url can point to any website, but by default, it points to the
    official Stanford News website

    This function does not return anything. It just prints to output.
    """

    # Get all text from an html page
    txt = fetch_html(url)

    # Get all lines of text from the raw html that contains h3 and <a
    htags = parse_headline_tags(txt)

    # For each line in the set from the line above, extract the human-readable text
    # and print it
    for tag in htags:
        hedtxt = extract_headline_text(tag)
        print(hedtxt)


def extract_headline_text(txt):
    """
    The `txt` argument is a string, ostensibly text that looks like what the HTML
    is for headlines on Stanford's news site, e.g.

        <h3><a href='https://news.stanford.edu/2018/01/1/hello-stanford>Hello Stanford</a></h3>

    This function returns a string, e.g. "Hello Stanford"
    """
    # Split the given line of html on the end of tags
    split_on_close = txt.split('>')

    # Loop through each item in the split string
    #for split_string in split_on_close:
        # If the item is not empty and does not begin with the opening of a tag
    #    if split_string != "":
    #        if split_string[0] != '<':
    #            final_split = split_string.split('<')
    #            return final_split[0]

    correct_tag = split_on_close[2]
    split_ctag = correct_tag.split('<')
    
    return split_ctag[0]

    # Return value if no 'human-readable' text is found in the line
    #return "Error: Sorry, we couldn't find any human-readable text on that page!"


def parse_headline_tags(txt):
    """
    The `txt` argument is a string, ostensibly text that looks like the raw HTML
      that can be found at https://wgetsnaps.github.io/stanford-edu-news/news/simple.html

    This function returns a list of strings, each string
        should look like the raw HTML for a standard Stanford news headline, e.g.

          [
            '<h3><a href='https://news.stanford.edu/2018/01/1/hello-stanford>Hello Stanford</a></h3>',
            '<h3><a href='https://news.stanford.edu/2018/01/1/bye-stanford>Bye Stanford</a></h3>'
          ]
    """
    # Splits the given raw html into lines
    prelim_headlinez = txt.splitlines()
    
    return_list = []

    # Loops through each line and saves it if it contains h3 and <a (To isolate headlines)
    for line in prelim_headlinez:
        free_line = line.strip()
        if "h3" in free_line and "<a" in free_line:
            return_list.append(free_line)

    return return_list



def fetch_html(url):
    """
    The `url` argument should be string, representing a URL for a webpage

    This function returns another string -- the raw text (i.e. HTML) found at the given URL
    """
    myreq = requests.get(url)
    txt = myreq.text
    return txt

