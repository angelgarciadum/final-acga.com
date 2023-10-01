
# TRATAMIENTO DE DATOS
## Proyecto Final
## ÍNDICE

Link del proyecto: [https://github.com/angelgarciadum/final-acga.com.git](https://github.com/angelgarciadum/final-acga.com.git)

1.  Objetivo del Proyecto
2.  Requisitos
3.  Instalación
4.  Autor
5.  Licencia

## Objetivos del Proyecto
El objetivo de la prueba final es obtener una visión general del tratamiento de datos desde  su obtención hasta su almacenado  
**Parte 1:** extraer datos de una fuente de datos online.  En nuestro caso usamos la página tiendamia.com.
 **Parte 2:** Almacenar esta información de forma estructurada en una base de datos en la nube. En nuestro caso usamos como almacenamiento de datos MongoDB.
**Parte 3:**  Crear un servicio web (usando Python + Flask o Django) que acceda a esa base de datos. Usamos Flask

## 2. REQUISITOS

**PyCharm** : Navegador Web. Usamos Google Chrome pero puede ser a criterio de cada persona.
**Selenium: 
MongoDB
Flask.**

## 3. INSTALACIÓN

Primero creamos el archivo requiriments.txt para poder instalar las extensiones y complementos que necesitamos:
```
selenium  
pymongo  
python-dotenv  
flask
```
Se exporta las librerías en nuestro archivo main.py
```
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.by import By  
from mongo import MongoConnection
```
Después configuramos la conexión y extraemos la información de la página que escogimos.
```
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
```

## 4. Autor
angelgarciadum

## 5. Licencia
Se trabajó con Código Abierto.
