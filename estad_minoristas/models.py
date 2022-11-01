from lib2to3.pgen2.token import NAME
from pickle import TRUE
from statistics import mode
from tkinter.tix import Tree
from django.db import models
from djmoney.models.fields import MoneyField

# Dimension tables
class N_Producto(models.Model):
    prod_id = models.IntegerField(name='Prod_Id',primary_key=True)
    prod_IdSentai = models.CharField(name='Prod_IdSentai',max_length=20,null = True)
    codigo_barra = models.CharField(name='Prod_CodigoBarra',max_length=40,null = True)
    descripcion = models.CharField(name='Prod_Descripcion',max_length=200,null = True)
    id_origen = models.IntegerField(name ='Prod_IdOrigen',null = True)
    origen = models.CharField(name='Prod_Origen',max_length=20,null = True)
    unidad_menor = models.CharField(name='Prod_UnidadMenor',max_length=15,null = True)
    forma_traza = models.CharField(name='Prod_FormaTraza',max_length=20,null = True)
    costo_inicial = MoneyField(max_digits=14,name = 'Prod_CostoInicial',null = True)
    costo_total = MoneyField(max_digits=14,name = 'Prod_CostoTotal',null = True)
    arancel = MoneyField(max_digits=14,name='Prod_Arancel',null = True)
    margen_distribucion = models.FloatField(name='Prod_MargenDistribucion',max_length=53,null = True)
    precio_base = MoneyField(max_digits=14,name='Prod_PrecioBase',null = True)
    dep_id_oltp = models.CharField(name='Dep_IdOLTP',max_length=12,null = True)
    dep_descripcion = models.CharField(name='Dep_Descripcion',max_length=255,null = True)
    seccion_id_oltp = models.CharField(name='Sec_IdOLTP',max_length=12,null = True)
    seccion_descripcion = models.CharField(name='Sec_Descripcion',max_length=255,null = True)
    linea_id_oltp = models.CharField(name='Lin_IdOLTP',max_length=12,null = True)
    linea_descripcion = models.CharField(name='Lin_Descripcion',max_length=255,null = True)
    circular_mup = models.IntegerField(name='Prod_CircularMUP',null = True)
    primera_circular_mup = models.CharField(name ='Prod_PrimeraCircularMUP',max_length=15,null = True)
    suministrador_minorista = models.IntegerField(name='Prod_SuministradorMinorista',null = True)
    suministrador_id_oltp = models.CharField(name="Prod_SuministradorIdOLTP",max_length=20,null = True)
    suministrador_descripcion = models.CharField(name="Prod_SuministradorDescripcion",max_length=100,null = True)
    volumen = MoneyField(max_digits=14,name = 'Prod_Volumen',null = True)
    unidad_volumen = models.CharField(name ='Prod_UnidadVolumen',max_length=20,null = True)
    peso = MoneyField(max_digits=14,name='Prod_Peso',null = True)
    unidad_peso = models.CharField(name='Prod_UnidadPeso',max_length=20,null = True)
    mt_bandera_activo = models.CharField(name='MT_BanderaActivo',max_length=20,null = True)

