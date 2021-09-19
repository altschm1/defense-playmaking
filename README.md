# Defensive Playmaking

Created by: Michael Altschuler

Last Updated: 09/18/2021

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

```
python scraper.py {season}
```

For example:
```
python scraper.py 2016-17
```

## Potential Issues

This application uses chromedriver selenium to scrape the javascript table from stats.nba.com.  Make sure you have Chrome installed and make sure you have have the correct version of chromedriver that matches your version of chrome (https://chromedriver.chromium.org/downloads) and have it located in the same directory as scraper.py

It is possible that due to taking too long to load the webpage, not all of the rows will be read.  This application built in a protection to re-run it it didn't collect at least 50 rows. If you do not intend for this behavior, comment out that infinite loop at the bottom of scraper.py or hit CTL + C  after final.csv is saved the first time.
