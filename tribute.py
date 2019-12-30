import pandas as pd
import requests
import bs4 as BeautifulSoup

now_playing_titles = []
new_this_week_titles = []
new_dvd_titles = []
box_office_numbers = []
box_office_titles = []

page = requests.get('https://www.tribute.ca/')

soup = BeautifulSoup.BeautifulSoup(page.content, 'html.parser')

now_playing = soup.find(class_='slickwrapper')
new_this_week = soup.find(class_='home_new_this_week')
new_dvd = soup.find(class_='home_new_dvd')

print('Now Playing:')
for link in now_playing.find_all('a'):
    if link.parent.name == 'p':
        if link.get('title') != None:
            now_playing_titles.append(link.get('title'))
print(now_playing_titles)

print('\nNew This Week:')
for link in new_this_week.find_all('a'):
    if link.parent.name == 'p':
        if link.get('title') != None:
            new_this_week_titles.append(link.get('title'))
print(new_this_week_titles)

print('\nNew in DVD:')
for link in new_dvd.find_all('a'):
    if link.parent.name == 'p':
        if link.get('title') != None:
            new_dvd_titles.append(link.get('title'))
print(new_dvd_titles)

#fix with a better solution
box_office_titles = [title.get('title')[0:len(title.get('title'))-11] for movie in soup.find_all(class_='movie-name') for title in movie.find_all('a')]
box_office_numbers = [float(number.get_text()[1:-1]) for number in soup.find_all(class_='movie-numbers')]

box_office_df = pd.DataFrame({'Title':box_office_titles, 'Money (M)':box_office_numbers})
box_office_df['Title'] = box_office_df['Title'].replace('Movie Info', 'test')
box_office_df.index += 1

print('\n')

print(box_office_df)
