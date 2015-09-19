import time
import praw
import traceback


""" 
	5.  PRAW - get_subreddit_recommendations(subreddits,omit)
		Comparing PRAW and Recommendit Engines for Precision
		and accuracy.
"""

# PRAW user_agent
user_agent = " PRAW Recommendation Crawler / J.D., Suphanut Jamonnak"


PRAW_result_file = "./Resources/PRAW_Results/Praw_recommendation.txt"
subredditlist_file = "./Resources/subreddit_list.txt"

def collect_PRAW_recommendation(subreddit):

	recommend_result = subreddit + " => "
	recommendation = list()
	r = praw.Reddit(user_agent=user_agent)

	# Select top 50 subreddit for pricision results
	recommendation = r.get_subreddit_recommendations([subreddit])

	count = 0
	for result in recommendation:
		if count == 0:
			recommend_result += " "+str(result)
		else:
			recommend_result += " , "+str(result)
		count += 1
	return recommend_result

def main():

	recommendation = list()
	r = praw.Reddit(user_agent=user_agent)

	# Select top 50 subreddit for pricision results
	with open(subredditlist_file) as file:
		
		for subreddit in file:
			# CASE SENSITIVE: space+"\n"
			try:
				pattern = subreddit.rstrip(" \n").lower()
				result = collect_PRAW_recommendation(pattern)
				with open(PRAW_result_file, "a") as PRAW_file:
					print result
					PRAW_file.write("{}\n".format(result))

			except:
				traceback.print_exc()
				print('resuming in 5...')
				time.sleep(5)
				continue

if __name__ == '__main__':
	main()