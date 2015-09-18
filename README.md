# Recommendit
Recommendation service for reddit.com communities
REMOTE SERVER: http://kilgallin.com/
# Files Structure
Recommendit Folder
	|- 01_RedditlistCrawler.py :
	|- 02_QueryTopPost.py :
	|- 03_TransactionBuilder.py :
	|- 04_Recommendit.py :
	|- 05_PRAW_Recommend.py :
	|- 06_PrecisionCalculator.py :
		|- Apriori-Master - Apriori Library (mit-license)
		|- Resources - output folder
		|- Paper - Recommendit Paper & References 

# How to Run
Step1: Data Collection and Transformation (out:data)
	$python 01_RedditlistCrawler.py
	$python 02_QueryTopPost.py
	$python 03_TransactionBuilder.py

Step2: Data Preprocessing (out:recommendation result)
	$python 04_Recommendit.py -s [SUPPORT] -c [CONFIDENCE]
	$python 05_PRAW_Recommend.py

Step3: Knowledge Discovery (out:precision value)
	$python 06_PrecisionCalculator.py

# System Requirements
- MAC OS X, Windows, Ubuntu
- Python Version 2.7.10 (Not compatible with Python3.0+)
- Require: sqlite3, BeautifulSoup, uillib2

# Copyright 2015, Jonathan D.Kilgallin & Suphanut Jamonnak, All rights reserved. { jdk72, sj70 @zips.uakron.edu }
