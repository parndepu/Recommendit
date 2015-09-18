# Recommendit
Recommendation service for reddit.com communities

## Files Structure 

	Recommendit Folder 	
		|- 01_RedditlistCrawler.py
		|- 02_QueryTopPost.py
		|- 03_TransactionBuilder.py
		|- 04_Recommendit.py
		|- 05_PRAW_Recommend.py
		|- 06_PrecisionCalculator.py
		|- Apriori-Master - Apriori Library (mit-license)
			|- apriori.py
			|- ...
		|- Resources - output folder
			|- itemset_transaction.csv  
			|- subreddit_list.txt
			|- ...
		|- Paper - Recommendit Paper & References 
			|- ...

## How to Run
1. Data Collection and Transformation (out:data)
	- $python 01_RedditlistCrawler.py
	- $python 02_QueryTopPost.py
	- $python 03_TransactionBuilder.py

2. Data Preprocessing (out:recommendation result)
	- $python 04_Recommendit.py
	- $python 05_PRAW_Recommend.py

3. Knowledge Discovery (out:precision value)
	- $python 06_PrecisionCalculator.py

## System Requirements
- MAC OS X, Windows, Ubuntu
- Python Version 2.7.10 (Not compatible with Python3.0+)
- Require: sqlite3, BeautifulSoup, uillib2

*Copyright 2015, Jonathan D.Kilgallin & Suphanut Jamonnak, All rights reserved. { jdk72, sj70 @zips.uakron.edu }*
[REMOTE SERVER](http://kilgallin.com/)
