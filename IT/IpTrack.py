
import os
import json
from urllib import *
from platform import system
from datetime import datetime
import time
import socket
import json
import requests
import time
from requests import get



def ipinfo():
    print('== IP tacker - sadZIX ==')
    print()
    ip = input('Ingresa la IP: ')
    api = "http://ip-api.com/json/" + ip
    data = requests.get(api).json()
    print('Ip: ', data['query'])
    print('Estado: ', data['status'])
    print('Pais: ', data['country'])
    print('Region: ', data['regionName'])
    print('Codigo del pais: ', data['countryCode'])
    print('isp: ', data['isp'])
    print('org: ', data['org'])
    print('as: ', data['as'])
    print('Latitud: ', data['lat'])
    print('Longitud: ', data['lon'])
    print('Escaneo Completado')
    time.sleep(1)
    exit()

def ipublic():
    ip = get('https://api.ipify.org').text
    print(f'Tu ip publica es  :  {ip}')

ipublic()


def menu():
      print(" ")
      print("Ip Track By. ZIX")
      print("V. [1.0.0]")
      print("Team | zBoys")
      print("")
      print("[ 1 ]  Escanea una IP")
      print("[ 2 ]  IP publica")
      print("[ 0 ] Salir")
      print("     ")
      option = input("[+] Información IP >>> ")
      if option == "1":
          ipinfo()
          exit()

      elif option == "2":
          ipublic()
          exit()

menu()