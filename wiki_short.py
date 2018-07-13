import requests
import re
from bs4 import BeautifulSoup
import time
import heapq


def findWikiLinks(page):
    page = 'https://en.wikipedia.org/wiki/' + page
    # print(page)
    page = requests.get(page)
    soup = BeautifulSoup(page.content, 'html.parser')
    wiki_tags = set([])
    for a in soup.find_all('a', href=True):
        href = a['href']
        if re.match(r'^/wiki/', href) and not ':' in href:
            wiki_tags.add(href[6:])
    return wiki_tags


def findWikiLadder(start_page, end_page):
    is_visited = set([])
    is_visited.add(start_page)
    wiki_ladder = []
    # wiki_ladder.append([start_page])
    heapq.heappush(wiki_ladder, (findCommonLinks(start_page), [start_page]))
    if start_page == end_page:
        return wiki_ladder

    while wiki_ladder:
        partial_ladder = wiki_ladder.pop()
        print(partial_ladder)
        neighbour_tags = findWikiLinks(partial_ladder[1][-1])

        if end_page in neighbour_tags:
            partial_ladder = partial_ladder[1].copy()
            partial_ladder.append(end_page)
            return partial_ladder

        for each in neighbour_tags:
            if each not in is_visited:
                is_visited.add(each)
                temp_ladder = partial_ladder[1].copy()
                temp_ladder.append(each)
                common_links = findCommonLinks(each)
                heapq.heappush(wiki_ladder, (common_links, temp_ladder))


end_ladder = findWikiLinks('PDF')


def findCommonLinks(link):
    ladder1 = findWikiLinks(link)
    count = 0
    for each in ladder1:
        if each in end_ladder:
            count += 1
            # print(each)
    # print(count, link)
    return count

start_time = time.time()
print(findWikiLadder('Fruit', 'PDF'))
print("--- %s seconds ---" % (time.time() - start_time))