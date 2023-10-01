from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from mongo import MongoConnection

db_client = MongoConnection().client
db = db_client.get_database('ebay')
col = db.get_collection('cameras')

driver = webdriver.Chrome()
driver.get("https://tiendamia.com/ec/search?amzs=drones")
drones = driver.find_elements(By.CLASS_NAME, "search-content")
print(drones)
mongodb = MongoConnection()

for c in drones:
    drones = c.find_element(by=By.CLASS_NAME, value="item-brand").text
    name = c.find_element(by=By.CLASS_NAME, value="item-name").text
    price = c.find_element(by=By.CLASS_NAME, value="item-price").text

    document = {
        "drones": drones,
        "name: ": name,
        "price": price
    }

    col.insert_one(document=document)
    print("Drones: ", drones)
    print("Nombre: ", name)
    print("Precio: ", price)
    print('=' * 40)

driver.quit()
