from bs4 import BeautifulSoup as bs
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import time as t
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_argument('--headless')

print("success")


app = FastAPI()
app.add_middleware(CORSMiddleware, allow_methods=["*"],
                   allow_headers=["*"],)


@app.get("/")
async def root():
    return {"message": "ap is up and running"}


@app.get("/images/{image}")
async def read_word(image):
    driver = webdriver.Chrome(options=options)
    search_image = image
    print(search_image)
    driver.get("https://images.google.com/")
    searchbox = driver.find_element(By.TAG_NAME, "textarea")
    search_keys = driver.find_elements(By.TAG_NAME, "button")
    searchbox.send_keys(search_image)
    search_key = search_keys[1]
    search_key.click()
    t.sleep(1)
    page = bs(driver.page_source, "lxml")
    images = page.select("img")
    print(images)
    cleand_images = []
    for x in images:
        try:
            cleand_images.append(x["src"])
        except:
            pass
    driver.close()
    return {"message": cleand_images}
