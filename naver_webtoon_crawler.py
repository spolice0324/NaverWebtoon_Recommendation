from selenium import webdriver
from bs4 import BeautifulSoup as bs
from time import sleep
from selenium.webdriver.common.by import By

# 네이버 웹툰 페이지 열기
nw_url = 'https://comic.naver.com/webtoon/weekday'
chromedriver_url = '다운로드/chromedriver'
driver = webdriver.Chrome(chromedriver_url)
driver.get(nw_url)

# 클릭할 수 있는 제목 리스트 가져오기
titles = driver.find_elements(By.CLASS_NAME, "title")

# 정보들을 담을 리스트 정의하기
id_list = []
title_list = []
author_list = []
day_list = []
genre_list = []
story_list = []
platform_list = []
webtoon_url_list = []
thumbnail_url_list = []

webtoon_id = 0

# 웹툰 개수만큼 반복하기
for i in range(len(titles)):
    print("\rprocess: " + str(i + 1) + " / " + str(len(titles)), end="")

    # 웹페이지가 로딩되기도 전에 코드가 실행되는 것을 방지하기 위한 기다림
    sleep(0.5)

    # 0번째 웹툰, 즉 월요일 첫번재 웹툰부터 클릭해서 해당 페이지로 이동하기
    titles = driver.find_elements(By.CLASS_NAME, "title")
    titles[i].click()

    # 이동한 페이지의 html 코드 가져오기
    html = driver.page_source
    soup = bs(html, 'html.parser')

    # 제목 정보 가져오기
    title = soup.find('span', {'class': 'title'}).text

    # 요일 정보 가져오기
    day = soup.find('ul', {'class': 'category_tab'})
    day = day.find('li', {'class': 'on'}).text[0:1]

    # 만약 연재 요일이 2개 이상이라서 이미 저장했던 웹툰이라면 요일만 추가하고 넘어가기
    if title in title_list:
        day_list[title_list.index(title)] += ', ' + day
        driver.back()
        continue

    # 나머지 정보 수집하기
    thumbnail_url = soup.find('div', {'class': 'thumb'}).find('a').find('img')['src']
    author = soup.find('span', {'class': 'wrt_nm'}).text[8:]
    author = author.replace(' / ', ', ')
    genre = soup.find('span', {'class': 'genre'}).text.split(", ")[1]
    story = soup.find('div', {'class': 'detail'}).find('p').text

    # 정보들을 리스트에 담기
    id_list.append(webtoon_id)
    title_list.append(title)
    author_list.append(author)
    day_list.append(day)
    genre_list.append(genre)
    story_list.append(story)
    platform_list.append("네이버")
    webtoon_url_list.append(driver.current_url)
    thumbnail_url_list.append(thumbnail_url)

    # 뒤로 가기
    driver.back()
    webtoon_id += 1
    sleep(0.5)

import pandas as pd

total_data = pd.DataFrame()

total_data['id'] = id_list
total_data['title'] = title_list
total_data['author'] = author_list
total_data['day'] = day_list
total_data['genre'] = genre_list
total_data['story'] = story_list
total_data['platform'] = platform_list
total_data['webtoon_url'] = webtoon_url_list
total_data['thumbnail_url'] = thumbnail_url_list

# 따로 인덱스를 생성하지 않고 id를 인덱스로 정하기
total_data.set_index('id', inplace=True)

# CSV 파일로 저장하기
total_data.to_csv("네이버 웹툰 정보.csv", encoding='utf-8-sig')
