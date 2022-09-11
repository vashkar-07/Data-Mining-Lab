import os
import csv
import bs4

def read_song_page_urls():
    song_urls = []
    with open('links/1-song-page-urls.csv') as main_url_csv:
        readCSV = csv.reader(main_url_csv)

        for row in readCSV:
            song_urls.append(row[0])

    return song_urls


def write_in_xls(song_lyrics):
    with open('links/2-song-lyrics.csv', mode='a', newline='',encoding='utf-8') as url_list_file:
        unit_url_writer = csv.writer(url_list_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for song_lyric in song_lyrics:
            unit_url_writer.writerow(song_lyric)


song_urls = read_song_page_urls()


song_count = len(song_urls)
for i in range(song_count):
    print(song_urls[i])
    page_content = os.system('wget -q ' + song_urls[i] + ' -O saved-pages/2-song-page.html')
    with open('saved-pages/2-song-page.html', "r+") as rdfile:
        page_content = rdfile.read()
    soup = bs4.BeautifulSoup(page_content, 'html.parser')

    try:
        song_title = soup.find("title").getText()
        content = soup.find(class_='lyric-text margint20 marginb20').find_all('p')
        details = ''
        
        for j in content[0].find_all('strong'):
            details += j.text
        
        attList = ["শিরোনামঃ","কন্ঠঃ","ব্যান্ডঃ","অ্যালবামঃ","সুরঃ","কথাঃ","সঙ্গীতঃ","টিউনঃ","মুভিঃ"]
        attName = []

        for att in attList:
            titties = ''
            try:
                flag = False
                for k in range(details.index(att),len(details)):
                    if details[k] == '\n':
                        break
                    if details[k] == ' ':
                        flag = True
                    if flag:
                        titties += details[k]
                    
                titties.split(att)
            except:
                titties = None
            attName.append(titties)

        song_title = attName[0]
        singer = attName[1]
        bandName = attName[2]
        album = attName[3]
        composer = attName[4]
        lyricist = attName[5]
        director = attName[6]
        tune = attName[7]
        movie = attName[8]

        lyrics = ''
        for j in range(1, len(content)):
            lyrics += content[j].text

        # Header Row
        # "শিরোনাম","কন্ঠ","ব্যান্ড","অ্যালবাম","সুর","কথা","সঙ্গীত","টিউন","মুভি", "Lyrics"
        write_in_xls([[song_title, singer, bandName, album, composer, lyricist, director, tune, movie, lyrics]])
    except AttributeError:
        pass
