from __future__ import division
from decimal import Decimal
from prettytable import PrettyTable
import exceptions
import sys
import traceback
import time

""" 
	6.  Precision Calculator.py
		- 	Comparing Recommendit and PRAW (Existing library) for- 
			evaluate the precision and accuracy level.
		- 	Construct the comparision table using PrettyTable Library.
"""

# Resources file
subredditlist_file = "./Resources/subreddit_list.txt"
praw_recommendation_file = './Resources/Praw_Results/Praw_recommendation.txt'
recommendit_recommendation_file = './Resources/Recommendit_Results/Recommendit_recommendation.txt'
precision_result_file = './Resources/Precision_Results/precision_result.txt'

def get_recommendit_recommendation(subreddit):
	""" Get recommendit recommendation results """"
	# TODO: edit recommendit data
	recommendit_list = list()
	with open(recommendit_recommendation_file) as recommenditFile:
		for item in recommenditFile:
			# split with space
			pattern = item.split()
			try:
				if pattern[0].lower() == subreddit.lower():
					if len(pattern) <= 2:
						return recommendit_list
					else:
						for i in range (2, len(pattern)):
							if pattern[i] != ',':
								recommendit_list.append(pattern[i])
						return recommendit_list
			except exceptions.IndexError, e:
				print e

def get_praw_recommendation(subreddit):
	""" get praw recommendation results """
	praw_list = list()
	with open(praw_recommendation_file) as prawFile:
		for item in prawFile:
			# split with space
			pattern = item.split()
			try:
				if pattern[0].lower() == subreddit.lower():
					if len(pattern) <= 2:
						return praw_list
					else:
						for i in range (2, len(pattern)):
							if pattern[i] != ',':
								praw_list.append(pattern[i])
						return praw_list
				
			except exceptions.IndexError, e:
				print e

def subreddit_found(subreddit):
	""" Finding input subreddit in the list """
	with open(subredditlist_file) as file:
		for i in file:
			# CASE SENSITIVE: space+"\n"
			pattern = i.rstrip(" \n").lower()
			if subreddit.lower() == pattern:
				return True
		return False

def intersection(recommendit, praw):
	""" count shared subreddits """
	intersection_rec = set(recommendit).intersection(praw)
	#print 'intersection set: '+str(intersection_rec)
	print 'intersection = '+str(len(intersection_rec))+' subreddit'
	return len(intersection_rec)

def minimum_len(recommendit, praw):
	""" calculate minimum length of recommendation results """
	return min(len(recommendit), len(praw))

if __name__ == "__main__":
	print '------------------------------------------------'
	print 'Recommendit & Praw comparision table'
	print '------------------------------------------------'
	subreddit = raw_input('input subreddit: /r/')
	
	if subreddit_found(subreddit):
		praw_rec = get_praw_recommendation(subreddit)
		recommendit_rec = get_recommendit_recommendation(subreddit)
	else:
		print "Error: Subreddit not found"
		print "Force to exit ..."
		sys.exit()

	""" create comparision table """

	comparision_table = PrettyTable()
	comparision_table.padding_width = 1

	recommendit_l = list()
	praw_l = list()
	
	# init.
	rec_item = 0
	praw_item = 0

	for recommendit_subr in recommendit_rec:
		recommendit_l.append(recommendit_subr)
		rec_item += 1

	for praw_subr in praw_rec:
		praw_l.append(praw_subr)
		praw_item += 1


	""" Balancing comparision table """
	if rec_item > praw_item:
		for i in range(0,rec_item-praw_item):
			praw_l.append('-')
	if praw_item > rec_item:
		for i in range(0,praw_item-rec_item):
			recommendit_l.append('-')

	comparision_table.add_column("RECOMMENDIT",recommendit_l)
	comparision_table.add_column("PRAW",praw_l)
	
	# out: comparision table
	print comparision_table
	print '------------------------------------------------'

	if len(praw_rec) >= 1 and len(recommendit_rec) >= 1:
		precision = intersection(recommendit_rec, praw_rec) / minimum_len(recommendit_rec, praw_rec)
		print "P-Value = "+str(round(precision*100,2))+"%"
		print '------------------------------------------------'
	else:
		print 'cannot calculate P-Value (one or more recommendation not found)'

	# Ask for saving all of the result from ~4000 subreddit list
	yesno = raw_input("Save all P-Value for all subreddit list? (y/n): ")
	if yesno.lower() == "y" or yesno.lower() == "yes":
		print 'Start saving precision file ...'
		with open(subredditlist_file) as file:
			for subreddit in file:
				try:
					pattern = subreddit.rstrip(" \n").lower()
					praw_recommended = get_praw_recommendation(pattern)
					recommendit_recomended = get_recommendit_recommendation(pattern)

					if len(praw_recommended) >= 1 and len(recommendit_recomended) >= 1:
						precision = intersection(recommendit_recomended, praw_recommended) / minimum_len(recommendit_recomended, praw_recommended)
						
						precision_value = round(precision*100,2)
						precision_result = pattern + " = " + str(precision_value)+"%"

						# write precision value with more than 60.0%
						if precision_value > 60:
							with open(precision_result_file, "a") as precision_file:
								precision_file.write("{}\n".format(precision_result))
								print precision_result
					else:
						# TODO: check case here!
						precision_result = pattern + " = " + "0.0%"
						
				except:
					print('resuming in 5...')
					time.sleep(2)
					continue
	else:
		print 'Bye bye!'
		sys.exit()

	


