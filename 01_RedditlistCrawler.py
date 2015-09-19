import requests
from bs4 import BeautifulSoup
import urllib2 # require python 2.0 

"""
    1.  Get all subreddit name from redditlist.com
        using urllib and BeautifulSoup library
"""

def get_subreddit_list(max_pages):
    """ 
        Get all of the top ~4000 subreddits 
        from http://www.redditlist.com
    """

    page = 1
    subs = []
    print("Getting subreddits...")
    while page <= max_pages:
        print("Crawling Page "+ str(page))
        if page == 1 :
            url = "http://www.redditlist.com"
        else:
            url = "http://www.redditlist.com?page="+str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.findAll("a",{"class":"sfw"}):
            href = link.get("href")
            subs.append(href)
            title = link.string
        # comment
        page += 1

    # comment
    result = []
    subreddits = list(set(subs))
    subreddits_count = 0
    for subreddit in subreddits:
        subreddit_url = "http://reddit.com/r/"
        if subreddit_url in subreddit:
            print subreddit[20:]
            #subreddit_list.append(subreddit[20:])
            with open("./Resources/subreddit_list.txt", "a") as myfile:
                # comment (important)
                myfile.write("{} \n".format(subreddit[20:]))
            subreddits_count += 1
    print("Collect "+str(subreddits_count)+" subreddits")

# Query on 33 PAGES of http://www.redditlist.com
get_subreddit_list(33)