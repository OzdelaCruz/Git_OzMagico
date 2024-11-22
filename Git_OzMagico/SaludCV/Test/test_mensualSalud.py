import logging
import pandas as pd
import smtplib
from time import sleep
from datetime import datetime
from dateutil.relativedelta import relativedelta
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from deepdiff import DeepDiff
from selenium.webdriver.support.wait import WebDriverWait
from Configuration.configuration import Configuration
from Configuration.locatorLooker import locator
from Consultas.suscripcionesCV import bq
from Consultas.rs_suscripciones import rs_addon
from Consultas.rs_clarotvGO import rs_claroTV
from Consultas.clarotvGO import claroTV_Go
from Consultas.rs_clarotvPAYTV import rs_claro_payTv
from Consultas.clarotvPLAYTV import claro_payTv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from datetime import datetime, timedelta


class mensualSalud:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("Revisión Mensual Salud vs Claro Video")
        self.config = Configuration()
        self.locators = locator()
        self.consultaSuscritos = bq()
        self.rs_suscritosADDON = rs_addon()
        self.rs_TVGo = rs_claroTV()
        self.ClaroTVGo = claroTV_Go()
        self.rs_payTv = rs_claro_payTv()
        self.payTV = claro_payTv()
        self.login()

    def login(self):
        self.config.inicia_pagina()
        if self.config.driver is None:
            raise Exception(
                "Driver no inicializado, Asegura que inicia_pagina() esta correctamente instanciado"
            )

        self.logger.info("Se instancia la configuración del driver")
        try:
            WebDriverWait(self.config.driver, 5).until(
                EC.visibility_of_element_located((By.ID, self.locators.boton_acceder))
            )
        except TimeoutError as toe:
            print("Timeout Error en la carga de la página: ", toe)

        self.config.driver.find_element(By.ID, self.locators.textbox_user).send_keys(
            self.locators.Loocker_user
        )
        self.config.driver.find_element(
            By.ID, self.locators.id_textbox_password
        ).send_keys(self.locators.Loocker_password)
        self.config.driver.find_element(By.ID, self.locators.boton_acceder).click()
        self.config.driver.implicitly_wait(5)

        try:
            WebDriverWait(self.config.driver, 5).until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.locators.xpath_reportes_homologados)
                )
            )
        except TimeoutException as toe:
            print("TimeOut en la carga de la página: ", toe)

        # Navegacion al reporte
        self.config.driver.find_element(
            By.XPATH, self.locators.xpath_claro_video
        ).click()
        self.config.driver.implicitly_wait(5)
        self.config.driver.find_element(
            By.XPATH, self.locators.xpath_ClaroVideo
        ).click()
        sleep(3)
        try:
            WebDriverWait(self.config.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.locators.xpath_titulo_CV)
                )
            )
        except TimeoutException as toe:
            print("TimeOut en la carga de la página: ", toe)

        try:
            WebDriverWait(self.config.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.locators.xpath_suscritos)
                )
            )
        except TimeoutError as toe:
            print("No se visualizan los datos de la tabla: ", toe)
        self.config.driver.implicitly_wait(10)


    def test_1_columnaMesAnterior(self):
        today = datetime.now()
        primer_dia_del_mes = today.replace(day=1)
        ultimo_mes = primer_dia_del_mes - timedelta(days=1)
        mes = ultimo_mes.strftime("%Y %b")
        print(f"\nMes Anterior: {mes}")

        # Desplazar a la tabla de indicadores
        tabla = self.config.driver.find_element(
            By.XPATH, "(//div[normalize-space()='Indicadores'])[1]"
        )
        self.config.driver.execute_script("arguments[0].scrollIntoView();", tabla)
        self.config.driver.implicitly_wait(10)

        # Diccionario de conceptos y sus respectivos XPaths para columna Mes Anterior
        xpaths_mAnterior = {
            "CLIENTES SUSCRITOS(cv)": self.locators.xpath_mAnterior_suscritos,
            "CLIENTES PERIODO DE PRUEBA(cv)": self.locators.xpath_mAnterior_periodoPrueba,
            "CLIENTES ACTIVOS A 30 DIAS": self.locators.xpath_mAnterior_activos30,
            "ALTAS(cv)": self.locators.xpath_mAnterior_altas,
            "BAJAS(cv)": self.locators.xpath_mAnterior_bajas,
            "SUSCRIPCIONES ADDON OTT": self.locators.xpath_mAnterior_ADDON_OTT,
            "SUSCRIPCIONES ClaroTV Go": self.locators.xpath_mAnterior_ClaroTV,
            "SUSCRIPCIONES PAYTV": self.locators.xpath_mAnterior_PAYTV,
            "VISUALIZACIONES": self.locators.xpath_mAnterior_visualizaciones,
            "COMPRAS": self.locators.xpath_mAnterior_compras,
            "RENTAS": self.locators.xpath_mAnterior_rentas,
            "SERIES TEMPORADA": self.locators.xpath_mAnterior_series,
            "SUSCRIPCIONES No Informado": self.locators.xpath_mAnterior_noInformado,
        }

        # Extracción de valores de la columna Mes Anterior
        valores_mAnterior = []
        errores1 = []

        for concepto, xpath in xpaths_mAnterior.items():
            try:
                valorAnterior = (
                    WebDriverWait(self.config.driver, 5)
                    .until(EC.visibility_of_element_located((By.XPATH, xpath)))
                    .text
                )
                valores_mAnterior.append((concepto, valorAnterior))
            except Exception as e:
                errores1.append((concepto, xpath, str(e)))

        if valores_mAnterior:
            print("\nResultados del Mes Anterior:")
            for concepto, valorAnterior in valores_mAnterior:
                print(f"{concepto}: {valorAnterior}")
        else:
            print("No se obtuvieron valores para la columna Mes Anterior.")

        if errores1:
            print("\nErrores encontrados en Mes Anterior:")
            for concepto, xpath, error in errores1:
                print(f"Concepto: {concepto}, XPath: {xpath}, Error: {error}")

        # Cambio de fecha al mes anterior en el sistema
        today = datetime.today()
        mes = today + relativedelta(months=-2)
        mes_anterior = mes.strftime("%Y %b")
        print(f"\nMes de la Revisión: {mes_anterior}")

        self.config.driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div/div/section/div/div[1]/div/div[2]/section/div/div[1]/div/div[2]/div/span[2]/input",
        ).click()
        self.config.driver.implicitly_wait(5)

        elemento = self.config.driver.find_element(By.XPATH, "//div/div/div/ul/li[2]")
        action = ActionChains(self.config.driver)
        action.move_to_element(elemento).click().perform()
        self.config.driver.implicitly_wait(5)
        self.config.driver.find_element(
            By.CSS_SELECTOR, self.locators.css_actualizar_button
        ).click()
        sleep(5)

        # Diccionario de conceptos y XPaths para columna Mes Actual
        xpaths_mActual = {
            "CLIENTES SUSCRITOS(cv)": self.locators.xpath_mActual_suscritos,
            "CLIENTES PERIODO DE PRUEBA(cv)": self.locators.xpath_mActual_periodoPrueba,
            "CLIENTES ACTIVOS A 30 DIAS": self.locators.xpath_mActual_activos30,
            "ALTAS(cv)": self.locators.xpath_mActual_altas,
            "BAJAS(cv)": self.locators.xpath_mActual_bajas,
            "SUSCRIPCIONES ADDON OTT": self.locators.xpath_mActual_ADDON_OTT,
            "SUSCRIPCIONES ClaroTV Go": self.locators.xpath_mActual_ClaroTV,
            "SUSCRIPCIONES PAYTV": self.locators.xpath_mActual_PAYTV,
            "VISUALIZACIONES": self.locators.xpath_mActual_visualizaciones,
            "COMPRAS": self.locators.xpath_mActual_compras,
            "RENTAS": self.locators.xpath_mActual_rentas,
            "SERIES TEMPORADA": self.locators.xpath_mActual_series,
            "SUSCRIPCIONES No Informado": self.locators.xpath_mActual_noInformado,
        }

        # Extracción de valores de la columna Mes Actual
        valores_mActual = []
        errores2 = []

        for concepto, xpath in xpaths_mActual.items():
            try:
                valorActual = (
                    WebDriverWait(self.config.driver, 5)
                    .until(EC.visibility_of_element_located((By.XPATH, xpath)))
                    .text
                )
                valores_mActual.append((concepto, valorActual))
            except Exception as e:
                errores2.append((concepto, xpath, str(e)))

        if valores_mActual:
            print("\nResultados del Mes Actual:")
            for concepto, valorActual in valores_mActual:
                print(f"{concepto}: {valorActual}")
        else:
            print("No se obtuvieron valores para la columna Mes Actual.")

        if errores2:
            print("\nErrores encontrados en Mes Actual:")
            for concepto, xpath, error in errores2:
                print(f"Concepto: {concepto}, XPath: {xpath}, Error: {error}")

        # Comparación entre Mes Anterior y Mes Actual
        print("\nComparación de resultados:")
        for (concepto_anterior, valorAnterior), (concepto_actual, valorActual) in zip(
            valores_mAnterior, valores_mActual
        ):
            try:
                valorAnterior = int(valorAnterior.replace(",", ""))
                valorActual = int(valorActual.replace(",", ""))
                if valorAnterior == valorActual:
                    print(f"OK: {concepto_actual} - Sin cambios ({valorActual}).")
                else:
                    diferencia = valorActual - valorAnterior
                    print(
                        f"nOK: {concepto_actual} - Diferencia: {diferencia} "
                        f"(Mes Actual: {valorActual}, Mes Anterior: {valorAnterior})."
                    )
            except ValueError as e:
                print(f"Error procesando {concepto_actual}: {e}")


    def test_2_clientesSuscritos(self):
        # ubicar el filtro de fecha y volver a seleccionar el mes
        self.config.driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div/div/section/div/div[1]/div/div[2]/section/div/div[1]/div/div[2]/div/span[2]/input",
        ).click()
        self.config.driver.implicitly_wait(5)

        # seleccionar el mes
        elemento1 = self.config.driver.find_element(By.XPATH, "//div/div/div/div/ul/li")
        action = ActionChains(self.config.driver)
        action.move_to_element(elemento1).click().perform()
        self.config.driver.implicitly_wait(5)

        self.config.driver.find_element(
            By.CSS_SELECTOR, self.locators.css_actualizar_button
        ).click()
        sleep(5)


        # Aca se busca la tabla de indicadores
        tabla = self.config.driver.find_element(By.XPATH, "(//div[normalize-space()='Indicadores'])[1]")
        self.config.driver.execute_script("arguments[0].scrollIntoView();", tabla)

        self.config.driver.implicitly_wait(3)
        # Extracción de datos para Clientes Suscritos
        CV_clientesSuscritos = self.config.driver.find_element(By.XPATH, self.locators.xpath_mActual_suscritos).text
        print(f"Claro Video, Clientes Susctritos (Mes Actual): {CV_clientesSuscritos}")
        CV_clientesperiodoPrueba = self.config.driver.find_element(By.XPATH, self.locators.xpath_mActual_periodoPrueba).text
        print(f"Claro Video, Clientes Periodo de Prueba (Mes Actual): {CV_clientesperiodoPrueba}")

        # Se abre el Acceso al reporte de Salud
        self.config.driver.execute_script(f"window.open('{self.locators.Loocker_Salud}')")
        self.config.driver.switch_to.window(self.config.driver.window_handles[1])
        self.config.driver.implicitly_wait(10)

        
        try:
            WebDriverWait(self.config.driver, 20).until(
                EC.invisibility_of_element_located((By.ID, self.locators.cargo_reporte))
            )
        except Exception as e:
            print(f"No cargan los datos: {e}")


        tabla_BI = self.config.driver.find_element(By.XPATH, self.locators.tabla_Clarovideo_BI)
        self.config.driver.execute_script("arguments[0].scrollIntoView();", tabla_BI)
        # self.config.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5)

        suscritosBI = self.config.driver.find_element(By.XPATH, self.locators.salud_suscritosBI)
        print(f"Total Suscritos ReporteSalud: {suscritosBI.text}")
        periodoPruebaBI = self.config.driver.find_element(By.XPATH, self.locators.salud_periodo_pruebaBI)
        print(f"Total Periodo de Prueba ReporteSalud: {periodoPruebaBI.text}")

        try:
            assert (
                    suscritos_MA == suscritosBI
            ), f"Discrepacia de resultados, Suscritos de Claro Video: {suscritos_MA}\nReporte de Salud, tabla ClaroVideo (BI): {suscritosBI}"
            return True
        except Exception as e:
            return False

        finally:
            self.config.driver.switch_to.window(self.config.driver.window_handles[0])


    def test_3_altas(self):

        self.config.driver.execute_script(f"window.open('{self.locators.reporteSuscripciones}')")
        self.config.driver.switch_to.window(self.config.driver.window_handles[2])
        sleep(10)

        tablaAltas = self.config.driver.find_element(By.CSS_SELECTOR, self.locators.tabla_Altas)
        self.config.driver.execute_script("arguments[0].scrollIntoView();", tablaAltas)
        # self.config.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(3)

        total_Altas = self.config.driver.find_element(By.XPATH, self.locators.totalAltas)
        print(f"Total Altas en Reporte Suscritos: {total_Altas.text}")

        try:
            assert self.altas == total_Altas, f"Discrepacia entre Total Altas Claro Video: {self.altas}\nTotal Altas Reporte Suscripciones ClaroVideo/TV: {total_Altas}"
            return True
        except Exception as e:
            return False
            print(f"Error en: {e}")
        finally:
            print(f"Total Altas ClaroVideo :{self.altas.text}")
            self.config.driver.close
            self.config.driver.switch_to.window(self.config.driver.window_handles[0])


    def test_4_bajas(self):
        tablaBajas = self.config.driver.find_element(By.CSS_SELECTOR, self.locators.tabla_Bajas)
        self.config.driver.execute_script("arguments[0].scrollIntoView();", tablaBajas)
        # self.config.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(3)

        total_Bajas = self.config.driver.find_element(By.XPATH, self.locators.totalBajas)
        print(f"Total Bajas en Reporte Suscritos: {total_Bajas.text} ")
        print(f"Total Bajas Claro Video :{self.bajas.text}")
        try:
            assert self.bajas == total_Bajas, f"Discrepacia entre Total Bajas Claro Video: {self.bajas}\nTotal Bajas Reporte Suscripciones ClaroVideo/TV: {total_Bajas}"
            return True
        except Exception as e:
            return False
            print(f"Error en: {e}")
        finally:
            print(f"Total Bajas ClaroVideo :{self.bajas.text}")
            self.config.driver.close
            self.config.driver.switch_to.window(self.config.driver.window_handles[0])


    def test_5_addOn_OTT(self):
        self.config.driver.switch_to.window(self.config.driver.window_handles[0])
        sleep(2)
        addon = self.config.driver.find_element(By.XPATH, self.locators.xpath_mActual_ADDON_OTT).text
        print(f"Reporte Claro Video: {addon}")
        self.consultaSuscritos.consultaBQ()
        self.rs_suscritosADDON.rs_addonOTT()

        try:
            assert (addon == self.consultaSuscritos
                    ), f"Discrepancia entre Suscritos ADDON OTT: {addon}\nSuscritos en Reporte de Suscripciones CV: {self.consultaSuscritos}"
            assert (
                    addon == self.rs_suscritosADDON
                    ), f"Discrepancia entre Suscritos ADDON OTT: {addon}\Suscripciones activas OTT (BI): {self.rs_suscritosADDON}"
            return True
        except AssertionError as e:
            print(f"Error: {e}")
            return False
        finally:
            self.config.driver.switch_to.window(self.config.driver.window_handles[0])


    def test_6_claroTV_GO(self):
        self.config.driver.switch_to.window(self.config.driver.window_handles[0])
        sleep(2)
        rs_claroTV = self.config.driver.find_element(
            By.XPATH, self.locators.xpath_mActual_ClaroTV
        ).text
        print(f"Reporte Claro Video Suscripciones ClaroTV Go: {rs_claroTV}")
        self.rs_TVGo.rs_claroTV_Go()
        self.ClaroTVGo.claroTV_Go()

        try:
            assert (rs_claroTV == self.rs_TVGo
                    ), f"Discrepancia entre Suscripciones ClatoTV Go: {rs_claroTV}\nDetalle Suscripciones ClaroVideo/ClaroTV Go: {self.rs_TVGo}"
            assert (rs_claroTV == self.ClaroTVGo
                    ), f"Discrepancia entre Suscripciones ClatoTV Go: {rs_claroTV}\nSuscripciones activas ClaroTV Go (BI): {self.ClaroTVGo}"
            return True
        except AssertionError as e:
            print(f"Error: {e}")
            return False
        finally:
            self.config.driver.switch_to.window(self.config.driver.window_handles[0])


    def test_7_suscripcion_PAYTV(self):
        self.config.driver.switch_to.window(self.config.driver.window_handles[0])
        cv_PAYTV = self.config.driver.find_element(
            By.XPATH, self.locators.xpath_mActual_PAYTV
        ).text
        print(f"Reporte Claro Video campo Suscriociones PAYTV: {cv_PAYTV}")
        self.rs_payTv.rs_paytv()
        self.payTV.paytv()

        try:
            assert (cv_PAYTV == self.rs_payTv), f"Discrepancia entre Suscripciones ClatoTV Go: {cv_PAYTV}\nDetalle Suscripciones ClaroVideo/ClaroTV Go: {self.rs_payTv}"
            assert (cv_PAYTV == self.payTV), f"Discrepancia entre Suscripciones ClatoTV Go: {cv_PAYTV}\nSuscripciones activas ClaroTV Go (BI): {self.ClaroTVGo}"
            return True
        except AssertionError as e:
            print(f"Error: {e}")
            return False
        finally:
            self.config.driver.switch_to.window(self.config.driver.window_handles[0])
            #self.config.driver.quit


    def test_8_activos30_Vis(self):
        self.config.driver.switch_to.window(self.config.driver.window_handles[0])

        # REPORTE DE CLARO VIDEO
        clientes_activos30 = self.config.driver.find_element(By.XPATH, self.locators.xpath_mActual_activos30).text
        print(f"Claro Video Activos 30: {clientes_activos30}")
        visualizaciones = self.config.driver.find_element(By.XPATH, self.locators.xpath_mActual_visualizaciones).text
        print(f"Claro video Visualizaciones: {visualizaciones}")

        # Cambio al reporte de Salud
        self.config.driver.switch_to.window(self.config.driver.window_handles[1])
        rs_Usuarios_activos30 = self.config.driver.find_element(By.XPATH, self.locators.activos30)
        self.config.driver.execute_script("arguments[0].scrollIntoView();", rs_Usuarios_activos30)
        sleep(2)

        usr_activos30 = self.config.driver.find_element(By.XPATH, self.locators.totalBajas).text
        print(f"Total Bajas en Reporte Suscritos: {usr_activos30} ")

        rs_visualizaciones = self.config.driver.find_element(By.XPATH, self.locators.total_visualizaciones).text
        print(f"visualizaciones reporte de Salud : {rs_visualizaciones}")


    def test_9_comprasRentas(self):

        pass


    def test_10_seriesTemporada(self):

        pass


    def test_11_activos30(self):

        pass


    def test_12_indicadores(self):

        pass
