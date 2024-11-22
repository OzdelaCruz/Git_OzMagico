from google.cloud import bigquery
from datetime import datetime
from dateutil.relativedelta import relativedelta

class rs_addon:
    def rs_addonOTT(self):
        client = bigquery.Client()
        today = datetime.today() 
        primer_dia_del_mes_anterior = today.replace(day=1) - relativedelta(months=1)
        ultimo_dia_del_mes_anterior = primer_dia_del_mes_anterior + relativedelta(day=31)
        fechaConsulta = ultimo_dia_del_mes_anterior.strftime('%Y-%m-%d 00:00:00') #Formato de fecha
        print(f'FECHA DEL REPORTE:\n{fechaConsulta}')
        # Resultados de Activos
        query = f"""
        with gral as (
SELECT
    case when (upper(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.NOMBRE_COMPLETO)) = 'FOX+' then 1
              when (upper(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.NOMBRE_COMPLETO)) = 'FOX PREMIUM' then 2
              when (upper(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.NOMBRE_COMPLETO)) = 'FOX SPORTS' then 3
              when (upper(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.NOMBRE_COMPLETO)) = 'HBO' then 4
              when (upper(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.NOMBRE_COMPLETO)) = 'NOGGIN' then 5
              when (upper(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.NOMBRE_COMPLETO)) = 'PICARDIA NACIONAL' then 6
              when (upper(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.NOMBRE_COMPLETO)) = 'EDYE' then 7
              when (upper(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.NOMBRE_COMPLETO)) = 'PARAMOUNT' then 8
              when (upper(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.NOMBRE_COMPLETO)) = 'QELLO' then 9
              when (upper(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.NOMBRE_COMPLETO)) = 'KARAOKE' then 10
              when (upper(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.NOMBRE_COMPLETO)) = 'INDYCAR' then 11
              when (upper(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.NOMBRE_COMPLETO)) = 'WIN SPORTS+' then 12
              when (upper(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.NOMBRE_COMPLETO)) = 'ATRES' then 13
              when (upper(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.NOMBRE_COMPLETO)) = 'RTVEPLAY' then 14
              when (upper(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.NOMBRE_COMPLETO)) = 'STARZPLAY' then 15 else 20 end   AS bi_ta_dw_susc_activas_diarias_orden_nombre_completo_1,
    upper(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.NOMBRE_COMPLETO)  AS bi_ta_dw_susc_activas_diarias_nombre_completo_1,
    COALESCE(SUM(COALESCE(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.CANTIDAD_DE_CLIENTES,0) ), 0) AS bi_ta_dw_susc_activas_diarias_total_cantidad_de_clientes_1
FROM `amco-cv-qa.PAG.DW_SUSC_ACTIVAS_DIARIAS_DETALLE` AS BI_TA_DW_SUSC_ACTIVAS_DIARIAS
LEFT JOIN `amco-cv-des.BQ.BQ_CA_DIM_PAIS`
     AS bq_ca_dim_pais ON BI_TA_DW_SUSC_ACTIVAS_DIARIAS.PAIS = bq_ca_dim_pais.PAIS_BI
WHERE id_fecha=date(TIMESTAMP('{format}'))
AND (case when BI_TA_DW_SUSC_ACTIVAS_DIARIAS.PAIS= 'PUERTORICO' THEN 1 ELSE 0 END  ) = 0 AND ((case when BI_TA_DW_SUSC_ACTIVAS_DIARIAS.PAIS='MEXICO' and UPPER((upper(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.NOMBRE_COMPLETO)))='PAQUETE TV AVANZADO HD' then 1
              when ((DATE(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.ID_FECHA ))between '2021-07-14' and '2021-07-30'  and UPPER((upper(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.NOMBRE_COMPLETO)))='HBO' and (case when BI_TA_DW_SUSC_ACTIVAS_DIARIAS.PAQUETE = 'PAQUETE_TV' and BI_TA_DW_SUSC_ACTIVAS_DIARIAS.TIPO_PRODUCTO in ('OTT','IPTV') then 'PAYTV'
        when BI_TA_DW_SUSC_ACTIVAS_DIARIAS.TIPO_PRODUCTO = 'IPTV' then 'PAYTV'
        else BI_TA_DW_SUSC_ACTIVAS_DIARIAS.TIPO_PRODUCTO end)='OTT') then 1
              when ((DATE(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.ID_FECHA ))between '2021-08-01' and '2021-08-15'  and UPPER((upper(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.NOMBRE_COMPLETO)))='HBO' and (case when BI_TA_DW_SUSC_ACTIVAS_DIARIAS.PAQUETE = 'PAQUETE_TV' and BI_TA_DW_SUSC_ACTIVAS_DIARIAS.TIPO_PRODUCTO in ('OTT','IPTV') then 'PAYTV'
        when BI_TA_DW_SUSC_ACTIVAS_DIARIAS.TIPO_PRODUCTO = 'IPTV' then 'PAYTV'
        else BI_TA_DW_SUSC_ACTIVAS_DIARIAS.TIPO_PRODUCTO end)='OTT') then 1
              when BI_TA_DW_SUSC_ACTIVAS_DIARIAS.ID_ABONO in (3741) then 1

      else 0 end  ) = 0 AND ((upper(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.NOMBRE_COMPLETO) ) <> 'Claro Video' AND (upper(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.NOMBRE_COMPLETO) ) <> 'HBOVMVPD ' AND (upper(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.NOMBRE_COMPLETO) ) <> 'CLARO VIDEO' OR (upper(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.NOMBRE_COMPLETO) ) IS NULL)) AND ((BI_TA_DW_SUSC_ACTIVAS_DIARIAS.PAQUETE ) = 'ADDON' AND ((case when BI_TA_DW_SUSC_ACTIVAS_DIARIAS.PAQUETE = 'PAQUETE_TV' and BI_TA_DW_SUSC_ACTIVAS_DIARIAS.TIPO_PRODUCTO in ('OTT','IPTV') then 'PAYTV'
        when BI_TA_DW_SUSC_ACTIVAS_DIARIAS.TIPO_PRODUCTO = 'IPTV' then 'PAYTV'
        else BI_TA_DW_SUSC_ACTIVAS_DIARIAS.TIPO_PRODUCTO end) = 'OTT' AND (bq_ca_dim_pais.PAIS ) IS NOT NULL))
GROUP BY
1,2
ORDER BY
    3 DESC limit 5000)
 select
 sum(bi_ta_dw_susc_activas_diarias_total_cantidad_de_clientes_1) as total_susc
      from gral
        """
     # Obtener los resultados
        query_job = client.query(query)

        results = query_job.result()
        row = next(results)
        # Acceder al valor del número en la primera fila
        rs_suscripciones = row[0]
        # Mostrar el valor en el formato deseado
        print(f"Suscripciones activas OTT (BI): {rs_suscripciones}")