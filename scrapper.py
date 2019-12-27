from time import sleep
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os
import requests
import shutil
from dotenv import load_dotenv
from pathlib import Path

PATH='./geckodriver'
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
USERNAME = os.getenv('email')
PASS = os.getenv('password')
driver = webdriver.Firefox(executable_path=PATH)
driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
login = driver.find_element_by_id('username')
password = driver.find_element_by_id('password')
login.send_keys(USERNAME)
password.send_keys(PASS)
button = driver.find_element_by_xpath("/html/body/div/main/div/form/div[3]/button")
button.send_keys(Keys.ENTER)
sleep(5)
driver.get("https://www.linkedin.com/groups/3762811/")

lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    sleep(3)
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount==lenOfPage:
        match=True

post_descriptions = driver.find_elements_by_css_selector("div[class='feed-shared-text__text-view feed-shared-text-view white-space-pre-wrap break-words ember-view']")
# src = open("grp.html", "w")
# src.write(driver.page_source)
# src.close()
# print(post_descriptions)
# print(post_descriptions[0].text)
comment_buttons = driver.find_elements_by_css_selector("li[class='social-details-social-counts__item social-details-social-counts__comments']")

for line in comment_buttons:
    button = line.find_element_by_tag_name('button')
    button.click()

try:
    load_more_comments = driver.find_elements_by_css_selector("div[class='comments-comments-list__show-previous-container']")
    for line in load_more_comments:
        button = line.find_element_by_css_selector('button')
        button.click()
except:
    pass

try:
    show_previous_replies = driver.find_element_by_css_selector("button[class='button show-prev-replies t-12 t-black t-normal hoverable-link-text']")
    for button in show_previous_replies:
        button.click()
except:
    pass

comments_data = driver.find_elements_by_css_selector("p[class='comments-comment-item__main-content feed-shared-main-content--comment t-12 t-black t-normal feed-shared-main-content ember-view']")

for post in post_descriptions[:5]:
    print(post.text)

for comment in comments_data[:5]:
    print(comment.text)