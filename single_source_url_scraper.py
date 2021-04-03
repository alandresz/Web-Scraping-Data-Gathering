import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By




with open('urls.csv', 'wb') as csvfile:
    fieldnames = ['url']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    url = 'https://www.soccerpunter.com/soccer-statistics/England/Premier-League-2015-2016/results'

    browser = webdriver.Chrome()
    browser.get(url)

    time.sleep(5)

    for stats_url in browser.find_elements(By.XPATH, '//a[@class="smallDetails"]'):

        actual_url = stats_url.get_attribute('href').encode('utf-8')

        writer.writerow({'url': actual_url})

        print actual_url

    csvfile.close()
    browser.close()
