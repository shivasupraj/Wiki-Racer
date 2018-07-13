import requests
import re
import collections
from bs4 import BeautifulSoup
import time


class WikiRacer:
    def __init__(self, start_page, end_page):
        self.start_page = start_page
        self.end_page = end_page
        self.wiki_ladder = []

    def findWikiLinks(self, page):
        page = 'https://en.wikipedia.org/wiki/' + page
        page = requests.get(page)
        soup = BeautifulSoup(page.content, 'html.parser')
        wiki_tags = set([])
        for a in soup.find_all('a', href=True):
            href = a['href']
            if re.match(r'^/wiki/', href) and not ':' in href:
                wiki_tags.add(href[6:])
        return wiki_tags

    def findWikiLadder(self, start_page, end_page):
        is_visited = set([])
        is_visited.add(start_page)
        self.wiki_ladder = collections.deque()
        self.wiki_ladder.append([start_page])

        if start_page == end_page:
            return wiki_ladder

        while wiki_ladder:
            partial_ladder = wiki_ladder.pop()
            neighbour_tags = self.findWikiLinks(partial_ladder[-1])

            if end_page in neighbour_tags:
                partial_ladder.append(end_page)
                return partial_ladder

            for each in neighbour_tags:
                if each not in is_visited:
                    is_visited.add(each)
                    temp_ladder = partial_ladder.copy()
                    temp_ladder.append(each)
                    wiki_ladder.append(temp_ladder)

    def __str__(self):
        return

start_page = input('Please enter the start page')
end_page = input('Please enter the end page')

wiki_ladder = WikiRacer(start_page, end_page)
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))



