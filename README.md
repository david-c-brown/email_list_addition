# email list distribution across multiple locations

## problem:
* internal crm is archaic, bulk download/upload isn't supported for this area
* in the same vein, locational databases do not talk to each other, even if they have identical sources
* the html / javascript is written without much thought to actual usage
* remote server access is owned by the contracted company, and they do not allow direct access to their database

## solution:
* navigate through the website using selenium
* once navigation with selenium hits its wall due to iframe obfuscation, use pyautogui to interact with the website
* build or update email lists with sources
* remove sources from list once they've been added to a locations mail blast

## additional notes:
* this took 117 minutes to run uninterrupted. average iteration time of 1.43/s
* by hand each source in the list would have take a 45/s, assuming no distractions and typical workpace.
* time spent reduced by 97%

## why jupyter?
* the final full solution required some creative steps for certain locations based on website idiosynchrasies
* simpler to locate and fix edge cases without dropping seleniums connection
