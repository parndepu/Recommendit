import praw
import csv
import time
import sqlite3

"""
    2.  PRAW library - Crawling top 1000 post of all time
        from the existing ~4000 subreddit list
"""

user_agent = " Crawling top post in subreddit"

r = praw.Reddit(user_agent=user_agent)

# Global Variables
databasename = './Resources/subreddit_post_alltime.db'
sql = sqlite3.connect(databasename)
cur = sql.cursor()
cur.execute(('CREATE TABLE IF NOT EXISTS reddit_post(created TEXT, score INT, author TEXT, num_comments INT,'
'over_18 INT, subreddit TEXT, domain TEXT)'))



def insert_toDB(created, author, subreddit, score, nsfw, num_comment, url):
    """ Insert to subreddit_post_alltime.db """

    postdata = [created,score,author,num_comment,nsfw,subreddit,url]
    print (postdata)
    cur.execute('INSERT INTO reddit_post VALUES(?, ?, ?, ?, ?, ?, ?)', postdata)
    sql.commit()
    

def searchtop(header):
    """ Search 1000 post of alltime on each subreddit """

    post_count = 0
    # edit limit to 100 if you want to
    while True:
            try:
                subreddit = r.get_subreddit(header).get_top_from_all(limit = 1000)
                break
            except:
                traceback.print_exc()
                print('resuming in 5...')
                time.sleep(5)
                continue
            break

    for post in subreddit:
                if not post.author:
                    name = '[deleted]'
                else:
                    name = post.author.name

                created_time = time.strftime("%D", time.localtime(float(post.created_utc)))
                author = name
                subreddit = post.subreddit.display_name
                score = post.score 
                nsfw = post.over_18
                num_comment = post.num_comments
                url = post.domain
                
                insert_toDB(created_time, author, subreddit, score, nsfw, num_comment, url)
                post_count+=1

    print ("getting total: ", post_count, " post")
            


def main():
    """ main """

	r = praw.Reddit(user_agent = user_agent)
    # edit your redditlist file 
	with open('./Resources/subreddit_list.txt') as f:
            subreddit_list = f.readlines()
            #count = 0
            for subs in subreddit_list:
                subreddit = subs.split()
                print ("Start searching top 1000 post in /r/", subreddit[0])
                searchtop(subreddit[0])

if __name__ == '__main__':
	main()