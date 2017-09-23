#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("http://mahsumakbas.net/selenium/dragdrop.html")
drag_element= driver.find_element_by_id("draggable")
targ_element= driver.find_element_by_id("droppable")
print(targ_element.text)

ac=ActionChains(driver)
ac.drag_and_drop(drag_element,targ_element).perform()

print(targ_element.text)