class N_Establecimiento(models.Model):
    est_id = models.IntegerField(name="Est_IdODS",primary_key=True)
    codigo = models.CharField(name='Est_Codigo',max_length=50,null = True)
    descripcion = models.CharField(name="Est_Descripcion",max_length=255,null = True)
    codigo_estructurado = models.CharField(name='Est_CodigoEstructurado',max_length=50,null = True)
    suc_id = models.IntegerField(name='Suc_IdODS',null = True)
    suc_codigo = models.CharField(name='Suc_Codigo',max_length=2,null = True)
    suc_nombre = models.CharField(name='Suc_Nombre',max_length=255,null = True)
    comp_id = models.IntegerField(name='Comp_IdODS',null = True)
    comp_codigo = models.CharField(name='Comp_Codigo',max_length=50,null = True)
    comp_nombre  = models.CharField(name='Comp_Nombre',max_length=255,null = True)
    es_interno =models.BooleanField(name='Est_EsInterno',null = True)
    padre_id = models.IntegerField(name='Est_PadreIdODS',null = True)
    padre_codigo = models.CharField(name='Est_PadreCodigo',max_length=50,null = True)
    padre_descripcion = models.CharField(name='Est_PadreDescripcion',max_length=255,null = True)
    nivel =models.IntegerField(name='Est_Nivel',null = True)
    codigo_actividad = models.IntegerField(name='Est_ActividadCodigo',null = True)
    actividad = models.CharField(name='Est_Actividad',max_length=255,null = True)
    codigo_clasif_id = models.IntegerField(name='Est_ClasificacionCodigoId',null = True)
    codigo_clasificacion = models.CharField(name= 'Est_ClasificacionCodigo',max_length=20,null = True)
    clasificacion = models.CharField(name='Est_Clasificacion',max_length=255,null = True)
    inv_sist_inf_codigo = models.CharField(name='Est_CodigoSistInformaticoInv',max_length=20,null = True)
    sist_inv = models.CharField(name='Est_SistemaInventario',max_length=50,null = True)
    es_dependiente = models.BooleanField(name='Est_EsDependiente',null = True)
    dpa = models.CharField(name='Dpa',max_length=4,null = True)
    cod_tipo_est_id = models.IntegerField(name='Est_TipoEstabCodigoId',null = True)
    tipo_est_cod = models.CharField(name='Est_TipoEstabCodigo',max_length=20,null = True)
    tipo_est = models.CharField(name='Est_TipoEstab' ,max_length=255,null = True)
    mt_fecha_actualizacion = models.DateField(name= 'MT_FechaActualizacion',null = True)
    path = models.CharField(name='Path',max_length=100,null = True)
    mt_activo = models.BooleanField(name='MT_Activo',null = True)
    sist_inv_id_ods = models.IntegerField(name='Est_SistemaInventarioIdOds',null = True)
    sist_inv_nombre = models.CharField(name='Est_SistemaInventarioNombre',max_length=255,null = True)

class N_Proveedor(models.Model):
    prov_id = models.IntegerField(name='Prov_IdODS',primary_key=True)
    prov_id_oltp = models.CharField(name= 'Prov_IdOLTP', max_length=20,null = True)
    nombre = models.CharField(name='Prov_Nombre',max_length=255,null = True)
    cod_panamericano = models.CharField(name='Prov_CodigoPanamericano',max_length=15,null = True)
    organismo = models.CharField(name='Prov_Organismo',max_length=100,null = True)
    tipo_id_ods = models.IntegerField(name='TipoProv_IdODS',null = True)
    tipo_descripcion = models.CharField(name='TipoProv_Descripcion',max_length=30,null = True)
    codigo_mup =models.CharField(name='Prov_CodigoMUP',max_length=15,null = True)
    nombre_mup =models.CharField(name='Prov_NombreMUP',max_length=100,null = True)
    tipo_mup =models.CharField(name='Prov_TipoMUP',max_length=100,null = True)
    organismo_mup =models.CharField(name='Prov_OrganismoMUP',max_length=50,null = True)
    tipo_mup_id_ods = models.IntegerField(name="Prov_TipoMUPIdODS",null = True)
    mt_activo = models.BooleanField(name='MT_Activo',null = True)
    organismo_id = models.IntegerField(name='Organismo_IdOds',null=True)
    organismo_id_oltp = models.CharField(name='Organismo_IdOLTP',max_length=50,null=True)
    organismo_nombre = models.CharField(name='Organismo_Nombre',max_length=255,null=True)

class N_Periodo(models.Model):
    periodo_id = models.IntegerField(name='Periodo_IdODS')
    descripcion =models.CharField(name='Periodo_Descripcion',max_length=200, null=True)
    fecha_inicio = models.DateField(name='Periodo_FechaInicio',null=True)
    fecha_fin = models.DateField(name='Periodo_FechaFin',null=True)
 
class N_Actividad(models.Model):
    act_cod= models.CharField(name='Act_Codigo',primary_key=True,max_length=2)
    descripcion = models.CharField(name='Act_Descripcion',max_length=255,null=True)

