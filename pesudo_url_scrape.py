## this is psuedo code of what I want to do ##
#
#
#
#--------- this code will extract a url link form RCP and copy it into a csv file ----------#
#
#
#
# NOTE: Go into the code, create a new file for url column and create a new dictionary each time the url is needed
#       >> This means that every time you see 'pollster_xyz...', put the new addition of url into the master code


# 1. import the packages necessary for code to be successful

# 2. scrape the url from the table with the corresponding poll

# 3. create a way to populate it into a csv file

# 4. import code into master code


from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import re

html_page = urlopen("https://www.realclearpolitics.com/epolls/other/2018_generic_congressional_vote-6185.html")
page = soup(html_page)
links = []

for link in page.findAll('a'):
    links.append(link.get('href'))

# write new polls to the csv
with open("url_link_sheet_bri.csv", "a", newline='') as f:
	writer=csv.writer(f, delimiter=',')
	for links in page:
        writer.writerow(links)

print(links)


