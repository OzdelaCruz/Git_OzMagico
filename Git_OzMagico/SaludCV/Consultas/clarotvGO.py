from google.cloud import bigquery
from datetime import datetime
from dateutil.relativedelta import relativedelta

class claroTV_Go:
    def claroTV_Go(self):
        client = bigquery.Client()
        today = datetime.today() 
        primer_dia_del_mes_anterior = today.replace(day=1) - relativedelta(months=1)
        ultimo_dia_del_mes_anterior = primer_dia_del_mes_anterior + relativedelta(day=31)
        fechaConsulta = ultimo_dia_del_mes_anterior.strftime('%Y-%m-%d 00:00:00')
        print(f'FECHA DEL REPORTE:\n{fechaConsulta}')  #Formato de fecha
        
        # Resultados de Activos
        query = f"""
        SELECT
            COALESCE(SUM(COALESCE(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.CANTIDAD_DE_CLIENTES,0) ), 0) AS bi_ta_dw_susc_activas_diarias_total_clientes_1
        FROM `amco-cv-qa.PAG.DW_SUSC_ACTIVAS_DIARIAS_DETALLE` AS BI_TA_DW_SUSC_ACTIVAS_DIARIAS
        LEFT JOIN `amco-cv-des.BI.BI_CA_DIM_PRODUCTOS_CV`
            AS BI_CA_DIM_PRODUCTOS_CV ON BI_TA_DW_SUSC_ACTIVAS_DIARIAS.ID_ABONO = BI_CA_DIM_PRODUCTOS_CV.ID_ABONO
        LEFT JOIN `amco-cv-des.BQ.BQ_CA_DIM_PAIS`
            AS bq_ca_dim_pais ON BI_TA_DW_SUSC_ACTIVAS_DIARIAS.PAIS = bq_ca_dim_pais.PAIS_BI
        LEFT JOIN `amco-cv-des.BQ.BQ_CA_PAIS_HUB`
            AS bq_ca_pais_hub ON bq_ca_pais_hub.DESCRIPCION = BI_TA_DW_SUSC_ACTIVAS_DIARIAS.PAIS
        WHERE id_fecha=date(TIMESTAMP('{fechaConsulta}'))
        AND (case when BI_TA_DW_SUSC_ACTIVAS_DIARIAS.PAIS= 'PUERTORICO' THEN 1 ELSE 0 END  ) = 0 AND (case when BI_TA_DW_SUSC_ACTIVAS_DIARIAS.PAIS='MEXICO' and UPPER((upper(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.NOMBRE_COMPLETO)))='PAQUETE TV AVANZADO HD' then 1
                    when ((DATE(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.ID_FECHA ))between '2021-07-14' and '2021-07-30'  and UPPER((upper(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.NOMBRE_COMPLETO)))='HBO' and (case when BI_TA_DW_SUSC_ACTIVAS_DIARIAS.PAQUETE = 'PAQUETE_TV' and BI_TA_DW_SUSC_ACTIVAS_DIARIAS.TIPO_PRODUCTO in ('OTT','IPTV') then 'PAYTV'
                when BI_TA_DW_SUSC_ACTIVAS_DIARIAS.TIPO_PRODUCTO = 'IPTV' then 'PAYTV'
                else BI_TA_DW_SUSC_ACTIVAS_DIARIAS.TIPO_PRODUCTO end)='OTT') then 1
                    when ((DATE(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.ID_FECHA ))between '2021-08-01' and '2021-08-15'  and UPPER((upper(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.NOMBRE_COMPLETO)))='HBO' and (case when BI_TA_DW_SUSC_ACTIVAS_DIARIAS.PAQUETE = 'PAQUETE_TV' and BI_TA_DW_SUSC_ACTIVAS_DIARIAS.TIPO_PRODUCTO in ('OTT','IPTV') then 'PAYTV'
                when BI_TA_DW_SUSC_ACTIVAS_DIARIAS.TIPO_PRODUCTO = 'IPTV' then 'PAYTV'
                else BI_TA_DW_SUSC_ACTIVAS_DIARIAS.TIPO_PRODUCTO end)='OTT') then 1
                    when BI_TA_DW_SUSC_ACTIVAS_DIARIAS.ID_ABONO in (3741) then 1

            else 0 end  ) = 0 AND (case when BI_TA_DW_SUSC_ACTIVAS_DIARIAS.PAQUETE = 'PAQUETE_TV' and BI_TA_DW_SUSC_ACTIVAS_DIARIAS.TIPO_PRODUCTO in ('OTT','IPTV') then 'PAYTV'
                when BI_TA_DW_SUSC_ACTIVAS_DIARIAS.TIPO_PRODUCTO = 'IPTV' then 'PAYTV'
                else BI_TA_DW_SUSC_ACTIVAS_DIARIAS.TIPO_PRODUCTO end) = 'ClaroTV Go' AND (bq_ca_pais_hub.FECHA_BAJA ) IS NULL AND (bq_ca_dim_pais.PAIS ) IS NOT NULL
        LIMIT 1"""
     # Obtener los resultados
        query_job = client.query(query)

        results = query_job.result()
        row = next(results)
        # Acceder al valor del número en la primera fila
        suscripcionesClaroTV = row[0]
        # Mostrar el valor en el formato deseado
        print(f"Suscripciones ClaroTV Go: {suscripcionesClaroTV}")