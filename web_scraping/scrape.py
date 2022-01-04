import requests
from bs4 import BeautifulSoup
import pprint #importing Pretty Print
import sys



def sort_stories_by_vote(hn_dict):  #sort articles by votes asecending
    sorted_dict = sorted(hn_dict, key= lambda x:x['votes'], reverse=True)
    return sorted_dict


def create_custom_hn(links, subtext, hn):
#    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()    #gets only article title
        href = links[idx].get('href', None) #get URL or returns 0
        vote = subtext[idx].select('.score') #get just the points on article
        if len(vote):   #if zero means this is a new article and NO points so far
            points = int(vote[0].getText().replace(' points','')) 
            hn.append({'title': title, 'url': href, 'votes':points})
    return hn


def scrap_page(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.titlelink')
    subtext = soup.select('.subtext')
    return links, subtext


passed_url = sys.argv[1]
pages_to_get = int(sys.argv[2])
pre_sorted_hn_list = []

for p in range(1,pages_to_get):
    if pages_to_get == 1:
        end = '/news'
    else:
        end = str('/news?p='+str(p))

    url_to_scrap = 'https://news.'+passed_url+end
    print(url_to_scrap)

    links, subtext = scrap_page(url_to_scrap)    
    pre_sorted_hn_list = create_custom_hn(links, subtext, pre_sorted_hn_list) 

sorted_articles = sort_stories_by_vote(pre_sorted_hn_list)

count = 0
for article in sorted_articles:
    if article['votes'] > 100:
        pprint.pprint(article)
        count += 1 

pprint.pprint(f'/n there are {count} articles with more then 100 points')
