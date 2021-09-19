# Defensive Playmaking

Created by: Michael Altschuler

Last Updated: 09/18/2021

## Table of Contents:
* [Purpose](#purose)
* [How to Run](#how-to-run)
* [Potential Issues](#potentia-issues)

## Purpose

The purpose of this application is to gather the following stats for a particular season from stats.nba.com:
* Player
* Team
* Age
* Height (in inches)
* Weight (in pounds)
* Games Played
* Minutes Played
* Steals
* Blocks
* Deflections

The final file will be located in final_data/{season} and will be called final.csv

## How to Run

'''
python scraper.py {season}
'''

For example:
'''
python scraper.py 2016-17
'''

## Potential Issues

This application uses chromedriver selenium to scrape the javascript table from stats.nba.com.  Make sure you have Chrome installed and make sure you have have the correct version of chromedriver that matches your version of chrome (https://chromedriver.chromium.org/downloads) and have it located in the same directory as scraper.py
