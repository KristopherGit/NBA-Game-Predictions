
# NBA Predictions - https://www.basketball-reference.com Web Scraper Program

# Import libraries and dependencies

# Note: Make sure if running this .py file in VSCode that Command+Shift+P --> 'Python: Select Interpreter' 3.7.13('dev') is selected
# in order to have access to pre-installed modules from 'Fintech (conda activate dev)' installations
#

# i.) Import libraries for web scraping specifically
# Playwright and BeautifulSoup allows web browser to open, navigate to specific part of the page, use 'Instance'
# to access the html and grab information
import os
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
import time
import pandas as pd

# Setup constants
# range are seasons we want to scrap data from
SEASONS = list(range(2016, 2023))
print(SEASONS)

# Directory to store SEASONS data -> Creating pointers where to store the data that eventually gets scraped
DATA_DIR = "data2"
# Directory inside the DATA_DIR="data2" directory in order to store standings info (info we scrap that lists all
# box scores)
STANDINGS_DIR = os.path.join(DATA_DIR, "standings")

# Directory to then store all the box scores
SCORES_DIR = os.path.join(DATA_DIR, "scores")

# Use https://www.basketball-reference.com/
# Link to each NBA game for a particular season/month's individual box scores:
# i.e.) https://www.basketball-reference.com/ -> 'Season' -> 'All NBA and ABA Seasons' -> '2015-16'
# -> 'Schedule & Results' -> 'October' November' December' 'January', etc.
# Function script that if we give it a url & a selector it can grab html from a part of that page
# Playwright works async (executes in the background and doesn't print to main page)
# Get 'html' function
# Function is used to scrap, but pauses for sleep=5 (* i) seconds so the server doesn't ban us attempting to get data


def get_html(url, selector, sleep=5, retries=3):
    html = None
    for i in range(1, retries+1):
        time.sleep(sleep * i)

        # try launching playwright & chromium browser w/ await activated (waiting until browser is finished loading until scraping begins
        try:
            with sync_playwright() as p:
                # launches browser, 'awaits' until browser is finished loading
                browser = p.firefox.launch()
                # create new tab in browser
                page = browser.new_page()
                page.goto(url)
                # print the title of the url webpage so we know our progress in the 'try' method await playwright webscrap process
                print(page.title())
                # grab 'selector' a certain section or piece of the html
                html = page.inner_html(selector)
        except PlaywrightTimeout:
            # 'except' PlaywrightTimeout will throw us an error if there's a timeout error in attempting to scrap
            print(f"Timeout error on {url}")
            # if it fails, it will loop again and retry with a longer scrap timer (sleep * i, i=iteration number)
            continue
        else:
            break
    return html


# Start grabbing 'a' tags / 'href' links from www.basketball-reference.com/leagues/NBA_{season}_games.html
# Define season variable
#season = 2016

# Define base url variable
#url = f"https://www.basketball-reference.com/leagues/NBA_{season}_games.html"
# print(url)

# Get html variable
# html = get_html(url, "#content .filter")
# print(html)

# Instantiate BeautifulSoup
#soup = BeautifulSoup(html)
#links = soup.find_all("a")
#href = [l["href"] for l in links]
#standings_page = [f"https://wwww.basketball-reference.com{l}" for l in href]
# print(standings_page)

# Create a function based on the above variables called 'scrape_season' that works by passing in a season value i.e. season=2017
# Instantiate 'scrape_season' function


def scrape_season(season):
    url = f"https://www.basketball-reference.com/leagues/NBA_{season}_games.html"
    html = get_html(url, "#content .filter")

    soup = BeautifulSoup(html)
    links = soup.find_all("a")
    href = [l["href"] for l in links]
    standings_page = [
        f"https://basketball-reference.com{l}" for l in href]

    for url in standings_page:
        save_path = os.path.join(STANDINGS_DIR, url.split("/")[-1])
        if os.path.exists(save_path):
            continue

        html = get_html(url, '#all_schedule')
        with open(save_path, "w+") as f:
            f.write(html)


# Loop through individual 'season' in SEASON list (passed in from being defined above)
for season in SEASONS:
    scrape_season(season)

# Verify the scraping is completed by looking at the files in the standings dir
standings_files = os.listdir(STANDINGS_DIR)
print(standings_files)


# Create a function called 'scrape_game' to read and write all box_scores data from the body of the passed in standings_file(html)
# (This function will scan a single standings file (html) for a single month and save all the box_scores for that month)
def scrape_game(standings_file):
    with open(standings_file, 'r') as f:
        html = f.read()

    soup = BeautifulSoup(html)
    links = soup.find_all("a")
    hrefs = [l.get("href") for l in links]
    box_scores = [l for l in hrefs if l and "boxscore" in l and ".html" in l]
    box_scores = [
        f"https://www.basketball-reference.com{l}" for l in box_scores
    ]

    for url in box_scores:
        save_path = os.path.join(SCORES_DIR, url.split("/")[-1])
        if os.path.exists(save_path):
            continue

        html = get_html(url, "#content")
        if not html:
            continue
        with open(save_path, "w+") as f:
            f.write(html)


# Iterate through all 'standings_files' in the STANDINGS_DIR file folder by individual files (f)
# os.path.join concatenates pieces of file path into one direct filepath

standings_files = [s for s in standings_files if ".html" in s]
standings_files

for f in standings_files:
    filepath = os.path.join(STANDINGS_DIR, f)
    scrape_game(filepath)
