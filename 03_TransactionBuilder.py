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

"""
def buildTransaction(author, posts):
	Build subreddit items transaction

	print 'Build Username:' + author
	key = (author)
	author_items = key
	subreddit_set = set()
	temp_subreddit_set = set()
	for post in posts:
		subreddit = post[5]
		if key == post[2] and subreddit not in temp_subreddit_set:
			temp_subreddit_set.add(subreddit)
			subreddit_set.add(subreddit)

	#print list(subreddit_set)
	subreddit_list.append(list(subreddit_set))

	with open('./Resources/itemset_transaction.csv', 'wb') as fp:
		a = csv.writer(fp, delimiter=',')
		a.writerows(subreddit_list)"""
			


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

	"""
		for author in row:
			cur2 = sql.cursor()
			cur2.execute ("SELECT DISTINCT subreddit,author FROM reddit_post WHERE author =\""+author+"\"")
			cur2.fetchone()[0]

	for row in cursor:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "ADDRESS = ", row[2]
   print "SALARY = ", row[3], "\n" """

	"""
	print 'Start Transaction Builder'
	csvFile = "./Resources/subreddit_post_alltime.csv"
	# open userpostdata.csv
	with open(csvFile) as content:
		csvReader = csv.reader(content)
		# Skip csv header
		csvReader.next()
		posts = list(csvReader)
		author_set = set()
		for post in posts:
			# get author name & subreddit name
			author = post[2]
			if author not in author_set and author != '[deleted]':
				# author_post patterns
				author_set.add(author)
				# write file - subreddit items dataset
				buildTransaction(author, posts)"""


if __name__ == '__main__':
	main()
