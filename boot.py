#importamos librerias
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



web = webdriver.Chrome() #añadimos a la variable web el explorador Chrome
web.get('http://instagram.com') #abrimos instagram
time.sleep(5) #esperamos 

#función de inicio de sesión
  
def login():
    user = "" #tu usuario
    paswd = "" #tu password
    aceptarCookies = web.find_element(By.XPATH, "//button[contains(text(),'Permitir cookies necesarias y opcionales')]") #buscamos botón de coockies
    aceptarCookies.click() #aceptamos las cookies
    time.sleep(5)
    inputUser = web.find_element("name", "username") #mediante el nombre seleccionamos el campo del usuario
    inputUser.send_keys(user) #lo introducimos
    inputPass = web.find_element("name", "password") #mediante el nombre seleccionamos el campo de la conntraseña
    inputPass.send_keys(paswd) #la introducimos
    time.sleep(5)
    loginButton = web.find_element(By.XPATH, "//button[@type='submit']").click() #buscamos el primer botón de tipo submit y lo clicamos
    time.sleep(5)
    print("Salgo del login")
 
#función abrir folowers
 
def open_followers(account_instagram): 
    web.get("https://www.instagram.com/" + account_instagram + "/followers/") #abrimos en instagram los seguidores de la página que hayamos indicado
    time.sleep(5) 
 
#función seguir cuentas

def follow_followers(seguidores):
    time.sleep(5)
    i = 1 
    j = 5
    #localizamos el primet boton "Seguir" mediante la variable "i" e iteraremos sobre esta ruta
    button = web.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[" + str(i) + "]/div[3]/button")
    while(button and i < seguidores): #mientras i sea menor a la cantidad de seguidores que queremos entramos en el bucle
        print("vuelta: " + str(i))
        if(i > j):#en caso de que j sea mayor que i haremos scroll en el pop up e incrementaremos la variable j
            print("5 segundos")
            time.sleep(5)
            j += 3
            pop_up_window = web.find_element(By.XPATH, "//div[@class='_aano']")  #localizamos el div que contiene los seguidores
            timeout = time.time() + 2 
            if time.time() < timeout: #scroll durante dos segundos
                web.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                pop_up_window)
        web.find_element(By.XPATH, "//html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[" + str(i) + "]/div[3]/button").click()
        i += 1
    else:
        print(str(seguidores) + " seguidos")

 

 
sources = [""] #Array donde almacenamos las paginas a las que queremos ir
login() #invocamos la función login
time.sleep(5) #esperamos 5 segundos
for account in sources: # dentro del array sources buscamos cada parametro y lo asociamos a la variable account
    open_followers(account) #pasamos la variable account a la función followers
    time.sleep(5) #esperamos
    follow_followers(30) #invocamos a la función follow y le pasamos la cantidad de seguidores que queremos
