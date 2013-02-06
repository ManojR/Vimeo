Read Me 
========

In this project I have created three .py files. There are as follows :-

1)vimeouser.py
2)vimeostaffpick.py
3)vimeostaffpickusers.py

	Vimeouser.py program is to crawl the vimeo.com website, to get information such as username,their url,paid users or not and upload videos information. These information are stored in search_vimeo table.

	vimeostaffpick.py program is to get the videos url of users from vimeo staffpick channel website and stores the details in staffpick table.

	vimeostaffpickusers.py program is to get the users url from staffpick videos url( ex:-www.vimeo.com/141358) and saves the information in search_staffpick table.

	With use of users url from search_staffpick table we have updated search_vimeo table for the field staffpick as 'Y'.

