
import os
import sys
import csv
import exceptions
import signal

sys.path.insert(0, './Apriori-Master')
import apriori

# TODO: get all subreddit recommendation!

""" 
	4. Recommendit - Output Query Subreddit with specific support & confidence levels
	Utilities: " Uncomment line in __main__ to save all the best result "
	(default s= 0.1 - 0.2 c= 0.5 - 0.7) -> set s= 0.05 & c=0.60 for the best result.
"""

# resources file
subredditlist_file = "./Resources/subreddit_list.txt"
csvItem_file = "./Resources/itemset_transaction.csv"
tempFile_path = "./Resources/temp_transaction.csv"
recommendit_result_file = "./Resources/Recommendit_Results/Recommendit_recommendation.txt"

class TimeoutException(Exception):   # Custom exception class
    pass

def timeout_handler(signum, frame):   # Signal handler
    raise TimeoutException

# Change the behavior of SIGALRM
signal.signal(signal.SIGALRM, timeout_handler)

def get_all_recommendation( sup, con, subreddit):

	""" function to save all of the best recommendation result """
	temp_file = apriori.dataFromFile(tempFile_path)
	items, rules = apriori.runApriori(temp_file, sup, con)
	recommendation_set = list()
	for rule, confidence in rules:
		pre, post = rule
		for item in pre:
			if item not in recommendation_set and item.lower() != subreddit.lower():
				recommendation_set.append(item)
	
	os.remove(tempFile_path)
	return recommendation_set
	

def create_temporary_file(subreddit):
	""" create .db file template 
		that query subreddit appeared """

	tempItemset = list()
	with open(csvItem_file) as csvFile:
		csvReader = csv.reader(csvFile)
		itemset_list = list(csvReader)
		itemset_count = 0
		for itemset in itemset_list:
			for item in itemset:
				# For more accurate pull out for 3 item in each transaction
				if subreddit.lower() == item.lower() and len(itemset) >= 3:
					tempItemset.append(itemset)
					itemset_count += 1

		print 'get '+str(itemset_count)+' item-set'
	
	with open(tempFile_path, 'wb') as fp:
		writer = csv.writer(fp, delimiter=',')
		writer.writerows(tempItemset)



""" Utilities functions() """

def subreddit_found(subreddit):
	""" Query subreddit and Create a Temp file """

	with open(subredditlist_file) as file:
		for i in file:
			# CASE SENSITIVE: space+"\n"
			pattern = i.rstrip(" \n").lower()
			if subreddit.lower() == pattern:
				return True
		return False

def check_numeric_types(value, value2):
	if isinstance(value, basestring) or isinstance(value2, basestring):
		print '----------------------------------'
		print 'ERROR: support and confidence not handling this type'
		exit_recommendit()
	else: return

def exit_recommendit():
	print 'force to exit program ...'
	sys.exit()

if __name__ == "__main__":

	print '----------------------------------'
	subreddit_input = raw_input('Query Subreddit: ')

	# Find subreddit in the list
	if subreddit_found(subreddit_input):
		try:
			support = input('support = ')
			confidence = input('confidence = ')
			check_numeric_types(support , confidence)
			print '----------------------------------'
			print "Generating "+subreddit_input+" Recommendation (s="+str(support) + ", c=" + str(confidence)+")"

			create_temporary_file(subreddit_input)
			result = get_all_recommendation(support,confidence, subreddit_input)
			for item in result:
				print 'r/'+str(item)
			print '----------------------------------'

			yesno = raw_input("Save all result with (s="+str(support) + " and c=" + str(confidence)+") (y/n):")
			if yesno.lower() == "y" or yesno.lower() == "yes":

				""" save all file """
				with open(subredditlist_file) as file:
					for subreddit in file:

						# alarm for timeout exception
						signal.alarm(20) 

						# CASE SENSITIVE: space+"\n"
						try:

							pattern = subreddit.rstrip(" \n").lower()
							recommend_result = pattern + " => "
							
							create_temporary_file(pattern)

							result = get_all_recommendation(support,confidence, pattern)

							subr_count = 0
							for subr in result:
								
								if subr_count == 0:
									recommend_result += " "+subr
								else:
									recommend_result += " , "+subr
								subr_count += 1

							with open(recommendit_result_file, "a") as recommendit_file:
								recommendit_file.write("{}\n".format(recommend_result))
								print recommend_result

						except TimeoutException:
							print 'time out!'
							# Continue collecting results
							continue

						else:
							# Reset the alarm
							signal.alarm(0)
			else:
				print 'Bye bye!'
				exit_recommendit() 


		except (exceptions.NameError,exceptions.SyntaxError), e:
			print '----------------------------------'
			#print e
			print 'ERROR: support and confidence not handling this type'
			exit_recommendit()
	else:
		print '/r/'+subreddit_input+' not found in the basket'
		exit_recommendit()
		
