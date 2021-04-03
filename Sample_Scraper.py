import time
import csv
import winsound
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# UNCOMENT TO ALLOW GET PROXY FUNCTION #
# from get_proxy_for_browser import *

# Beep Settings #
frequency1 = 2500  # Set Frequency To 2500 Hertz
frequency2 = 800
duration = 750  # Set Duration To 1000 ms == 1 second
###################


count = 0

last_line = 45

browser = webdriver.Chrome()

proxy_change_counter = 0


with open('Premier_League_2015_2016.csv', 'ab') as output_file:
    fieldnames = ['season', 'league', 'date', 'home_team', 'away_team', 'home_attacks', 'away_attacks', 'home_danger_attacks', 'away_danger_attacks', 'coef_over_total_2_5', 'w_home', 'draw', 'w_away']
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()

    with open("urls.csv", "rb") as input_file:
        reader = csv.reader(input_file, delimiter="\t")

        for line in reader:
            if count < last_line:
                count += 1
                continue
            else:
                break

        for row in reader:

            url = row[0]

            # RESET IP EVERY 15 USES #
            if proxy_change_counter == 0:
                browser.close()
                browser.quit()
                browser = webdriver.Chrome()
                proxy_change_counter = 15
                winsound.Beep(frequency1, duration)
                print "New Browser Open :)"
            else:
                proxy_change_counter -= 1
            ###########################

            while True:
                try:
                    browser.get(url)
                    break
                except:
                    winsound.Beep(frequency2, duration)
                    time.sleep(1)
                    continue

            while True:
                try:
                    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "matchStats")))
                    leagueAndSeason_string = browser.find_element(By.CLASS_NAME, 'breadcrumb').find_elements(By.TAG_NAME, 'a')[3].text
                    break
                except:
                    winsound.Beep(frequency2, duration)
                    time.sleep(1)
                    browser.get(url)
                    continue

            season = leagueAndSeason_string[-9:]

            league = leagueAndSeason_string[0:-10]

            date = browser.find_element(By.CLASS_NAME, 'matchDate').text

            home_team = browser.find_element(By.ID, 'h2hHead').find_elements(By.XPATH, "//tbody/tr/td/h2")[0].text

            away_team = browser.find_element(By.ID, 'h2hHead').find_elements(By.XPATH, "//tbody/tr/td/h2")[1].text

            home_attacks = browser.find_element(By.CLASS_NAME, 'msType_attacks').find_element(By.CLASS_NAME, 'msValueA').text

            away_attacks = browser.find_element(By.CLASS_NAME, 'msType_attacks').find_element(By.CLASS_NAME, 'msValueB').text

            home_danger_attacks = browser.find_element(By.CLASS_NAME, 'msType_dangerous_attacks').find_element(By.CLASS_NAME, 'msValueA').text

            away_danger_attacks = browser.find_element(By.CLASS_NAME, 'msType_dangerous_attacks').find_element(By.CLASS_NAME, 'msValueB').text


# Get Odds Data #

            odds_url = browser.find_element(By.CLASS_NAME, 'h2hHeaderButton').get_attribute('href').encode('utf-8')

            while True:
                try:
                    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "matchStats")))
                    browser.find_element(By.CLASS_NAME, 'h2hHeaderButton').click()
                    break
                except:
                    winsound.Beep(frequency2, duration)
                    browser.get(url)
                    continue

            while True:
                try:
                    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "odds_row")))
                    break
                except:
                    winsound.Beep(frequency2, duration)
                    while True:
                        try:
                            browser.get(odds_url)
                            break
                        except:
                            winsound.Beep(frequency2, duration)
                            time.sleep(1)
                            continue
                    continue

            over_under_url = browser.find_element(By.XPATH, '//a[@title="Over/Under"]').get_attribute('href').encode('utf-8')

            while True:
                try:
                    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "odds_row")))
                    w_home = browser.find_element(By.CLASS_NAME, 'odds_row').find_elements(By.TAG_NAME, 'td')[2].find_elements(By.TAG_NAME, 'span')[0].text
                    break
                except:
                    winsound.Beep(frequency2, duration)
                    time.sleep(1)
                    browser.get(odds_url)
                    continue

            while True:
                try:
                    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "odds_row")))
                    draw = browser.find_element(By.CLASS_NAME, 'odds_row').find_elements(By.TAG_NAME, 'td')[3].find_elements(By.TAG_NAME, 'span')[0].text
                    break
                except:
                    winsound.Beep(frequency2, duration)
                    time.sleep(1)
                    browser.get(odds_url)
                    continue

            while True:
                try:
                    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "odds_row")))
                    w_away = browser.find_element(By.CLASS_NAME, 'odds_row').find_elements(By.TAG_NAME, 'td')[4].find_elements(By.TAG_NAME, 'span')[0].text
                    break
                except:
                    winsound.Beep(frequency2, duration)
                    time.sleep(1)
                    browser.get(odds_url)
                    continue

            browser.find_element(By.XPATH, '//a[@title="Over/Under"]').click()

            while True:
                try:
                    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "odds_row")))
                    time.sleep(3)
                    j = 0
                    while True:
                        j += 1

                        if ((browser.find_element(By.XPATH, '//table[@id="bbResults"]')).find_elements(
                                By.CLASS_NAME, 'odds_row')[j].find_elements(By.TAG_NAME, 'td')[2].text == '2.5'):
                            coef_over_total_2_5 = \
                            (browser.find_element(By.XPATH, '//table[@id="bbResults"]')).find_elements(
                                By.CLASS_NAME, 'odds_row')[j].find_elements(By.TAG_NAME, 'td')[4].text.encode(
                                'utf-8')[0:4]
                            break
                    break
                except:
                    winsound.Beep(frequency2, duration)
                    time.sleep(1)
                    while True:
                        try:
                            browser.get(odds_url)
                            WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "odds_row")))
                            break
                        except:
                            winsound.Beep(frequency2, duration)
                            time.sleep(1)
                            continue
                    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "odds_row")))
                    browser.find_element(By.XPATH, '//a[@title="Over/Under"]').click()
                    time.sleep(1)
                    continue


# Write in file part #

            writer.writerow({'season': season,
                             'league': league,
                             'date': date,
                             'home_team': home_team,
                             'away_team': away_team,
                             'home_attacks': home_attacks,
                             'away_attacks': away_attacks,
                             'home_danger_attacks': home_danger_attacks,
                             'away_danger_attacks': away_danger_attacks,
                             'coef_over_total_2_5': coef_over_total_2_5,
                             'w_home': w_home,
                             'draw': draw,
                             'w_away': w_away})

            count += 1

            print count

            print [season + " " + league + " " + date + " " + home_team + " " + away_team + " " + home_attacks + " " +
                   away_attacks + " " + home_danger_attacks + " " + away_danger_attacks + " " + coef_over_total_2_5 +
                   " " + w_home + " " + draw + " " + w_away]

            print " "

    browser.close()
    browser.quit()
    input_file.close()
    output_file.close()
