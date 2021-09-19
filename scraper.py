## Michael Altschuler
## Last Updated: 2021-09-18

import sys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import os
import datetime

# helper function to take stats.nba.com table and make sure all rows are showns
def select_all(driver):
    select_options = driver.find_elements_by_xpath("//select")
    try:
        for s in select_options:
            select_test = Select(s)
            for option in select_test.options:
                if 'All' == option.text:
                    dropdown_menu = select_test
                    dropdown_menu.select_by_visible_text('All')
    except Excpetion as e:
        print("Error selecting all...")
        print(f"{err}")
        quit()

# convert height field to just inches
def get_height(x):
    return int(x.split('-')[0]) * 12 + int(x.split('-')[1])

# main function
def main(season):
    # make sure final_data/season directory exists
    try:
        os.mkdir(f'final_data/{season}')
        print(f"Generated dir final_data/{season}")
    except Exception as e:
        print(f"Dir final_data/{season} already exists")

    # get the url set for all the players for that season (stats.nba.com bio page)
    driver = webdriver.Chrome('./chromedriver')
    driver.get(f'https://www.nba.com/stats/players/bio/?Season={season}&SeasonType=Regular%20Season')
    select_all(driver)

    # get relevant fields from bio page
    df = pd.read_html(driver.page_source)[0]
    df.dropna(inplace=True)
    df = df[['Player', 'Team', 'Age', 'Height', 'Weight']]

    # get player games, total minutes, steals, blocks from the traditional page
    driver.get(f'https://www.nba.com/stats/players/traditional/?sort=PTS&dir=-1&Season={season}&SeasonType=Regular%20Season&PerMode=Totals')
    select_all(driver)
    df2 = pd.read_html(driver.page_source)[0]
    df2 = df2[['PLAYER', 'TEAM', 'GP', 'MIN', 'STL', 'BLK']]

    # merge bio and traditional dataframe
    final_df = pd.merge(df, df2, left_on=['Player', 'Team'], right_on=['PLAYER','TEAM'])
    final_df.drop(columns=['PLAYER', 'TEAM'], inplace=True)

    # get deflection stats and merge to final df
    driver.get(f'https://www.nba.com/stats/players/hustle/?Season={season}&SeasonType=Regular%20Season&PerMode=Totals')
    select_all(driver)
    df3 = pd.read_html(driver.page_source)[0]
    df3 = df3[['Player', 'TEAM', 'Deflections']]
    final_df = pd.merge(final_df, df3, left_on=['Player', 'Team'], right_on=['Player','TEAM'])
    final_df.drop(columns=['TEAM'], inplace=True)
    final_df['Height'] = final_df['Height'].apply(get_height)

    # save dataframe for that seasom
    print(final_df)
    print(final_df.shape)
    final_df.to_csv(f'final_data/{season}/final.csv', index=False)
    return final_df.shape



if __name__ == '__main__':
    # argv1 is season string (ie 2017-18)
    while True:
        shape = main(sys.argv[1])
        if shape[0] > 50:
            break
