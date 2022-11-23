{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "9e9eb0ff-4cd5-4b8b-8dcf-62c628641ab0",
   "metadata": {},
   "source": [
    "## NBA Predictions - Predicting NBA Game Outcomes with ML / Neural Networks"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a923529c-d796-4715-a9fe-a8e4f9951853",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import libraries and dependencies\n",
    "\n",
    "# i.) Import libraries for web scraping specifically\n",
    "# Playwright and BeautifulSoup allows web browser to open, navigate to specific part of the page, use 'Instance'\n",
    "# to access the html and grab information\n",
    "import os \n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "#Note: Playwright runs asyncronously; executes separately in the background not in the main code section\n",
    "from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout\n",
    "import time\n",
    "\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c48f3f82-d101-4e1c-a974-243973c70aae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[2016, 2017, 2018, 2019, 2020, 2021, 2022]"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Setup constants\n",
    "# range are seasons we want to scrap data from\n",
    "SEASONS = list(range(2016, 2023))\n",
    "SEASONS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6942681a-0cb9-44ee-bab8-3b69d5466da7",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Directory to store SEASONS data -> Creating pointers where to store the data that eventually gets scraped\n",
    "DATA_DIR = \"data2\"\n",
    "# Directory inside the DATA_DIR=\"data2\" directory in order to store standings info (info we scrap that lists all\n",
    "# box scores)\n",
    "STANDINGS_DIR = os.path.join(DATA_DIR, \"standings\")\n",
    "\n",
    "# Directory to then store all the box scores\n",
    "SCORES_DIR = os.path.join(DATA_DIR, \"scores\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "48311b17-f608-4826-a896-7e34dbe5249a",
   "metadata": {},
   "source": [
    "#### i.) Web Scraping NBA Data with Playwright"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8e23b132-8ff8-467e-8777-449bae51fb90",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use https://www.basketball-reference.com/\n",
    "# Link to each NBA game for a particular season/month's individual box scores: \n",
    "# i.e.) https://www.basketball-reference.com/ -> 'Season' -> 'All NBA and ABA Seasons' -> '2015-16' \n",
    "# -> 'Schedule & Results' -> 'October' November' December' 'January', etc.\n",
    "\n",
    "# Function script that if we give it a url & a selector it can grab html from a part of that page\n",
    "# Playwright works async (executes in the background and doesn't print to main page)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "80d1d1ef-bfeb-464f-99b9-20b43e37de7a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Get 'html' function\n",
    "# Function is used to scrap, but pauses for sleep=5 (* i) seconds so the server doesn't ban us attempting to get data\n",
    "async def get_html(url, selector, sleep=5, retries=3):\n",
    "    html = None\n",
    "    for i in range(1, retries+1):\n",
    "        time.sleep(sleep * i)\n",
    "        \n",
    "        # try launching playwright & chromium browser w/ await activated (waiting until browser is finished loading until scraping begins\n",
    "        try:\n",
    "            async with async_playwright() as p:\n",
    "                #launches browser, 'awaits' until browser is finished loading\n",
    "                browser = await p.firefox.launch()\n",
    "                #create new tab in browser\n",
    "                page = await browser.new_page()\n",
    "                await page.goto(url)\n",
    "                #print the title of the url webpage so we know our progress in the 'try' method await playwright webscrap process\n",
    "                print(await page.title())\n",
    "                #grab 'selector' a certain section or piece of the html\n",
    "                html = await page.inner_html(selector)\n",
    "        except PlaywrightTimeout: \n",
    "            # 'except' PlaywrightTimeout will throw us an error if there's a timeout error in attempting to scrap\n",
    "            print(f\"Timeout error on {url}\")\n",
    "            # if it fails, it will loop again and retry with a longer scrap timer (sleep * i, i=iteration number)\n",
    "            continue\n",
    "        else:\n",
    "            break\n",
    "    return html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "e7de7e7f-48dc-4912-b545-e0d7ce2728f8",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Start grabbing 'a' tags / 'href' links from www.basketball-reference.com/leages/NBA_{season}_games.html\n",
    "# i.e.\n",
    "\n",
    "season = 2016\n",
    "\n",
    "url = f\"https://www.basketball-reference.com/leagues/NBA_{season}_games.html\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "9889f933-a749-4c1a-83ad-cb3b99a9a2cf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://www.basketball-reference.com/leagues/NBA_2016_games.html'"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "64906ace-a9d8-48c7-9369-22da7828528e",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndexError",
     "evalue": "list index out of range",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/hg/vnmbs9t948b9fyrh8m06w5h40000gn/T/ipykernel_86487/2055780016.py\u001b[0m in \u001b[0;36masync-def-wrapper\u001b[0;34m()\u001b[0m\n",
      "\u001b[0;32m/var/folders/hg/vnmbs9t948b9fyrh8m06w5h40000gn/T/ipykernel_86487/1618872960.py\u001b[0m in \u001b[0;36mget_html\u001b[0;34m(url, selector, sleep, retries)\u001b[0m\n\u001b[1;32m     10\u001b[0m             \u001b[0;32masync\u001b[0m \u001b[0;32mwith\u001b[0m \u001b[0masync_playwright\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mp\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     11\u001b[0m                 \u001b[0;31m#launches browser, 'awaits' until browser is finished loading\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 12\u001b[0;31m                 \u001b[0mbrowser\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mawait\u001b[0m \u001b[0mp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfirefox\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlaunch\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     13\u001b[0m                 \u001b[0;31m#create new tab in browser\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     14\u001b[0m                 \u001b[0mpage\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mawait\u001b[0m \u001b[0mbrowser\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mnew_page\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/envs/dev/lib/python3.7/site-packages/playwright/async_api/_generated.py\u001b[0m in \u001b[0;36mlaunch\u001b[0;34m(self, executable_path, channel, args, ignore_default_args, handle_sigint, handle_sigterm, handle_sighup, timeout, env, headless, devtools, proxy, downloads_path, slow_mo, traces_dir, chromium_sandbox, firefox_user_prefs)\u001b[0m\n\u001b[1;32m  12824\u001b[0m                 \u001b[0mtracesDir\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mtraces_dir\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m  12825\u001b[0m                 \u001b[0mchromiumSandbox\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mchromium_sandbox\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m> 12826\u001b[0;31m                 \u001b[0mfirefoxUserPrefs\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mmapping\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mto_impl\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfirefox_user_prefs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m  12827\u001b[0m             )\n\u001b[1;32m  12828\u001b[0m         )\n",
      "\u001b[0;32m~/opt/anaconda3/envs/dev/lib/python3.7/site-packages/playwright/_impl/_browser_type.py\u001b[0m in \u001b[0;36mlaunch\u001b[0;34m(self, executablePath, channel, args, ignoreDefaultArgs, handleSIGINT, handleSIGTERM, handleSIGHUP, timeout, env, headless, devtools, proxy, downloadsPath, slowMo, tracesDir, chromiumSandbox, firefoxUserPrefs)\u001b[0m\n\u001b[1;32m     91\u001b[0m         \u001b[0mnormalize_launch_params\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     92\u001b[0m         browser = cast(\n\u001b[0;32m---> 93\u001b[0;31m             \u001b[0mBrowser\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mfrom_channel\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;32mawait\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_channel\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"launch\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     94\u001b[0m         )\n\u001b[1;32m     95\u001b[0m         \u001b[0mbrowser\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_set_browser_type\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/envs/dev/lib/python3.7/site-packages/playwright/_impl/_connection.py\u001b[0m in \u001b[0;36msend\u001b[0;34m(self, method, params)\u001b[0m\n\u001b[1;32m     43\u001b[0m     \u001b[0;32masync\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0msend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmethod\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mstr\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mDict\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m->\u001b[0m \u001b[0mAny\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m         return await self._connection.wrap_api_call(\n\u001b[0;32m---> 45\u001b[0;31m             \u001b[0;32mlambda\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0minner_send\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mFalse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     46\u001b[0m         )\n\u001b[1;32m     47\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/envs/dev/lib/python3.7/site-packages/playwright/_impl/_connection.py\u001b[0m in \u001b[0;36mwrap_api_call\u001b[0;34m(self, cb, is_internal)\u001b[0m\n\u001b[1;32m    412\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0;32mawait\u001b[0m \u001b[0mcb\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    413\u001b[0m         \u001b[0mtask\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0masyncio\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcurrent_task\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_loop\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 414\u001b[0;31m         \u001b[0mst\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mList\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0minspect\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mFrameInfo\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mgetattr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtask\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"__pw_stack__\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0minspect\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstack\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    415\u001b[0m         \u001b[0mmetadata\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_extract_metadata_from_stack\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mst\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mis_internal\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    416\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mmetadata\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/envs/dev/lib/python3.7/inspect.py\u001b[0m in \u001b[0;36mstack\u001b[0;34m(context)\u001b[0m\n\u001b[1;32m   1511\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mstack\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcontext\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1512\u001b[0m     \u001b[0;34m\"\"\"Return a list of records for the stack above the caller's frame.\"\"\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1513\u001b[0;31m     \u001b[0;32mreturn\u001b[0m \u001b[0mgetouterframes\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msys\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_getframe\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcontext\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1514\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1515\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mtrace\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcontext\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/envs/dev/lib/python3.7/inspect.py\u001b[0m in \u001b[0;36mgetouterframes\u001b[0;34m(frame, context)\u001b[0m\n\u001b[1;32m   1488\u001b[0m     \u001b[0mframelist\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1489\u001b[0m     \u001b[0;32mwhile\u001b[0m \u001b[0mframe\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1490\u001b[0;31m         \u001b[0mframeinfo\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0mframe\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0mgetframeinfo\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mframe\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcontext\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1491\u001b[0m         \u001b[0mframelist\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mFrameInfo\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0mframeinfo\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1492\u001b[0m         \u001b[0mframe\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mframe\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mf_back\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/envs/dev/lib/python3.7/inspect.py\u001b[0m in \u001b[0;36mgetframeinfo\u001b[0;34m(frame, context)\u001b[0m\n\u001b[1;32m   1462\u001b[0m         \u001b[0mstart\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mlineno\u001b[0m \u001b[0;34m-\u001b[0m \u001b[0;36m1\u001b[0m \u001b[0;34m-\u001b[0m \u001b[0mcontext\u001b[0m\u001b[0;34m//\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1463\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1464\u001b[0;31m             \u001b[0mlines\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mlnum\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mfindsource\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mframe\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1465\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mOSError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1466\u001b[0m             \u001b[0mlines\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mindex\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/envs/dev/lib/python3.7/inspect.py\u001b[0m in \u001b[0;36mfindsource\u001b[0;34m(object)\u001b[0m\n\u001b[1;32m    826\u001b[0m         \u001b[0mpat\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mre\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcompile\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mr'^(\\s*def\\s)|(\\s*async\\s+def\\s)|(.*(?<!\\w)lambda(:|\\s))|^(\\s*@)'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    827\u001b[0m         \u001b[0;32mwhile\u001b[0m \u001b[0mlnum\u001b[0m \u001b[0;34m>\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 828\u001b[0;31m             \u001b[0;32mif\u001b[0m \u001b[0mpat\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmatch\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlines\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mlnum\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;32mbreak\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    829\u001b[0m             \u001b[0mlnum\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mlnum\u001b[0m \u001b[0;34m-\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    830\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0mlines\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mlnum\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mIndexError\u001b[0m: list index out of range"
     ]
    }
   ],
   "source": [
    "html = await get_html(url, \"#content .filter\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "83d97d2d-351c-45da-a408-68de85eb2643",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "dev",
   "language": "python",
   "name": "dev"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
