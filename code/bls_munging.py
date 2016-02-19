# crawls and scrapes the data from the bls website for recent job openings and massive layoff
# the layoff data is only till jan 2013 and hence I took the job openings for the same period and month.
# i.e Jan 2013

from bs4 import BeautifulSoup
import urllib2
import re
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt


def create_plot(industry, opening, dataset):
    pos = np.arange(len(industry))
    width = 1.0
    ax = plt.axes()
    ax.set_xticks(pos + (width / 2))
    ax.set_xticklabels(industry)
    ax.set_xlabel('Name of the Industries')
    ax.set_ylabel('Number in Thousands')
    ax.set_title(dataset)

    plt.bar(pos, opening, width, color='r')
    plt.show()

def scrape_page(crawl_url, url_type):
    crawl_page = urllib2.urlopen(crawl_url)
    crawl_soup = BeautifulSoup(crawl_page)
    if url_type == 'job':
        text = crawl_soup.find("div", class_ = "normalnews").contents[0].get_text()
    else:
        text = crawl_soup.find("div", class_ = "normalnews").get_text()
    first = text.find('Construction')
    last = text.find('Government')
    text = text[first:last]
    text = re.sub('\.', '',text).split('\n')
    industry = []
    opening = []
    for row in text:
        if url_type == 'job':
            row = re.sub('\s+','',row)
            line = row.split('|')
        else:
            line = re.split('  +', row)
        if len(line) > 5 and line[3] != '':
            if url_type == 'layoff' and line[0] != '':
                continue
            if line[3].find('(') == 0:
                line[3] = line[3][1:-1]
            opening.append(int(line[3]))
            if url_type == 'job':
                industry.append(line[0])
            else:
                industry.append(line[1])

    return industry, opening



def main():
    job_url = "http://www.bls.gov/news.release/archives/jolts_03122013.htm"
    layoff_url = "http://www.bls.gov/news.release/archives/mmls_02262013.htm"
    industry, opening = scrape_page(job_url, 'job')
    create_plot(industry, opening,'job openings across the industries for jan 2013')
    industry, opening = scrape_page(layoff_url, 'layoff')
    create_plot(industry, opening,'layoffs across the openings for jan 2013')




# Boiler plate code to call main
if __name__ == '__main__':
    main()
