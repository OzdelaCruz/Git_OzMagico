import unittest
from Test.test_mensualSalud import mensualSalud


class TestSalud(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Método de configuración que se ejecuta una vez antes de todas las pruebas."""
        print("Iniciando pruebas de Salud (configuración inicial).")
        cls.tc_mensual = mensualSalud()  # Inicializa el objeto

    def login(self):
        """Se inicia el login\n\n."""
        print("=====> Login en Looker y navegación al reporte ClaroVideo <=====")
        self.tc_mensual.test_1_columnaMesAnterior()
        print("=====> Fin <=====")
    
    #@unittest.skip("Esta prueba está desactivada")
    def test_1_columnaMesAnterior(self):
        """Prueba de la columna del mes anterior\n\n."""
        print("=====> Inicia la revisión de columna Mes Anterior <=====")
        self.tc_mensual.test_1_columnaMesAnterior()
        print("=====> Fin de la revisión de columna Mes Anterior <=====")

    #@unittest.skip("Esta prueba está desactivada")
    def test_2_clientesSuscritos(self):
        """Prueba de clientes suscritos."""
        print("=====> Inicia la revisión de Clientes Suscritos <=====")
        self.tc_mensual.test_2_clientesSuscritos()
        print("=====> Fin de la revisión de Clientes Suscritos <=====")

    @unittest.skip("Esta prueba está desactivada")
    def test_3_altas(self):
        """Prueba de altas."""
        print("=====> Inicia la revisión de Altas <=====")
        self.tc_mensual.test_3_altas()
        print("=====> Fin de la revisión de Altas <=====")

    @unittest.skip("Esta prueba está desactivada")
    def test_4_bajas(self):
        """Prueba de bajas."""
        print("=====> Inicia la revisión de Bajas <=====")
        self.tc_mensual.test_4_bajas()
        print("=====> Fin de la revisión de Bajas <=====")

    @unittest.skip("Esta prueba está desactivada")
    def test_5_addOn_OTT(self):
        """Prueba de Add-On OTT."""
        print("=====> Inicia la revisión de Add-On OTT <=====")
        self.tc_mensual.test_5_addOn_OTT()
        print("=====> Fin de la revisión de Add-On OTT <=====")

    @unittest.skip("Esta prueba está desactivada")
    def test_6_claroTV_GO(self):
        """Prueba del Add-On OTT: Claro TV GO."""
        print("=====> Inicia la revisión de Claro TV GO <=====")
        self.tc_mensual.test_6_claroTV_GO()
        print("=====> Fin de la revisión de Claro TV GO <=====")

    @unittest.skip("Esta prueba está desactivada")
    def test_7_suscripcion_PAYTV(self):
        """Prueba de la suscripción PAYTV."""
        print("=====> Inicia la revisión de la suscripción PAYTV <=====")
        self.tc_mensual.test_7_suscripcion_PAYTV()
        print("=====> Fin de la revisión de la suscripción PAYTV <=====")

    @unittest.skip("Esta prueba está desactivada")
    def test_8_activos30_Vis(self):
        """Prueba de activos a 30 días (Visualizaciones)."""
        print("=====> Inicia la revisión de Activos a 30 días y Visualizaciones<=====")
        self.tc_mensual.test_8_activos30_Vis()
        print("=====> Fin de la revisión de Activos a 30 días y Visualizaciones<=====")

    @unittest.skip("Esta prueba está desactivada")
    def test_9_comprasRentas(self):
        """Prueba de Compras y Rentas."""
        print("=====> Inicia la revisión de Compras y Rentas <=====")
        self.tc_mensual.test_9_comprasRentas()
        print("=====> Fin de la revisión de Compras y Rentas <=====")

    @unittest.skip("Esta prueba está desactivada")
    def test_10_seriesTemporada(self):
        """Prueba de Series y Temporadas."""
        print("=====> Inicia la revisión de Series y Temporadas <=====")
        self.tc_mensual.test_10_seriesTemporada()
        print("=====> Fin de la revisión de Series y Temporadas <=====")

    @unittest.skip("Esta prueba está desactivada")
    def test_11_activos30(self):
        """Prueba de Activos a 30 días."""
        print("=====> Inicia la revisión de Activos a 30 días <=====")
        self.tc_mensual.test_11_activos30()
        print("=====> Fin de la revisión de Activos a 30 días <=====")

    @unittest.skip("Esta prueba está desactivada")
    def test_12_indicadores(self):
        """Prueba de Indicadores."""
        print("=====> Inicia la revisión de Indicadores <=====")
        self.tc_mensual.test_12_indicadores()
        print("=====> Fin de la revisión de Indicadores <=====")

    @classmethod
    def tearDownClass(cls):
        """Método de limpieza que se ejecuta una vez después de todas las pruebas."""
        print("Limpiando después de las pruebas...")

        # Aquí puedes realizar tareas de limpieza, como cerrar conexiones o liberar recursos.


if __name__ == '__main__':
    # Ejecutar las pruebas y mostrar resultados detallados
    unittest.main(verbosity=2)
