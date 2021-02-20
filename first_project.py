from selenium import webdriver
import time
browser = webdriver.Chrome("/Users/Desktop/chromedriver")

browser.get("https://www.forbes.com/powerful-brands/list/#tab:rank")
#print(browser.page_source)
#print(browser.title)

browser.fullscreen_window()
time.sleep(2)

browser.get("https://www.forbes.com/companies/apple/?list=powerful-brands#17d8e6c15355")
time.sleep(3)

browser.set_window_size(600,400)
time.sleep(3)
browser.save_screenshot("/Users/Desktop/image.png")
time.sleep(2)

browser.back()
time.sleep(3)
browser.quit()
