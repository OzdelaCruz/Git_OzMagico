class locator():
    Loocker_URL = "https://amco.cloud.looker.com/login"
    Loocker_Salud = 'https://amco.cloud.looker.com/dashboards/1456?Pais=&Fecha%20a%20consultar=2024%2F09%2F01%20to%202024%2F09%2F30&Medio%20De%20Pago=&Prueba='
    textbox_user = "login-email"
    id_textbox_password = "login-password"
    boton_acceder = "login-submit"
    Loocker_user = "datos_qa.cmx@clarovideotv.com"
    Loocker_password = "89Fu8B;48:0Y"
    xpath_dashboard_claro_video_link = "/html/body/div[2]/div/div/div/div/section/div/div[1]/div/a/span"
    xpath_production_link = "/html/body/div[2]/div/div/div/div/section/folders-subrouter/div/div/lk-folder/div/div[1]/div/div[1]/lk-breadcrumbs/div/ul/li[2]/a"
    xpath_reportes_homologados = "/html/body/div[2]/div/div/div/div/section/folders-subrouter/div/div/lk-folder/div/div[2]/div/div/lk-folder-children-section/div/div[2]/a[5]/div/div"
    xpath_claro_video = "/html/body/div[2]/div/div/div/div/section/folders-subrouter/div/div/lk-folder/div/div[2]/div/div/lk-folder-children-section/div/div[2]/a[3]/div/div"
    xpath_finanzas = "/html/body/div[2]/div/div/div/div/section/folders-subrouter/div/div/lk-folder/div/div[2]/div/div/lk-folder-children-section/div/div[2]/a[9]/div/div"
    xpath_archivos_CVMAX = "/html/body/div[2]/div/div/div/div/section/folders-subrouter/div/div/lk-folder/div/div[2]/div/div/lk-folder-children-section/div/div[2]/a[4]/div/div"
    xpath_archivos_operaciones_CVMAX = "/html/body/div[2]/div/div/div/div/section/folders-subrouter/div/div/lk-folder/div/div[2]/div/div/lk-browse-table[1]/table/tbody/tr/td[3]/div/a/div[1]"
    xpath_descarga_archivo = "/html/body/div[2]/div/div/div/div/section/div/div[2]/div[1]/div/div[2]/div/section/div/div[2]/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[4]/div/span/div/div/span/span/a/button"
    xpath_confirmación_de_reporte = "/html/body/div[2]/div/div/div/div/section/div/div[1]/div/div[1]/div[1]/h1"
    xpath_reportesDisponibles = "/html/body/div[2]/div/div/div/div/section/div/div[1]/div/div[1]/div[2]/div/div/button/div[1]"
    # Localizador de drive y descompresion
    Drivers_path = "C:\\Auto_amco\\drivers\\chromedriver.exe"
    Download_path = "C:\\Auto_amco\\reportes\\Semanal_CVMAX"

    # Asserts
    camino_prod = "/html/body/div[2]/div/div/div/div/section/folders-subrouter/div/div/lk-folder/div/div[1]/div/div[1]/lk-breadcrumbs/div/ul/li[2]/h2"

    # LOCALIZADORES UTILIADOS PARA LA AUTOMATIZACIÓN DEL REPORTE MENSUAL
    # -----------------------SALUD VS CLARO VIDEO-----------------------#

    xpath_ClaroVideo = "/html/body/div[2]/div/div/div/div/section/folders-subrouter/div/div/lk-folder/div/div[2]/div/div/lk-browse-table[1]/table/tbody/tr/td[3]/div/a/div[1]"
    xpath_titulo_CV = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/h1[1]"
    xpath_fechaCierre = "/html/body/div[2]/div/div/div/div/section/div/div[1]/div/div[2]/section/div/div[1]/div/div[2]/div/span[2]/input"
    indicadores = "/html/body/div[2]/div/div/div/div/section/div/div[2]/div[1]/div/div[4]"
    limpieza = "/html/body/div[2]/div/div/div/div/section/div/div[1]/div/div[2]/section/div/div[1]/div/div[2]/div/div/button/div[2]"
    # BotónActualiza
    css_actualizar_button = ".ButtonBase__ButtonOuter-sc-1bpio6j-0.hHesMM.ButtonBase-sc-1bpio6j-1.Button-sc-18euc9m-0.hVRVhU.jnQEzj"

    # TABLA DE RESULTADOS DEL REPORTE CLARO VIDEO
    xpath_fecha = "/html/body/div[2]/div/div/div/div/section/div/div[1]/div/div[2]/section/div/div[1]/div/div[2]/div/div/button/div[2]/svg/path[2]"
    xpath_visualizaciones = "//a[contains(text(),'VISUALIZACIONES')]"
    xpath_suscritos = "//a[contains(text(),'CLIENTES SUSCRITOS(cv)')]"
    xpath_suscripciones_PAYTV = "//body/div[@id='looker']/div[@id='lk-react-container']/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[8]/div[1]/div[1]/div[1]/span[1]/span[1]/a[1]"
    xpath_activos30 = "//a[contains(text(),'CLIENTES ACTIVOS A 30 DIAS')]"
    xpath_suscripciones_ClaroTV = "//body/div[@id='looker']/div[@id='lk-react-container']/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[7]/div[1]/div[1]/div[1]/span[1]/span[1]/a[1]"
    xpath_bajas = "//body/div[@id='looker']/div[@id='lk-react-container']/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/span[1]/span[1]/a[1]"
    xpath_altas = "//body/div[@id='looker']/div[@id='lk-react-container']/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/span[1]/span[1]/a[1]"
    xpath_ADDON_OTT = "//body/div[@id='looker']/div[@id='lk-react-container']/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[6]/div[1]/div[1]/div[1]/span[1]/span[1]/a[1]"
    xpath_periodoPrueba = "//a[contains(text(),'CLIENTES PERIODO DE PRUEBA(cv)')]"
    xpath_rentas = "//body/div[@id='looker']/div[@id='lk-react-container']/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[11]/div[1]/div[1]/div[1]/span[1]/span[1]/a[1]"
    xpath_noInformado = "//a[contains(text(),'SUSCRIPCIONES No Informado')]"
    xpath_clasificar = "/html/body/div[2]/div/div/div/div/section/div/div[2]/div[1]/div/div[4]/div/section/div/div[2]/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div[12]/div[1]/div/div/span/span[1]/a"
    xpath_compras = "//body/div[@id='looker']/div[@id='lk-react-container']/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[10]/div[1]/div[1]/div[1]/span[1]/span[1]/a[1]"
    xpath_series = "//body/div[@id='looker']/div[@id='lk-react-container']/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[12]/div[1]/div[1]/div[1]/span[1]/span[1]/a[1]"

    # RESULTADOS MES ACTUAL
    xpath_mActual_visualizaciones = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/span[1]"
    xpath_mActual_suscritos = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/span[1]"
    xpath_mActual_PAYTV = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[8]/div[2]/div[1]/div[1]/span[1]/span[1]"
    xpath_mActual_activos30 = "/html/body/div[2]/div/div/div/div/section/div/div[2]/div[1]/div/div[4]/div/section/div/div[2]/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div[3]/div[2]/div/div/span"
    xpath_mActual_ClaroTV = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[7]/div[2]/div[1]/div[1]/span[1]/span[1]"
    xpath_mActual_bajas = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[5]/div[2]/div[1]/div[1]/span[1]/span[1]"
    xpath_mActual_altas = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/span[1]"
    xpath_mActual_ADDON_OTT = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[6]/div[2]/div[1]/div[1]/span[1]/span[1]"
    xpath_mActual_periodoPrueba = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/span[1]"
    xpath_mActual_rentas = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[11]/div[2]/div[1]/div[1]/span[1]/span[1]"
    xpath_mActual_noInformado = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[13]/div[2]/div[1]/div[1]/span[1]/span[1]"
    xapth_mActual_clasificar = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[12]/div[1]/div[1]/div[1]/span[1]/span[1]/a[1]"
    xpath_mActual_compras = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[10]/div[2]/div[1]/div[1]/span[1]/span[1]"
    xpath_mActual_series = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[12]/div[2]"

    # RESULTADO MES ANTERIOR
    xpath_mAnterior_suscritos = "/html/body/div[2]/div/div/div/div/section/div/div[2]/div[1]/div/div[4]/div/section/div/div[2]/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[3]"
    xpath_mAnterior_periodoPrueba = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/span[1]/span[1]"
    xpath_mAnterior_activos30 = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[3]/div[3]/div[1]/div[1]/span[1]/span[1]"
    xpath_mAnterior_altas = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[4]/div[3]/div[1]/div[1]/span[1]/span[1]"
    xpath_mAnterior_bajas = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[5]/div[3]"
    xpath_mAnterior_ADDON_OTT = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[6]/div[3]/div[1]/div[1]/span[1]/span[1]"
    xpath_mAnterior_ClaroTV = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[7]/div[3]/div[1]/div[1]/span[1]/span[1]"
    xpath_mAnterior_PAYTV = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[8]/div[3]/div[1]/div[1]/span[1]/span[1]"
    xpath_mAnterior_visualizaciones = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[9]/div[3]/div[1]/div[1]/span[1]/span[1]"
    xpath_mAnterior_compras = "/html/body/div[2]/div/div/div/div/section/div/div[2]/div[1]/div/div[4]/div/section/div/div[2]/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div[10]/div[3]/div/div/span/span"
    xpath_mAnterior_rentas = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[11]/div[3]/div[1]/div[1]/span[1]/span[1]"
    xpath_mAnterior_series = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[12]/div[3]/div[1]/div[1]/span[1]/span[1]"
    xpath_mAnterior_noInformado = "/html/body/div[2]/div/div/div/div/section/div/div[2]/div[1]/div/div[4]/div/section/div/div[2]/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div[13]/div[3]"

    total_suscritos = "/html/body/div[2]/div/div/div/div/section/div/div[2]/div[1]/div/div[4]/div/section/div/div[2]/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[3]/div/div/span/span"

    # ESCENARIO 2
    # TABLERO CLAROvIDEO
    # TABLERO REPORTE SALUD
    tabla_Clarovideo_BI = "/html/body/div[2]/div/div/div/div/section/div/div[2]/div[1]/div/div[17]/div/section/div/div[2]"
    salud_suscritosBI = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[17]/div[1]/section[1]/div[1]/div[2]/div[1]/div[3]/*[name()='svg'][1]/*[name()='g'][7]/*[name()='g'][1]/*[name()='text'][1]"
    salud_periodo_pruebaBI = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[17]/div[1]/section[1]/div[1]/div[2]/div[1]/div[3]/*[name()='svg'][1]/*[name()='g'][7]/*[name()='g'][2]/*[name()='text'][1]"
    cargo_reporte = "/html/body/div[2]/div/div/div/div/section/div/div[1]/div/div[1]/div[2]/div/div/button/div[2]/svg"

    # ESCENARIO3 Y 4 TABLERO PARA ALTAS BAJAS SUSCRIPCIONES OTT ClaroVideosalud_suscritosBI
    
    reporteSuscripciones = "https://amco.cloud.looker.com/dashboards/821?Fecha=2023%2F11%2F01+to+2023%2F11%2F30&Pais=&Nombre+Producto=Claro+Video&Tipo+Producto=OTT"
    tabla_Altas = "section[aria-label='RESUMEN ALTAS']"
    tabla_Bajas = "section[aria-label='RESUMEN BAJAS']"
    tabla_Suscripciones = "section[aria-label='RESUMEN SUSCRIPCIONES']"
    totalAltas = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[5]/div[2]/div[1]/div[1]/div[12]/span[1]/span[1]/div[1]/span[1]"
    totalBajas = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[8]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[5]/div[2]/div[1]/div[1]/div[10]/span[1]/span[1]/div[1]/span[1]/span[1]"
    totalSuscipciones = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[11]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[6]/div[2]"

    # f_tipoProducto = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[2]"
    header = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[2]/section[1]"
    f_nombreProducto = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[4]/div[1]/span[1]"
    nameProducto = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[2]"
    listaProductos = "/html[1]/body[1]/div[3]"

    # reporte de salud
    activos30 = "/html/body/div[2]/div/div/div/div/section/div/div[2]/div[1]/div/div[57]/div/section/div/div[2]/div/div[2]/p"
    total_visualizaciones = "/html/body/div[2]/div/div/div/div/section/div/div[2]/div[1]/div/div[60]/div/section/div/div[2]/div/div[2]/p"