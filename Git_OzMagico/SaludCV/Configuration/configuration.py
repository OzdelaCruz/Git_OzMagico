from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import logging
import os
from Configuration.locatorLooker import locator
from webdriver_manager.chrome import ChromeDriverManager

class Configuration:
    def __init__(self):
        # Configuración del logger
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("Configuration")

        # Inicializa localizadores y URL
        self.locator = locator()
        self.url = "https://amco.cloud.looker.com/login"

        # Define la ruta de descarga
        self.download_path = self.locator.Download_path

        # Crear la carpeta si no existe
        if not os.path.exists(self.download_path):
            os.makedirs(self.download_path)

        # Configura las opciones de Chrome
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option('prefs', {
            'download.default_directory': self.download_path,  # Define la ruta de descarga
            'download.prompt_for_download': False,  # No preguntar por descarga
            'download.directory_upgrade': True,  # Permitir la actualización de directorios
            'safebrowsing.enabled': True,  # Permitir la descarga de archivos
            'profile.default_content_settings.popups': 0  # Deshabilitar popups
        })
        
        self.chrome_options.add_argument('--disable-gpu')  # Desactiva la aceleración GPU
        self.chrome_options.add_argument('--no-sandbox')  # Deshabilita el sandbox de Chrome
        self.chrome_options.add_argument('--disable-dev-shm-usage')  # Usa memoria temporal si /dev/shm es limitada
        self.chrome_options.add_argument('--disable-infobars')  # Oculta la barra de "automatización del navegador"
        self.chrome_options.add_argument('--headless')  # (Opcional) Ejecuta en modo headless, sin interfaz gráfica


    def inicia_pagina(self):
        # Inicialización del WebDriver
        service = Service(service = Service(ChromeDriverManager().install()))
        self.driver = webdriver.Chrome(service=service, options=self.chrome_options)

        # Configuración de WebDriverWait y ActionChains
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

        # Iniciar la página y maximizar la ventana
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.logger.info("WEBDRIVER INICIADO CORRECTAMENTE")
        self.logger.info(f"URL INICIADA CORRECTAMENTE: {self.url}")
