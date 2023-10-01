from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from mongo import MongoConnection

db_client = MongoConnection().client
db = db_client.get_databade('swatches')
col=db.get_collection('cameras')

driver = webdriver.Chrome()
driver.get("https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=camaras&_sacat=0")
cameras = driver.find_elements(By.CLASS_NAME, "s-item__wrapper")

for c in cameras:
    cam = c.find_element(by=By.CLASS_NAME, value="s-item__title").text
    price = c.find_element(by=By.CLASS_NAME, value="s-item__price").text
    envio = c.find_element(by=By.CLASS_NAME, value="s-item__logisticsCost").text

    document = {
        "cam": cam,
        "price: ": price,
        "envio": envio
    }

    col.insert_one(document=document)
    print("Articulo: ", cam)
    print("Valor total: ", price)
    print("Envio: ", envio)
        print('=' * 40)

driver.quit()
driver.close()