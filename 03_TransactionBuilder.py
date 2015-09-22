import csv
import sqlite3
import unicodedata

""" 
	3.  Transaction Builder - query userpost .db files 
		and convert its to itemsets and buckets in subreddit_items.txt
"""

subreddit_list = list()
databasename = './Resources/subreddit_post_alltime.db'
sql = sqlite3.connect(databasename)
cur = sql.cursor()

def main():
	""" main transaction builder """
	author_list = list()
	cur.execute ("SELECT DISTINCT author FROM reddit_post")
	for row in cur:
		cur2 = sql.cursor()
		cur2.execute ("SELECT DISTINCT author,subreddit FROM reddit_post WHERE author =\""+row[0]+"\"")
		count = 0
		subreddit_set = set()
		for row2 in cur2:
			subreddit = unicodedata.normalize('NFKD', row2[1]).encode('ascii','ignore')
			subreddit_set.add(subreddit)
			count += 1
		print "total: "+str(count)+" subreddit"
		subreddit_list.append(list(subreddit_set))
		with open('./Resources/itemset_transaction.csv', 'wb') as fp:
			a = csv.writer(fp, delimiter=',')
			a.writerows(subreddit_list)

if __name__ == '__main__':
	main()
