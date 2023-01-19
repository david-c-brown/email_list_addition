from selenium import webdriver
from selenium.webdriver.common.by import By
# as a note on pyautogui: it is not a fan of relative paths in my experience
# absolute paths will need to be added in for the code to run as written
import pyautogui as pg
import time

from config import *

driver = webdriver.Chrome()
actives = []
g = []
def add_to_list():
        try:
            # check for checkbox object with a tag that the source has an email associated
            checkbox = driver.find_element(By.XPATH, f"//input[@type='checkbox'][@class='n-mailer ref_check y-email']")
            checkbox.click()
            time.sleep(1)
            # navigate to drop down. Link text used because the button element shares an id and class with other items on the page
            bulk_dropdown = driver.find_element(By.LINK_TEXT, 'Select Bulk Action')
            bulk_dropdown.click()

            # the website being navigated is slow to say the least, and while selenium doesn't usually need explicit wait times, this is 100% necessary
            time.sleep(.5)

            # adding to the email list.
            # earlier versions of the script grabbed all sources then added to the list. 
            # This was substantially faster, but because of the way the system is set up it only pretends to select multiple searched for things.
            add_to_email = driver.find_element(By.ID, 'add_actives_to_email_list')
            add_to_email.click()

            time.sleep(1)
            #image of the desired list. This is the default when the list has previously been selected in that locations menu
            list_added = pg.locateCenterOnScreen('images/correct_list.png', confidence=.8)
            if list_added: #if list added not None just click the button
                finalize_list = pg.locateCenterOnScreen('images/add.png',confidence=.8)
                pg.click(finalize_list[0],finalize_list[1])
                # remove the name from the list, so we don't have multiple locations sending emails to one source
                actives.remove(g)
            else:
                # if the desired list is not already selected, navigate through the menu and select it    
                add_overlay = pg.locateCenterOnScreen('images/add_email.png',confidence=.8)
                pg.click(add_overlay[0]+50 ,add_overlay[1]+87 )
                time.sleep(2)
                # check if the list name has been created at this location. if it has select it and the source to the list
                try:
                    choose_campaign = pg.locateCenterOnScreen('images/email_pick.png',confidence=.8)
                    pg.click(choose_campaign[0],choose_campaign[1])
                    time.sleep(2)
                    finalize_list = pg.locateCenterOnScreen('images/add.png',confidence=.8)
                    pg.click(finalize_list[0],finalize_list[1])
                    actives.remove(g)
                # if the list has not been created, exit out of the menu
                except:
                    pg.press('esc')
                    # navigate to the dropdown again
                    bulk_dropdown = driver.find_element(By.LINK_TEXT, 'Select Bulk Action')
                    bulk_dropdown.click()

                    # make the list, with this source as the first addition
                    create_list = driver.find_element(By.ID, 'create_actives_email_list')
                    create_list.click()
                    
                    time.sleep(1)

                    create_list = pg.locateCenterOnScreen('images/create_email_list.png',confidence=.8)
                    pg.click(create_list[0], create_list[1])
                    pg.typewrite('2023 New Year Email List')
                    finalize_list = pg.locateCenterOnScreen('images/finalize.png', confidence=.8)
                    pg.click(finalize_list[0], finalize_list[1])
                    actives.remove(g)
        except:   
            try: 
                # there are 2 options for y-email. the code is otherwise identical to the above
                # a smarter man would just add this to the above definition if the first definition did not work out
                checkbox = driver.find_element(By.XPATH, f"//input[@type='checkbox'][@class='ref_check y-email y-mailer']")
                checkbox.click()
                bulk_dropdown = driver.find_element(By.LINK_TEXT, 'Select Bulk Action')
                bulk_dropdown.click()

                time.sleep(.5)

                add_to_email = driver.find_element(By.ID, 'add_actives_to_email_list')
                add_to_email.click()

                time.sleep(1)

                list_added = pg.locateCenterOnScreen('images/correct_list.png', confidence=.8)
                if list_added:
                    finalize_list = pg.locateCenterOnScreen('images/add.png',confidence=.8)
                    pg.click(finalize_list[0],finalize_list[1])
                else:    
                    add_overlay = pg.locateCenterOnScreen('images/add_email.png',confidence=.8)
                    pg.click(add_overlay[0]+50 ,add_overlay[1]+87 )
                    time.sleep(2)
                    choose_campaign = pg.locateCenterOnScreen('images/email_pick.png',confidence=.8)
                    pg.click(choose_campaign[0],choose_campaign[1])
                    time.sleep(2)
                    try:
                        finalize_list = pg.locateCenterOnScreen('images/add.png',confidence=.8)
                        pg.click(finalize_list[0],finalize_list[1])
                        actives.remove(g)
                    except:
                        pg.press('esc')

                        bulk_dropdown = driver.find_element(By.LINK_TEXT, 'Select Bulk Action')
                        bulk_dropdown.click()

                        create_list = driver.find_element(By.ID, 'create_actives_email_list')
                        create_list.click()
                        
                        time.sleep(1)

                        create_list = pg.locateCenterOnScreen('images/create_email_list.png',confidence=.8)
                        pg.click(create_list[0], create_list[1])
                        pg.typewrite('2023 New Year Email List')
                        finalize_list = pg.locateCenterOnScreen('images/finalize.png', confidence=.8)
                        pg.click(finalize_list[0], finalize_list[1])
                        actives.remove(g)
            except:
                pass     