from google.cloud import bigquery
from datetime import datetime
from dateutil.relativedelta import relativedelta

class bq:
    def consultaBQ(self):
        client = bigquery.Client()
        today = datetime.today() 
        primer_dia_del_mes_anterior = today.replace(day=1) - relativedelta(months=1)
        ultimo_dia_del_mes_anterior = primer_dia_del_mes_anterior + relativedelta(day=31)
        fechaConsulta = ultimo_dia_del_mes_anterior.strftime('%Y-%m-%d 00:00:00') #Formato de fecha
        print(f'FECHA DEL REPORTE:\n{fechaConsulta}')
        # Resultados de Activos
        query = f"""
                    SELECT
                        COALESCE(SUM(COALESCE(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.CANTIDAD_DE_CLIENTES,0) ), 0) AS bi_ta_dw_susc_activas_diarias_total_clientes_1
                    FROM amco-cv-qa.PAG.DW_SUSC_ACTIVAS_DIARIAS_DETALLE AS BI_TA_DW_SUSC_ACTIVAS_DIARIAS
                    LEFT JOIN `amco-cv-des.BI.BI_CA_DIM_PRODUCTOS_CV`
                        AS BI_CA_DIM_PRODUCTOS_CV ON BI_TA_DW_SUSC_ACTIVAS_DIARIAS.ID_ABONO = BI_CA_DIM_PRODUCTOS_CV.ID_ABONO
                    LEFT JOIN `amco-cv-des.BQ.BQ_CA_DIM_PAIS`
                        AS bq_ca_dim_pais ON BI_TA_DW_SUSC_ACTIVAS_DIARIAS.PAIS = bq_ca_dim_pais.PAIS_BI
                    LEFT JOIN `amco-cv-des.BQ.BQ_CA_PAIS_HUB`
                        AS bq_ca_pais_hub ON bq_ca_pais_hub.DESCRIPCION = BI_TA_DW_SUSC_ACTIVAS_DIARIAS.PAIS
                    WHERE id_fecha=date(TIMESTAMP('{format}'))
                    and (case when BI_TA_DW_SUSC_ACTIVAS_DIARIAS.PAIS= 'PUERTORICO' THEN 1 ELSE 0 END  ) = 0 AND ((case when BI_TA_DW_SUSC_ACTIVAS_DIARIAS.PAIS='MEXICO' and UPPER((upper(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.NOMBRE_COMPLETO)))='PAQUETE TV AVANZADO HD' then 1
                                when ((DATE(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.ID_FECHA ))between '2021-07-14' and '2021-07-30'  and UPPER((upper(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.NOMBRE_COMPLETO)))='HBO' and (case when BI_TA_DW_SUSC_ACTIVAS_DIARIAS.PAQUETE = 'PAQUETE_TV' and BI_TA_DW_SUSC_ACTIVAS_DIARIAS.TIPO_PRODUCTO in ('OTT','IPTV') then 'PAYTV'
                            when BI_TA_DW_SUSC_ACTIVAS_DIARIAS.TIPO_PRODUCTO = 'IPTV' then 'PAYTV'
                            else BI_TA_DW_SUSC_ACTIVAS_DIARIAS.TIPO_PRODUCTO end)='OTT') then 1
                                when ((DATE(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.ID_FECHA ))between '2021-08-01' and '2021-08-15'  and UPPER((upper(BI_TA_DW_SUSC_ACTIVAS_DIARIAS.NOMBRE_COMPLETO)))='HBO' and (case when BI_TA_DW_SUSC_ACTIVAS_DIARIAS.PAQUETE = 'PAQUETE_TV' and BI_TA_DW_SUSC_ACTIVAS_DIARIAS.TIPO_PRODUCTO in ('OTT','IPTV') then 'PAYTV'
                            when BI_TA_DW_SUSC_ACTIVAS_DIARIAS.TIPO_PRODUCTO = 'IPTV' then 'PAYTV'
                            else BI_TA_DW_SUSC_ACTIVAS_DIARIAS.TIPO_PRODUCTO end)='OTT') then 1
                                when BI_TA_DW_SUSC_ACTIVAS_DIARIAS.ID_ABONO in (3741) then 1

                        else 0 end  ) = 0 AND (case when BI_TA_DW_SUSC_ACTIVAS_DIARIAS.PAQUETE = 'PAQUETE_TV' and BI_TA_DW_SUSC_ACTIVAS_DIARIAS.TIPO_PRODUCTO in ('OTT','IPTV') then 'PAYTV'
                            when BI_TA_DW_SUSC_ACTIVAS_DIARIAS.TIPO_PRODUCTO = 'IPTV' then 'PAYTV'
                            else BI_TA_DW_SUSC_ACTIVAS_DIARIAS.TIPO_PRODUCTO end) = 'OTT') AND ((BI_CA_DIM_PRODUCTOS_CV.NOMBRE_PRODUCTO ) IN ('ABONO_SUPERIOR_HC_OTT', 'ATRES', 'CDF HD - PREMIUM ', 'CLAROTVPLUS', 'CLOUD DVR 100 HRS IPTV', 'COMBO ADULTOS ', 'CONMEBOL', 'Canales en Vivo', 'Claro TV Go Plus', 'ClaroNow Basico Plus', 'Claro_TV+', 'Degustación Claro TV', 'EDYE', 'EPG', 'El Canal del Futbol', 'FOX +', 'FOX Premier ClaroNow', 'FOX Premium', 'FOX SPORTS', 'GOLDEN PREMIER HD IPTV', 'GRANDES LIGAS IPTV', 'GRILLA', 'GUIA_UNICA_HD_FAKE', 'Golden', 'Golden Premier ClaroNow', 'Guia Unica HD', 'Guia Unica HD TS_24 NPVR_30', 'HBO', 'HBO ClaroNow', 'HBO IPTV', 'HBO_IPTV', 'HD PLUS', 'HOT PACK IPTV', 'HOT_PACK_IPTV', 'INDYCAR', 'INTERMEDIO', 'IPTV-Plan_Familiar', 'LIGAMAX', 'LIONSGATE', 'MAX', 'MGM', 'MVSHUB', 'NOGGIN', 'NPVR 100', 'NUEVA TV DIGITAL PLUS', 'Nacional Tv Bonificado Ilimitado', 'OTT CLOUD DVR', 'OTT Nacional Plus', 'PACK  TV PAQUETE CDF HD ', 'PACK FTTH TV DIGITAL AVANZADA TS', 'PACK FTTH TV SUPERIOR TS', 'PAQUETE ADULTO', 'PAQUETE CR EVERYWHERE DTH BASICO HD', 'PAQUETE EXTRA OTT', 'PAQUETE FOX', 'PAQUETE FOX SPORTS', 'PAQUETE HBO', 'PAQUETE MORBIDO ', 'PAQUETE TV PAQUETE CDF PREMIUM ', 'PAQUETE TV PAQUETE CLARO NOW ', 'PAQUETE TV PAQUETE CLARO NOW PLUS ', 'PAQUETE TV PAQUETE PLAYBOY ', 'PAQUETE TV PAQUETE VENUS ', 'PARAMOUNT', 'PENTHOUSE IPTV', 'PICARDIA NACIONAL', 'PLAYBOY HD IPTV', 'PLAY_TV', 'PLUS+ IPTV', 'PQT_AR_PREMIUM_FUTBOL_IPTV_HUBCORP', 'PQT_AR_PREMIUM_HOT_IPTV_HUBCORP', 'PQT_AR_UNIVERSAL_PLUS_IPTV_HUBCORP', 'PQT_BRASIL_CANALES_HBO', 'PQT_CL_TV_HD', 'PQT_CL_TV_MAX', 'PQT_EC_Paquete_EXTRA_IPTV_Everywhere', 'PQT_EC_Paquete_MAXIMO_IPTV_Everywhere', 'PQT_EC_Paquete_SUPER_IPTV_Everywhere', 'PQT_HN_Paquete_Avanzado_HD', 'PQT_MINI_GRILLA', 'PQT_NACIONAL', 'PQT_SUPERIOR_IPTV', 'PQT_TV_FUTBOL_TEST', 'PREMIERE', 'PREMIUM LIGA1MAX ', 'Pack MAXIMO', 'Pack Premium HBO', 'Pack-Adultos', 'Pack-DIGITAL-FOX-PREMIUM', 'Pack-FTTH-TV-DIGITAL-AVANZADA', 'Pack-FTTH-TV-SUPERIOR', 'Pack-Fox', 'Pack-Futbol', 'Pack-Golden', 'Pack-HBO-GO', 'Pack-Hbo', 'Pack-MINIPACK-FOX-PREMIUM', 'Pack-Turf', 'Pack-VENUS-DTH', 'Paquete Avanzado HD NS', 'Paquete Avanzado IPTV', 'Paquete Basico solidario', 'Paquete CLARONOW AVANZADO', 'Paquete CLARONOW BÁSICO PLUS ', 'Paquete CLARONOW GOLDEN PREMIER', 'Paquete CLARONOW HBO', 'Paquete CLARONOW SUPERIOR', 'Paquete COMBO ADULTOS ', 'Paquete ECDF IPTV', 'Paquete ESENCIAL TV', 'Paquete EXTRA IPTV', 'Paquete EXTRA TV', 'Paquete Extendido Futbol', 'Paquete FAKE TV EXTENDIDO', 'Paquete Golden', 'Paquete HBO IPTV', 'Paquete HOT PACK', 'Paquete HOT PACK IPTV', 'Paquete MAXIMO IPTV', 'Paquete OLE Futbol', 'Paquete PAQUETE HD', 'Paquete PAQUETE HD ', 'Paquete PAQUETE HD PLUS', 'Paquete PLAN FULL HD', 'Paquete PLAN FULL HD - PACK_BASICO', 'Paquete PREMIUM GOLDEN', 'Paquete PREMIUM HBO', 'Paquete PREMIUM HD PLUS', 'Paquete Pack Star Premium', 'Paquete Premium', 'Paquete Premium Futbol', 'Paquete Premium Golden', 'Paquete SUPER BOX', 'Paquete SUPER IPTV', 'Paquete TV ADULTO', 'Paquete TV ADULTOS', 'Paquete TV ADULTOS ', 'Paquete TV Avanzado HD', 'Paquete TV Avanzado HD PLUS', 'Paquete TV Avanzado HD Plus', 'Paquete TV Avanzado HD Plus TS', 'Paquete TV Avanzado HD TS', 'Paquete TV Claro TV GO', 'Paquete TV Digital Fox Premium', 'Paquete TV EXTENDIDO ', 'Paquete TV FOX ', 'Paquete TV FSN ', 'Paquete TV FULL', 'Paquete TV GOLDEN PREMIER', 'Paquete TV GOLDEN PREMIER ', 'Paquete TV HBO', 'Paquete TV HBO Premium', 'Paquete TV HBOLAB ', 'Paquete TV HD', 'Paquete TV HD PLUS', 'Paquete TV HOT', 'Paquete TV NHK', 'Paquete TV PREPAGO', 'Paquete TV PRO HD', 'Paquete TV PRO HD MAS', 'Paquete TV PRUEBA', 'Paquete TV PRUEBA ', 'Paquete TV PRUEBA TimeShift 24 NPVR 100', 'Paquete TV Premium HBO MAX', 'Paquete TV TS 24 NPVR 100', 'Paquete TV en Vivo ', 'Paquete TV_BASICA_HFC_DTH', 'Paquete TyC Sports Futbol Argentina', 'Paquete Universal Plus', 'Paquete V EXTENDIDO PRUEBA', 'Paquete WIN SPORTS PREMIUM', 'Paquete_Avanzado_HD', 'Paquete_Avanzado_HD_Extra', 'Paquete_Avanzado_HD_NS', 'Paquete_Avanzado_HD_Plus', 'Paquete_Avanzado_HD_Plus_NS', 'Paquete_TV_en_Vivo_FAKE', 'Premium FOX PLUS', 'Premium Universal+', 'REGIONAL PLUS', 'RTVEplay', 'SALTA HD', 'SALTA PLUS', 'SMART PLUS - PREMIUM ', 'STINGRAY KARAOKE', 'STINGRAY QELLO', 'TELECINE', 'TV - AVANZADO', 'TV - BASICO', 'TV - Premium', 'TV Básica', 'TV EN VIVO', 'TV EN VIVO ', 'TV GRILLA REDUCIDA 20', 'TV Grilla Reducida', 'TV_ADULTOS_NS', 'TV_CLARO_TV_GO_STANDARD', 'TV_CLARO_TV_GO_STANDARD_PLUS', 'Telmexmexico_abono_TV_EN_VIVO_FAKE', 'Tigo Sports', 'ULTRA DEPORTES', 'UNIVERSAL PLUS IPTV', 'UNIVERSAL_PLUS', 'Universal Plus', 'VENUS IPTV', 'WIN SPORTS+', 'WIN_SPORTS_WIN_SPORT_PLUS_FAKE', 'nacional tv con costo') AND ((bq_ca_pais_hub.FECHA_BAJA ) IS NULL AND (bq_ca_dim_pais.PAIS ) IS NOT NULL))
                    LIMIT 1"""
            

        # Obtener los resultados
        query_job = client.query(query)

        results = query_job.result()
        row = next(results)
        # Acceder al valor del número en la primera fila
        suscripciones = row[0]
        # Mostrar el valor en el formato deseado
        print(f"Suscripciones en Reporte de Suscripciones ClaroVideo/ClaroTV.: {suscripciones}")