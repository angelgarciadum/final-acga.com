from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from mongo import MongoConnection

db_client = MongoConnection().client
db = db_client.get_database('tiendamia')
col = db.get_collection('drones')

driver = webdriver.Chrome()
driver.get("https://tiendamia.com/ec/search?amzs=drones")
Modelo = driver.find_elements(By.CLASS_NAME, "button-border")
print(Modelo)
mongodb = MongoConnection()

for c in Modelo:
    modelo = c.find_element(by=By.CLASS_NAME, value="item-brand").text
    name = c.find_element(by=By.CLASS_NAME, value="item-name").text
    price = c.find_element(by=By.CLASS_NAME, value="dollar_price").text

    document = {
        "Modelo": modelo,
        "Descripcion: ": name,
        "Precio": price
    }

    col.insert_one(document=document)
    print("Modelo: ", modelo)
    print("Descripcion: ", name)
    print("Precio: ", price)
    print('=' * 40)

driver.close()

