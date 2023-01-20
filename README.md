# Marketplace-Scraper (2021)


## Project Lore:
Got a laptop stolen while travelling through France. Hoping it would turn up on facebook marketplace I wrote a scraper that worked on a specific facebook version.
My goal was to ask the thief for certain files back (very far fetched).

Laptop never turned up, Facebook front end was updated making this version of the scraper obsolete.

## To Note:
The code is deprecated and no longer works due to changes in facebook frontend and possibly due to changes to the webdriver in use as well (2023 January).


## Functioning:

The program is based around chrome driver using selenium. After opening chromium the algorithm would select the correct parameters (location, range, and topic), it would then load in elements by scrolling, while scanning the names and short descriptions of the items. After a certain time of searching, the selected items are loaded into an output html page that is then opened displaying the name and image of the given item, as well as providing a link to get back to the said item onto marketplace.

