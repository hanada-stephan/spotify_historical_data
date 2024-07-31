# Spotify Historical Data

##### Tags: data, dashboard, ETL, json, python, powerbi

## Code and resources

Power BI version: 2.130.754.0
Python version: 3.10.5
Packages: dotenv, json, os, shutil, zipfile

## Dataset

Go to https://www.spotify.com/us/account/privacy/, sign into your account and search for "Download your data" and, then click in checkbox into "Extended streaming history". It may take up 30 days for all your data be ready to download.

When you get the json files, run the main.py script to unzip and clean the data. Lastly, upload the data into Power BI, copy and paste the code from "power-query.txt" file into Advanced Editor.

From Spotify's page:
"Check the 'Preparing Account Data' for the last 365 days worth of information
and check the 'Preparing Extended streaming history' to retrieve the lifetime
history of streaming."

# Dashboard


The dashboard is 4 pages long:
1) Overview: the main information about the historical streaming data such as, minutes played, distinct tracks and artists over time, most used platform and end track reason;
2) My top songs: information about the most streamed songs;
3) My top artists: information about the most streamed artists;
4) MY top albums: information about the most streamed albums.

All the pages have date, song, artist and album filters. To navigate among them, use the green and gray icons  in the top center parte of the dashboards. If an icon is green, it means you are in that page and the gray icons are the one that have been selected.