class N_TipoArea(models.Model):
    tipo_area_id = models.IntegerField(name='TipoArea_Id',primary_key=True)
    nombre = models.CharField(name='TipoArea_Nombre',max_length=50,null=True)

class N_Familia(models.Model):
    fam_id = models.CharField(name='Fam_IdOLTP',max_length=10,null=True)
    linea_id = models.CharField(name='Lin_IdOLTP',max_length=10,null=True)
    seccion_id = models.CharField(name='Sec_IdOLTP',max_length=10,null=True)
    dep_id = models.CharField(name='Dep_IdOLTP',max_length=10,null=True)
    linea_descrip = models.CharField(name='Lin_Descripcion',max_length=255,null=True)
    seccion_descrip = models.CharField(name='Sec_Descripcion',max_length=255,null=True)
    dep_descrip = models.CharField(name='Dep_Descripcion',max_length=255,null=True)
    nivel = models.IntegerField(name='Fam_Nivel')
    ind_one_id= models.IntegerField(name='IndONE_Id',null=True)
    is_deleted = models.BooleanField(name='IsDeleted',null=True)


#Fact tables
class Ventas(models.Model):
    #key
    prod_id = models.IntegerField(name = 'Prod_Id',primary_key=True)
    est_id = models.IntegerField(name='Est_Id',unique=True)
    prov_id = models.IntegerField(name = 'Prov_Id',unique=True)
    periodo_id = models.IntegerField(name= 'Periodo_Id',unique=True)
    act_id = models.IntegerField(name='Act_Id', unique=True)
    area_tipo_codigo = models.IntegerField(name='AreaTipo_Id',unique=True)

    #attributes
    cantidad = models.FloatField(name='Venta_Cantidad',null = True)
    costo = MoneyField(max_digits=14,name='Venta_Costo',null = True)
    importe = MoneyField(max_digits=14,name='Venta_Importe',null = True)
    cantidad_prom = models.FloatField(name='VentaProm_Cantidad',null = True)
    costo_prom = MoneyField(max_digits=14,name='VentaProm_Costo',null = True)
    importe_prom = MoneyField(max_digits=14,name='VentaProm_Importe',null = True)
    cant_semestre = models.FloatField(name='VentaSemestre_Cantidad',null = True)
    costo_semestre = MoneyField(max_digits=14,name='VentaSemestre_Costo',null = True)
    importe_semestre = MoneyField(max_digits=14,name='VentaSemestre_Importe',null = True)
    cant_anno_anterior = models.FloatField(name='VentaAnnoAnt_Cantidad',null = True)
    costo_anno_anterior = MoneyField(max_digits=14,name='VentaAnnoAnt_Costo',null = True)
    importe_anno_anterior = MoneyField(max_digits=14,name='VentaAnnoAnt_Importe',null = True)
    costo_nacional= MoneyField(max_digits=14,name = 'Venta_Costo_Nacional',null = True)
    importe_nacional_anno_ant = MoneyField(max_digits=14,name = 'VentaAnnoAnt_Importe_Nacional',null = True) 

class Compra(models.Model):
    #key
    prod_id = models.IntegerField(name = 'Prod_Id',primary_key=True)
    est_id = models.IntegerField(name='Est_Id',unique=True)
    prov_id = models.IntegerField(name = 'Prov_Id',unique=True)
    periodo_id = models.IntegerField(name= 'Periodo_Id',unique=True)
    act_id = models.IntegerField(name='Act_Id', unique=True)
    area_tipo_codigo = models.IntegerField(name='AreaTipo_Id',unique=True)

    #attributes
    cantidad = models.FloatField(name='Compra_Cantidad',null = True)
    costo = MoneyField(max_digits=14,name='Compra_Costo',null = True) 
    cant_anno_anterior = models.FloatField(name='CompraAnnoAnt_Cantidad',null = True)
    costo_anno_anterior = MoneyField(max_digits=14,name='CompraAnnoAnt_Costo',null = True)
    costo_nacional= MoneyField(max_digits=14,name = 'Compra_Costo_Nacional',null = True)
    costo_nacional_anno_ant = MoneyField(max_digits=14,name = 'CompraAnnoAnt_Costo_Nacional',null = True)

