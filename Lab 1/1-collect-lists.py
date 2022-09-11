import os
import csv
import bs4


def write_in_xls(song_urls):
    with open('links/1-song-page-urls.csv', mode='w', newline='', encoding='utf-8') as url_list_file:
        unit_url_writer = csv.writer(
            url_list_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for url in song_urls:
            unit_url_writer.writerow(url)


songs_page_url = 'https://lyrics71.net/all-lyrics/'

song_urls = []


page_content = os.system('wget ' + songs_page_url + ' -O saved-pages/0-song-list.html')
with open("saved-pages/0-song-list.html", "r+") as rdfile:
    page_content = rdfile.read()
soup = bs4.BeautifulSoup(page_content, 'html.parser')


# tab-1 this section to run in loop
songs_container = soup.find(
    'div', {'class': 'latest-lyrics-container clearfix'}).find_all('li')

if (songs_container != None):
    for song_container in songs_container:
        song_url = song_container.find('a')['href']
        song_urls.append([song_url])

# section end

song_urls = sorted(set(map(tuple, song_urls)))
write_in_xls(song_urls)
