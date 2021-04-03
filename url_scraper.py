import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

source_url_dict = [
                   # "https://www.soccerpunter.com/soccer-statistics/England/Premier-League-2014-2015/results",
                   # "https://www.soccerpunter.com/soccer-statistics/England/Premier-League-2013-2014/results",
                   # "https://www.soccerpunter.com/soccer-statistics/Portugal/Primeira-Liga-2017-2018/results",
                   # "https://www.soccerpunter.com/soccer-statistics/Portugal/Primeira-Liga-2016-2017/results",
                   # "https://www.soccerpunter.com/soccer-statistics/Portugal/Primeira-Liga-2015-2016/results",
                   # "https://www.soccerpunter.com/soccer-statistics/Portugal/Primeira-Liga-2014-2015/results",
                   # "https://www.soccerpunter.com/soccer-statistics/Portugal/Primeira-Liga-2013-2014/results",
                   # "https://www.soccerpunter.com/soccer-statistics/Turkey/Super-Lig-2017-2018/results",
                   # "https://www.soccerpunter.com/soccer-statistics/Turkey/Super-Lig-2016-2017/results",
                   # "https://www.soccerpunter.com/soccer-statistics/Turkey/Super-Lig-2015-2016/results",
                   # "https://www.soccerpunter.com/soccer-statistics/Turkey/Super-Lig-2014-2015/results",
                   # "https://www.soccerpunter.com/soccer-statistics/Turkey/Super-Lig-2013-2014/results",
                   # "https://www.soccerpunter.com/soccer-statistics/Italy/Serie-A-2017-2018/results",
                   # "https://www.soccerpunter.com/soccer-statistics/Italy/Serie-A-2016-2017/results",
                   # "https://www.soccerpunter.com/soccer-statistics/Italy/Serie-A-2015-2016/results",
                   # "https://www.soccerpunter.com/soccer-statistics/Italy/Serie-A-2014-2015/results",
                   # "https://www.soccerpunter.com/soccer-statistics/Italy/Serie-A-2013-2014/results",
                   # "https://www.soccerpunter.com/soccer-statistics/Netherlands/Eredivisie-2017-2018/results",
                   # "https://www.soccerpunter.com/soccer-statistics/Netherlands/Eredivisie-2016-2017/results",
                   "https://www.soccerpunter.com/soccer-statistics/Netherlands/Eredivisie-2015-2016/results",
                   "https://www.soccerpunter.com/soccer-statistics/Netherlands/Eredivisie-2014-2015/results",
                   "https://www.soccerpunter.com/soccer-statistics/Netherlands/Eredivisie-2013-2014/results",
                   "https://www.soccerpunter.com/soccer-statistics/England/Championship-2017-2018/results",
                   "https://www.soccerpunter.com/soccer-statistics/England/Championship-2016-2017/results",
                   "https://www.soccerpunter.com/soccer-statistics/England/Championship-2015-2016/results",
                   "https://www.soccerpunter.com/soccer-statistics/England/Championship-2014-2015/results",
                   "https://www.soccerpunter.com/soccer-statistics/England/Championship-2013-2014/results",
                   "https://www.soccerpunter.com/soccer-statistics/Spain/La-Liga-2017-2018/results",
                   "https://www.soccerpunter.com/soccer-statistics/Spain/La-Liga-2016-2017/results",
                   "https://www.soccerpunter.com/soccer-statistics/Spain/La-Liga-2015-2016/results",
                   "https://www.soccerpunter.com/soccer-statistics/Spain/La-Liga-2014-2015/results",
                   "https://www.soccerpunter.com/soccer-statistics/Spain/La-Liga-2013-2014/results",
                   "https://www.soccerpunter.com/soccer-statistics/Germany/Bundesliga-2017-2018/results",
                   "https://www.soccerpunter.com/soccer-statistics/Germany/Bundesliga-2016-2017/results",
                   "https://www.soccerpunter.com/soccer-statistics/Germany/Bundesliga-2015-2016/results",
                   "https://www.soccerpunter.com/soccer-statistics/Germany/Bundesliga-2014-2015/results",
                   "https://www.soccerpunter.com/soccer-statistics/Germany/Bundesliga-2013-2014/results",
                   "https://www.soccerpunter.com/soccer-statistics/France/Ligue-1-2017-2018/results",
                   "https://www.soccerpunter.com/soccer-statistics/France/Ligue-1-2016-2017/results",
                   "https://www.soccerpunter.com/soccer-statistics/France/Ligue-1-2015-2016/results",
                   "https://www.soccerpunter.com/soccer-statistics/France/Ligue-1-2014-2015/results",
                   "https://www.soccerpunter.com/soccer-statistics/France/Ligue-1-2013-2014/results",
                   "https://www.soccerpunter.com/soccer-statistics/Sweden/Allsvenskan-2013/results",
                   "https://www.soccerpunter.com/soccer-statistics/Sweden/Allsvenskan-2014/results",
                   "https://www.soccerpunter.com/soccer-statistics/Sweden/Allsvenskan-2015/results",
                   "https://www.soccerpunter.com/soccer-statistics/Sweden/Allsvenskan-2016/results",
                   "https://www.soccerpunter.com/soccer-statistics/Sweden/Allsvenskan-2017/results",
                   "https://www.soccerpunter.com/soccer-statistics/Sweden/Allsvenskan-2018/results",
                   "https://www.soccerpunter.com/soccer-statistics/China-PR/CSL-2018/results",
                   "https://www.soccerpunter.com/soccer-statistics/China-PR/CSL-2017/results",
                   "https://www.soccerpunter.com/soccer-statistics/China-PR/CSL-2016/results",
                   "https://www.soccerpunter.com/soccer-statistics/China-PR/CSL-2015/results",
                   "https://www.soccerpunter.com/soccer-statistics/China-PR/CSL-2014/results",
                   "https://www.soccerpunter.com/soccer-statistics/China-PR/CSL-2013/results",
                   "https://www.soccerpunter.com/soccer-statistics/USA/MLS-2018/results",
                   "https://www.soccerpunter.com/soccer-statistics/USA/MLS-2017/results",
                   "https://www.soccerpunter.com/soccer-statistics/USA/MLS-2016/results",
                   "https://www.soccerpunter.com/soccer-statistics/USA/MLS-2015/results",
                   "https://www.soccerpunter.com/soccer-statistics/USA/MLS-2014/results",
                   "https://www.soccerpunter.com/soccer-statistics/USA/MLS-2013/results",
                   "https://www.soccerpunter.com/soccer-statistics/Brazil/Serie-A-2018/results",
                   "https://www.soccerpunter.com/soccer-statistics/Brazil/Serie-A-2017/results",
                   "https://www.soccerpunter.com/soccer-statistics/Brazil/Serie-A-2016/results",
                   "https://www.soccerpunter.com/soccer-statistics/Brazil/Serie-A-2015/results",
                   "https://www.soccerpunter.com/soccer-statistics/Brazil/Serie-A-2014/results",
                   "https://www.soccerpunter.com/soccer-statistics/Brazil/Serie-A-2013/results"]

browser = webdriver.Chrome()

for source_url in source_url_dict:

    filename = source_url[47:-8]
    filename = filename.replace('/', '_')
    filename = filename.replace('-', '_')
    filename += '_urls.csv'

    with open(filename, 'wb') as csvfile:
        fieldnames = ['url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        url = source_url

        browser.get(url)

        time.sleep(5)

        for stats_url in browser.find_elements(By.XPATH, '//a[@class="smallDetails"]'):

            actual_url = stats_url.get_attribute('href').encode('utf-8')

            writer.writerow({'url': actual_url})

            print actual_url

    csvfile.close()
browser.close()