class Inventario(models.Model):
    #key
    prod_id = models.IntegerField(name = 'Prod_Id',primary_key=True)
    est_id = models.IntegerField(name='Est_Id',unique=True)
    prov_id = models.IntegerField(name = 'Prov_Id',unique=True)
    periodo_id = models.IntegerField(name= 'Periodo_Id',unique=True)
    act_id = models.IntegerField(name='Act_Id', unique=True)
    area_tipo_codigo = models.IntegerField(name='AreaTipo_Id',unique=True)

    #attributes
    cantidad = models.FloatField(name='Inv_Cantidad,null = True')
    costo = MoneyField(max_digits=14,name='Inv_Costo',null = True)
    cant_prom = models.FloatField(name = 'InvProm_Cantidad',null = True)
    dias_existencia = models.IntegerField(name='Inv_DiasExistencia',null = True)
    pot_dias_existencia = models.IntegerField(name='Inv_PotenciasDiasExistencia',null = True)
    cantinicial = models.IntegerField(name='InvInicial_Cantidad',null = True)
    costo_inicial = MoneyField(max_digits=14,name='InvInicial_Costo',null = True)
    pot_dias_existencia = models.IntegerField(name='Inv_PotenciasDiasExistencia',null = True)
    mes_cant_prom = models.IntegerField( name='InvPromMes_Cantidad',null = True)
    mes_costo_prom = MoneyField(max_digits=14,name= 'InvPromMes_Costo',null = True)
    cant_prom = models.IntegerField(name= 'InvProm_Cantidad',null = True)
    costo_prom = MoneyField(max_digits=14,name= 'InvProm_Costo',null = True)
    dias_existencia_semestre = models.IntegerField(name='InvSemestre_DiasExistencia',null = True)
    uso_semestre= models.FloatField(name='InvSemestre_Uso',null = True)
    cant_anno_anterior = models.FloatField(name='InvAnnoAnt_Cantidad',null = True)
    costo_anno_anterior = MoneyField(max_digits=14,name='InvAnnoAnt_Costo',null = True)

class Ajuste(models.Model):
    #key
    prod_id = models.IntegerField(name = 'Prod_Id',primary_key=True)
    est_id = models.IntegerField(name='Est_Id',unique=True)
    prov_id = models.IntegerField(name = 'Prov_Id',unique=True)
    periodo_id = models.IntegerField(name= 'Periodo_Id',unique=True)
    act_id = models.IntegerField(name='Act_Id', unique=True)
    area_tipo_codigo = models.IntegerField(name='AreaTipo_Id',unique=True)

    #attributes
    cantidad = models.FloatField(name='Ajuste_Cantidad',max_length=53,null=True)
    costo = MoneyField(max_digits=14,name ='Ajuste_Costo',null=True)
    importe = MoneyField(max_digits=14,name ='Ajuste_Importe',null=True)
    cantidad_anno_ant = models.FloatField(name='AjusteAnnoAnt_Cantidad',max_length=53)
    costo_anno_ant = MoneyField(max_digits=14,name ='AjusteAnnoAnt_Costo',null=True)
    importe_anno_ant = MoneyField(max_digits=14,name ='AjusteAnnoAnt_Importe',null=True)

class Transferencia(models.Model):
    #key
    prod_id = models.IntegerField(name = 'Prod_Id',primary_key=True)
    est_id = models.IntegerField(name='Est_Id',unique=True)
    prov_id = models.IntegerField(name = 'Prov_Id',unique=True)
    periodo_id = models.IntegerField(name= 'Periodo_Id',unique=True)
    act_id = models.IntegerField(name='Act_Id', unique=True)
    area_tipo_codigo = models.IntegerField(name='AreaTipo_Id',unique=True)
    
    #attributes
    cantidad = models.FloatField(name='Transf_Cantidad',max_length=53,null=True)
    costo = MoneyField(max_digits=14,name ='Transf_Costo',null=True)
    cantidad_anno_ant = models.FloatField(name='TransfAnnoAnt_Cantidad',max_length=53)
    costo_anno_ant = MoneyField(max_digits=14,name ='TransfAnnoAnt_Costo',null=True)

