
import os
import sys
import csv
import exceptions

sys.path.insert(0, './Apriori-Master')
import apriori


""" 
	4. Recommendit - Output Query Subreddit with specific support & confidence levels
	Utilities: " Uncomment line in __main__ to save all the best result "
"""

# resources file
subredditlist_file = "./Resources/subreddit_list.txt"
csvItem_file = "./Resources/itemset_transaction.csv"
tempFile_path = "./Resources/temp_transaction.csv"

def get_all_recommendation( sup, con):
	""" function to save all of the best recommendation result """
	temp_file = apriori.dataFromFile(tempFile_path)
	items, rules = apriori.runApriori(temp_file, sup, con)
	#lastresult =
	apriori.printResults(items,rules)
	os.remove(tempFile_path)
	#return lastresult

def create_temporary_file(subreddit):
	""" create .db file template 
		that query subreddit appeared """

	tempItemset = list()
	with open(csvItem_file) as csvFile:
		csvReader = csv.reader(csvFile)
		itemset_list = list(csvReader)
	
		for itemset in itemset_list:
			for item in itemset:
				if subreddit.lower() == item.lower():
					tempItemset.append(itemset)
		
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

""" __main__ """

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
			#recommendation = 
			get_all_recommendation(support,confidence)
			# print recommendation result on specific subreddit
			for subreddit in recommendation:
				print subreddit
			print '----------------------------------'
			yesno = raw_input("Save all result with (s="+str(support) + " and c=" + str(confidence)+") (y/n):")
			if yesno.lower() == "y" or yesno.lower() == "yes":
				print 'Saving ...'
				#save_result_path()
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
		
