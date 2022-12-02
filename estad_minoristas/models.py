from lib2to3.pgen2.token import NAME
from pickle import TRUE
from statistics import mode
from tkinter.tix import Tree
from django.db import models

# Dimension tables
class N_Producto(models.Model):
    prod_id = models.IntegerField(name='prod_id',primary_key=True)
    prod_rec_no = models.IntegerField(name = 'prod_recno',null=True)
    prod_IdSentai = models.CharField(name='prod_id_sentai',max_length=20,null = True)
    codigo_barra = models.CharField(name='prod_codigo_barra',max_length=40,null = True)
    descripcion = models.TextField(name='prod_descripcion',max_length = 9999999,null = True)
    id_origen = models.IntegerField(name ='prod_id_origen',null = True)
    origen = models.CharField(name='prod_origen',max_length=20,null = True)
    unidad_menor = models.CharField(name='prod_unidad_menor',max_length=15,null = True)
    forma_traza = models.CharField(name='prod_forma_traza',max_length=20,null = True)
    costo_inicial = models.FloatField(name = 'prod_costo_inicial',null = True)
    costo_total = models.FloatField(name = 'prod_costo_total',null = True)
    arancel = models.FloatField(name='prod_arancel',null = True)
    margen_distribucion = models.FloatField(name='prod_margen_distribucion',max_length=53,null = True)
    precio_base = models.FloatField(name='prod_precio_base',null = True)
    dep_id_oltp = models.CharField(name='dep_id_oltp',max_length=12,null = True)
    dep_descripcion = models.CharField(name='dep_descripcion',max_length=255,null = True)
    seccion_id_oltp = models.CharField(name='sec_idoltp',max_length=12,null = True)
    seccion_descripcion = models.CharField(name='sec_descripcion',max_length=255,null = True)
    linea_id_oltp = models.CharField(name='lin_idoltp',max_length=12,null = True)
    linea_descripcion = models.CharField(name='lin_descripcion',max_length=255,null = True)
    circular_mup = models.IntegerField(name='prod_circular_mup',null = True)
    primera_circular_mup = models.CharField(name ='prod_primera_circular_mup',max_length=15,null = True)
    suministrador_minorista = models.IntegerField(name='prod_suministrador_minorista',null = True)
    suministrador_id_oltp = models.CharField(name="prod_suministrador_id_oltp",max_length=20,null = True)
    suministrador_descripcion = models.CharField(name="prod_suministrador_descripcion",max_length=100,null = True)
    volumen = models.FloatField(name = 'prod_volumen',null = True)
    unidad_volumen = models.CharField(name ='prod_unidad_volumen',max_length=20,null = True)
    peso = models.FloatField(name='prod_peso',null = True)
    unidad_peso = models.CharField(name='prod_unidad_peso',max_length=20,null = True)
    mt_bandera_activo = models.CharField(name='mt_bandera_activo',max_length=20,null = True)

class N_Establecimiento(models.Model):
    est_id = models.IntegerField(name="est_id_ods",primary_key=True)
    codigo = models.CharField(name='est_codigo',max_length=50,null = True)
    descripcion = models.CharField(name="est_descripcion",max_length=255,null = True)
    codigo_estructurado = models.CharField(name='est_codigo_estructurado',max_length=50,null = True)
    suc_id = models.IntegerField(name='suc_id_ods',null = True)
    suc_codigo = models.CharField(name='suc_codigo',max_length=2,null = True)
    suc_nombre = models.CharField(name='suc_nombre',max_length=255,null = True)
    comp_id = models.IntegerField(name='comp_id_ods',null = True)
    comp_codigo = models.CharField(name='comp_codigo',max_length=50,null = True)
    comp_nombre  = models.CharField(name='comp_nombre',max_length=255,null = True)
    es_interno =models.BooleanField(name='est_es_interno',null = True)
    padre_id = models.IntegerField(name='est_padre_id_ods',null = True)
    padre_codigo = models.CharField(name='est_padre_codigo',max_length=50,null = True)
    padre_descripcion = models.CharField(name='est_padre_descripcion',max_length=255,null = True)
    nivel =models.IntegerField(name='est_nivel',null = True)
    codigo_actividad = models.IntegerField(name='est_actividad_codigo',null = True)
    actividad = models.CharField(name='est_actividad',max_length=255,null = True)
    codigo_clasif_id = models.IntegerField(name='est_clasificacion_codigo_id',null = True)
    codigo_clasificacion = models.CharField(name= 'est_clasificacion_codigo',max_length=20,null = True)
    clasificacion = models.CharField(name='est_clasificacion',max_length=255,null = True)
    inv_sist_inf_codigo = models.CharField(name='est_codigo_sist_informatico_inv',max_length=20,null = True)
    sist_inv = models.CharField(name='est_sistema_inventario',max_length=50,null = True)
    es_dependiente = models.BooleanField(name='est_es_dependiente',null = True)
    dpa = models.CharField(name='dpa',max_length=4,null = True)
    cod_tipo_est_id = models.IntegerField(name='est_tipo_estab_codigo_id',null = True)
    tipo_est_cod = models.CharField(name='est_tipo_estab_codigo',max_length=20,null = True)
    tipo_est = models.CharField(name='est_tipo_estab' ,max_length=255,null = True)
    mt_fecha_actualizacion = models.DateField(name= 'mt_fecha_actualizacion',null = True)
    path = models.CharField(name='path',max_length=100,null = True)
    mt_activo = models.BooleanField(name='mt_activo',null = True)
    sist_inv_id_ods = models.IntegerField(name='est_sistema_inventario_id_ods',null = True)
    sist_inv_nombre = models.CharField(name='est_sistema_inventario_nombre',max_length=255,null = True)

class N_Proveedor(models.Model):
    prov_id = models.IntegerField(name='prov_id_ods',primary_key=True)
    prov_id_oltp = models.CharField(name= 'prov_id_oltp', max_length=20,null = True)
    nombre = models.CharField(name='prov_nombre',max_length=255,null = True)
    cod_panamericano = models.CharField(name='prov_codigo_panamericano',max_length=15,null = True)
    organismo = models.CharField(name='prov_organismo',max_length=100,null = True)
    tipo_id_ods = models.IntegerField(name='tipo_prov_id_ods',null = True)
    tipo_descripcion = models.CharField(name='tipo_prov_descripcion',max_length=255,null = True)
    codigo_mup =models.CharField(name='prov_codigo_mup',max_length=15,null = True)
    nombre_mup =models.CharField(name='prov_nombre_mup',max_length=100,null = True)
    tipo_mup =models.CharField(name='prov_tipo_mup',max_length=100,null = True)
    organismo_mup =models.CharField(name='prov_organismo_mup',max_length=50,null = True)
    tipo_mup_id_ods = models.IntegerField(name="prov_tipo_mup_id_ods",null = True)
    mt_activo = models.BooleanField(name='mt_activo',null = True)
    organismo_id = models.IntegerField(name='organismo_id_ods',null=True)
    organismo_id_oltp = models.CharField(name='organismo_id_oltp',max_length=50,null=True)
    organismo_nombre = models.CharField(name='organismo_nombre',max_length=255,null=True)

class N_Periodo(models.Model):
    periodo_id = models.IntegerField(name='periodo_id_ods',primary_key = True)
    descripcion =models.CharField(name='periodo_descripcion',max_length=200, null=True)
    fecha_inicio = models.DateField(name='periodo_fecha_inicio',null=True)
    fecha_fin = models.DateField(name='periodo_fecha_fin',null=True)
 
class N_Actividad(models.Model):
    act_cod= models.CharField(name='act_codigo',primary_key=True,max_length=2)
    descripcion = models.CharField(name='act_descripcion',max_length=255,null=True)

class N_TipoArea(models.Model):
    tipo_area_id = models.IntegerField(name='tipo_area_id',primary_key=True)
    nombre = models.CharField(name='tipo_area_nombre',max_length=50,null=True)

class N_Familia(models.Model):
    fam_id = models.CharField(name='fam_id_oltp',max_length=10, primary_key=True, default = '')
    linea_id = models.CharField(name='lin_id_oltp',max_length=10,null=True)
    seccion_id = models.CharField(name='sec_id_oltp',max_length=10,null=True)
    dep_id = models.CharField(name='dep_id_oltp',max_length=10,null=True)
    linea_descrip = models.CharField(name='lin_descripcion',max_length=255,null=True)
    seccion_descrip = models.CharField(name='sec_descripcion',max_length=255,null=True)
    dep_descrip = models.CharField(name='dep_descripcion',max_length=255,null=True)
    nivel = models.IntegerField(name='fam_nivel')
    ind_one_id= models.IntegerField(name='ind_one_Id',null=True)
    is_deleted = models.BooleanField(name='is_deleted',null=True)

class N_TipoCodigo(models.Model):
    tipo_cod_id = models.IntegerField(name= "tipo_cod_id",primary_key=True)	 
    tipo_cod_descripcion =models.CharField(name='tipo_cod_descripcion',max_length= 100)	

class N_OrigenProducto(models.Model):
    org_prod_id = models.IntegerField(name= "org_prod_id_ods",unique = True)	 
    origen_prod_descripcion =models.CharField(name='origen_prod_descripcion',max_length= 100)



#Fact tables
class Ventas_Producto_Establecimiento(models.Model):
    #key
    prod_id = models.ForeignKey(N_Producto,name = 'prod_id',on_delete=models.CASCADE)
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete= models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='venta_cantidad',null = True)
    costo = models.FloatField(name='venta_costo',null = True)
    importe = models.FloatField(name='venta_importe',null = True)
    cantidad_prom = models.FloatField(name='venta_prom_cantidad',null = True)
    costo_prom = models.FloatField(name='venta_prom_costo',null = True)
    importe_prom = models.FloatField(name='venta_prom_importe',null = True)
    cant_semestre = models.FloatField(name='venta_semestre_cantidad',null = True)
    costo_semestre = models.FloatField(name='venta_semestre_costo',null = True)
    importe_semestre = models.FloatField(name='venta_semestre_importe',null = True)
    cant_anno_anterior = models.FloatField(name='venta_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='venta_anno_ant_costo',null = True)
    importe_anno_anterior = models.FloatField(name='venta_anno_ant_importe',null = True)
    importe_nacional = models.FloatField(name = 'venta_importe_nacional',null = True) 
    importe_nacional_anno_ant = models.FloatField(name = 'venta_anno_ant_importe_nacional',null = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['prod_id','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'venta_prod_est')
        ]

class Compra_Producto_Establecimiento(models.Model):
    #key
    
    prod_id = models.ForeignKey(N_Producto,name = 'prod_id',on_delete=models.CASCADE)
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='compra_cantidad',null = True)
    costo = models.FloatField(name='compra_costo',null = True) 
    cant_anno_anterior = models.FloatField(name='compra_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='compra_anno_ant_costo',null = True)
    costo_nacional= models.FloatField(name = 'compra_costo_nacional',null = True)
    costo_nacional_anno_ant = models.FloatField(name = 'compra_anno_ant_costo_nacional',null = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['prod_id','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'compra_prod_est')
        ]

class Inventario_Producto_Establecimiento(models.Model):
    #key
    
    prod_id = models.ForeignKey(N_Producto,name = 'prod_id',on_delete=models.CASCADE)
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo_id = models.ForeignKey(N_TipoArea, name='area_tipo_id',on_delete=models.CASCADE, default = 1)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='inv_cantidad',null = True)
    costo = models.FloatField(name='inv_costo',null = True)
    dias_existencia = models.IntegerField(name='inv_dias_existencia',null = True)
    pot_dias_existencia = models.IntegerField(name='inv_potencias_dias_existencia',null = True)
    cant_inicial = models.IntegerField(name='inv_inicial_cantidad',null = True)
    costo_inicial = models.FloatField(name='inv_inicial_costo',null = True)
    mes_cant_prom = models.IntegerField( name='inv_prom_mes_cantidad',null = True)
    mes_costo_prom = models.FloatField(name= 'inv_prom_mes_costo',null = True)
    cant_prom = models.FloatField(name= 'inv_prom_cantidad',null = True,max_length=53)
    costo_prom = models.FloatField(name= 'inv_prom_costo',null = True)
    dias_existencia_semestre = models.IntegerField(name='inv_semestre_dias_existencia',null = True)
    uso_semestre= models.FloatField(name='inv_semestre_uso',null = True)
    cant_anno_anterior = models.FloatField(name='inv_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='inv_anno_ant_costo',null = True)
    area_tipo =  models.CharField(name = 'area_tipo', max_length= 12,null = True, default = '' )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['prod_id','est_id','prov_id','periodo_id','act_id','area_tipo_id','tipo_cod_id'],name= 'inv_prod_est')
        ]

class Ajuste_Producto_Establecimiento(models.Model):
    #key
    
    prod_id = models.ForeignKey(N_Producto,name = 'prod_id',on_delete=models.CASCADE)
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='ajuste_cantidad',max_length=53,null=True)
    costo = models.FloatField(name ='ajuste_costo',null=True)
    importe = models.FloatField(name ='ajuste_importe',null=True)
    cantidad_anno_ant = models.FloatField(name='ajuste_anno_ant_cantidad',max_length=53)
    costo_anno_ant = models.FloatField(name ='ajuste_anno_ant_costo',null=True)
    importe_anno_ant = models.FloatField(name ='ajuste_anno_ant_importe',null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['prod_id','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'ajuste_prod_est')
        ]

class Transferencia_Producto_Establecimiento(models.Model):
    #key
    
    prod_id = models.ForeignKey(N_Producto,name = 'prod_id',on_delete=models.CASCADE)
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)
    
    #attributes
    cantidad = models.FloatField(name='transf_cantidad',max_length=53,null=True)
    costo = models.FloatField(name ='transf_costo',null=True)
    cantidad_anno_ant = models.FloatField(name='transf_anno_ant_cantidad',max_length=53)
    costo_anno_ant = models.FloatField(name ='transf_anno_ant_costo',null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['prod_id','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'transf_prod_est')
        ]

###Aggregations###

#Producto_Sucursal
class Ventas_Producto_Sucursal(models.Model):
    #key
    prod_id = models.ForeignKey(N_Producto,name = 'prod_id',on_delete=models.CASCADE)
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='venta_cantidad',null = True)
    costo = models.FloatField(name='venta_costo',null = True)
    importe = models.FloatField(name='venta_importe',null = True)
    cantidad_prom = models.FloatField(name='venta_prom_cantidad',null = True)
    costo_prom = models.FloatField(name='venta_prom_costo',null = True)
    importe_prom = models.FloatField(name='venta_prom_importe',null = True)
    cant_semestre = models.FloatField(name='venta_semestre_cantidad',null = True)
    costo_semestre = models.FloatField(name='venta_semestre_costo',null = True)
    importe_semestre = models.FloatField(name='venta_semestre_importe',null = True)
    cant_anno_anterior = models.FloatField(name='venta_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='venta_anno_ant_costo',null = True)
    importe_anno_anterior = models.FloatField(name='venta_anno_ant_importe',null = True)
    importe_nacional = models.FloatField(name = 'venta_importe_nacional',null = True) 
    importe_nacional_anno_ant = models.FloatField(name = 'venta_anno_ant_importe_nacional',null = True) 

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['prod_id','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'venta_prod_suc')
        ]

class Compra_Producto_Sucursal(models.Model):
    #key
    
    prod_id = models.ForeignKey(N_Producto,name = 'prod_id',on_delete=models.CASCADE)
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='compra_cantidad',null = True)
    costo = models.FloatField(name='compra_costo',null = True) 
    cant_anno_anterior = models.FloatField(name='compra_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='compra_anno_ant_costo',null = True)
    costo_nacional= models.FloatField(name = 'compra_costo_nacional',null = True)
    costo_nacional_anno_ant = models.FloatField(name = 'compra_anno_ant_costo_nacional',null = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['prod_id','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'compra_prod_suc')
        ]

class Inventario_Producto_Sucursal(models.Model):
    #key
    prod_id = models.ForeignKey(N_Producto,name = 'prod_id',on_delete=models.CASCADE)
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='inv_cantidad',null = True)
    costo = models.FloatField(name='inv_costo',null = True)
    dias_existencia = models.IntegerField(name='inv_dias_existencia',null = True)
    pot_dias_existencia = models.IntegerField(name='inv_potencias_dias_existencia',null = True)
    cant_inicial = models.IntegerField(name='inv_inicial_cantidad',null = True)
    costo_inicial = models.FloatField(name='inv_inicial_costo',null = True)
    mes_cant_prom = models.IntegerField( name='inv_prom_mes_cantidad',null = True)
    mes_costo_prom = models.FloatField(name= 'inv_prom_mes_costo',null = True)
    cant_prom = models.FloatField(name= 'inv_prom_cantidad',null = True,max_length=53)
    costo_prom = models.FloatField(name= 'inv_prom_costo',null = True)
    dias_existencia_semestre = models.IntegerField(name='inv_semestre_dias_existencia',null = True)
    uso_semestre= models.FloatField(name='inv_semestre_uso',null = True)
    cant_anno_anterior = models.FloatField(name='inv_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='inv_anno_ant_costo',null = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['prod_id','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'inv_prod_suc')
        ]

class Ajuste_Producto_Sucursal(models.Model):
    #key
    
    prod_id = models.ForeignKey(N_Producto,name = 'prod_id',on_delete=models.CASCADE)
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='ajuste_cantidad',max_length=53,null=True)
    costo = models.FloatField(name ='ajuste_costo',null=True)
    importe = models.FloatField(name ='ajuste_importe',null=True)
    cantidad_anno_ant = models.FloatField(name='ajuste_anno_ant_cantidad',max_length=53)
    costo_anno_ant = models.FloatField(name ='ajuste_anno_ant_costo',null=True)
    importe_anno_ant = models.FloatField(name ='ajuste_anno_ant_importe',null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['prod_id','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'ajuste_prod_suc')
        ]

class Transferencia_Producto_Sucursal(models.Model):
    #key
    
    prod_id = models.ForeignKey(N_Producto,name = 'prod_id',on_delete=models.CASCADE)
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)
    
    #attributes
    cantidad = models.FloatField(name='transf_cantidad',max_length=53,null=True)
    costo = models.FloatField(name ='transf_costo',null=True)
    cantidad_anno_ant = models.FloatField(name='transf_anno_ant_cantidad',max_length=53)
    costo_anno_ant = models.FloatField(name ='transf_anno_ant_costo',null=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['prod_id','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'transf_prod_suc')
        ]

#Producto_Complejo
class Ventas_Producto_Complejo(models.Model):
    #key
    
    prod_id = models.ForeignKey(N_Producto,name = 'prod_id',on_delete=models.CASCADE)
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='venta_cantidad',null = True)
    costo = models.FloatField(name='venta_costo',null = True)
    importe = models.FloatField(name='venta_importe',null = True)
    cantidad_prom = models.FloatField(name='venta_prom_cantidad',null = True)
    costo_prom = models.FloatField(name='venta_prom_costo',null = True)
    importe_prom = models.FloatField(name='venta_prom_importe',null = True)
    cant_semestre = models.FloatField(name='venta_semestre_cantidad',null = True)
    costo_semestre = models.FloatField(name='venta_semestre_costo',null = True)
    importe_semestre = models.FloatField(name='venta_semestre_importe',null = True)
    cant_anno_anterior = models.FloatField(name='venta_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='venta_anno_ant_costo',null = True)
    importe_anno_anterior = models.FloatField(name='venta_anno_ant_importe',null = True)
    importe_nacional = models.FloatField(name = 'venta_importe_nacional',null = True) 
    importe_nacional_anno_ant = models.FloatField(name = 'venta_anno_ant_importe_nacional',null = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['prod_id','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'venta_prod_complejo')
        ]

class Compra_Producto_Complejo(models.Model):
    #key
    
    prod_id = models.ForeignKey(N_Producto,name = 'prod_id',on_delete=models.CASCADE)
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='compra_cantidad',null = True)
    costo = models.FloatField(name='compra_costo',null = True) 
    cant_anno_anterior = models.FloatField(name='compra_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='compra_anno_ant_costo',null = True)
    costo_nacional= models.FloatField(name = 'compra_costo_nacional',null = True)
    costo_nacional_anno_ant = models.FloatField(name = 'compra_anno_ant_costo_nacional',null = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['prod_id','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'compra_prod_complejo')
        ]

class Inventario_Producto_Complejo(models.Model):
    #key
    
    prod_id = models.ForeignKey(N_Producto,name = 'prod_id',on_delete=models.CASCADE)
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='inv_cantidad',null = True)
    costo = models.FloatField(name='inv_costo',null = True)
    dias_existencia = models.IntegerField(name='inv_dias_existencia',null = True)
    pot_dias_existencia = models.IntegerField(name='inv_potencias_dias_existencia',null = True)
    cant_inicial = models.IntegerField(name='inv_inicial_cantidad',null = True)
    costo_inicial = models.FloatField(name='inv_inicial_costo',null = True)
    mes_cant_prom = models.IntegerField( name='inv_prom_mes_cantidad',null = True)
    mes_costo_prom = models.FloatField(name= 'inv_prom_mes_costo',null = True)
    cant_prom = models.FloatField(name= 'inv_prom_cantidad',null = True,max_length=53)
    costo_prom = models.FloatField(name= 'inv_prom_costo',null = True)
    dias_existencia_semestre = models.IntegerField(name='inv_semestre_dias_existencia',null = True)
    uso_semestre= models.FloatField(name='inv_semestre_uso',null = True)
    cant_anno_anterior = models.FloatField(name='inv_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='inv_anno_ant_costo',null = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['prod_id','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'inv_prod_complejo')
        ]

class Ajuste_Producto_Complejo(models.Model):
    #key
    
    prod_id = models.ForeignKey(N_Producto,name = 'prod_id',on_delete=models.CASCADE)
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='ajuste_cantidad',max_length=53,null=True)
    costo = models.FloatField(name ='ajuste_costo',null=True)
    importe = models.FloatField(name ='ajuste_importe',null=True)
    cantidad_anno_ant = models.FloatField(name='ajuste_anno_ant_cantidad',max_length=53)
    costo_anno_ant = models.FloatField(name ='ajuste_anno_ant_costo',null=True)
    importe_anno_ant = models.FloatField(name ='ajuste_anno_ant_importe',null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['prod_id','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'ajuste_prod_complejo')
        ]

class Transferencia_Producto_Complejo(models.Model):
    #key
    
    prod_id = models.ForeignKey(N_Producto,name = 'prod_id',on_delete=models.CASCADE)
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)
    
    #attributes
    cantidad = models.FloatField(name='transf_cantidad',max_length=53,null=True)
    costo = models.FloatField(name ='transf_costo',null=True)
    cantidad_anno_ant = models.FloatField(name='transf_anno_ant_cantidad',max_length=53)
    costo_anno_ant = models.FloatField(name ='transf_anno_ant_costo',null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['prod_id','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'transf_prod_complejo')
        ]

#Linea_Establecimiento
class Ventas_Linea_Establecimiento(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='venta_cantidad',null = True)
    costo = models.FloatField(name='venta_costo',null = True)
    importe = models.FloatField(name='venta_importe',null = True)
    cantidad_prom = models.FloatField(name='venta_prom_cantidad',null = True)
    costo_prom = models.FloatField(name='venta_prom_costo',null = True)
    importe_prom = models.FloatField(name='venta_prom_importe',null = True)
    cant_semestre = models.FloatField(name='venta_semestre_cantidad',null = True)
    costo_semestre = models.FloatField(name='venta_semestre_costo',null = True)
    importe_semestre = models.FloatField(name='venta_semestre_importe',null = True)
    cant_anno_anterior = models.FloatField(name='venta_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='venta_anno_ant_costo',null = True)
    importe_anno_anterior = models.FloatField(name='venta_anno_ant_importe',null = True)
    importe_nacional = models.FloatField(name = 'venta_importe_nacional',null = True) 
    importe_nacional_anno_ant = models.FloatField(name = 'venta_anno_ant_importe_nacional',null = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'venta_linea_prod')
        ]

class Compra_Linea_Establecimiento(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='compra_cantidad',null = True)
    costo = models.FloatField(name='compra_costo',null = True) 
    cant_anno_anterior = models.FloatField(name='compra_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='compra_anno_ant_costo',null = True)
    costo_nacional= models.FloatField(name = 'compra_costo_nacional',null = True)
    costo_nacional_anno_ant = models.FloatField(name = 'compra_anno_ant_costo_nacional',null = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'compra_linea_prod')
        ]

class Inventario_Linea_Establecimiento(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)


    #attributes
    cantidad = models.FloatField(name='inv_cantidad',null = True)
    costo = models.FloatField(name='inv_costo',null = True)
    dias_existencia = models.IntegerField(name='inv_dias_existencia',null = True)
    pot_dias_existencia = models.IntegerField(name='inv_potencias_dias_existencia',null = True)
    cant_inicial = models.IntegerField(name='inv_inicial_cantidad',null = True)
    costo_inicial = models.FloatField(name='inv_inicial_costo',null = True)
    mes_cant_prom = models.IntegerField( name='inv_prom_mes_cantidad',null = True)
    mes_costo_prom = models.FloatField(name= 'inv_prom_mes_costo',null = True)
    cant_prom = models.FloatField(name= 'inv_prom_cantidad',null = True,max_length=53)
    costo_prom = models.FloatField(name= 'inv_prom_costo',null = True)
    dias_existencia_semestre = models.IntegerField(name='inv_semestre_dias_existencia',null = True)
    uso_semestre= models.FloatField(name='inv_semestre_uso',null = True)
    cant_anno_anterior = models.FloatField(name='inv_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='inv_anno_ant_costo',null = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'inv_linea_prod')
        ]

class Ajuste_Linea_Establecimiento(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)


    #attributes
    cantidad = models.FloatField(name='ajuste_cantidad',max_length=53,null=True)
    costo = models.FloatField(name ='ajuste_costo',null=True)
    importe = models.FloatField(name ='ajuste_importe',null=True)
    cantidad_anno_ant = models.FloatField(name='ajuste_anno_ant_cantidad',max_length=53)
    costo_anno_ant = models.FloatField(name ='ajuste_anno_ant_costo',null=True)
    importe_anno_ant = models.FloatField(name ='ajuste_anno_ant_importe',null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'ajuste_linea_prod')
        ]

class Transferencia_Linea_Establecimiento(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)
    
    #attributes
    cantidad = models.FloatField(name='transf_cantidad',max_length=53,null=True)
    costo = models.FloatField(name ='transf_costo',null=True)
    cantidad_anno_ant = models.FloatField(name='transf_anno_ant_cantidad',max_length=53)
    costo_anno_ant = models.FloatField(name ='transf_anno_ant_costo',null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'transf_linea_prod')
        ]


#Linea_Complejo
class Ventas_Linea_Complejo(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='venta_cantidad',null = True)
    costo = models.FloatField(name='venta_costo',null = True)
    importe = models.FloatField(name='venta_importe',null = True)
    cantidad_prom = models.FloatField(name='venta_prom_cantidad',null = True)
    costo_prom = models.FloatField(name='venta_prom_costo',null = True)
    importe_prom = models.FloatField(name='venta_prom_importe',null = True)
    cant_semestre = models.FloatField(name='venta_semestre_cantidad',null = True)
    costo_semestre = models.FloatField(name='venta_semestre_costo',null = True)
    importe_semestre = models.FloatField(name='venta_semestre_importe',null = True)
    cant_anno_anterior = models.FloatField(name='venta_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='venta_anno_ant_costo',null = True)
    importe_anno_anterior = models.FloatField(name='venta_anno_ant_importe',null = True)
    importe_nacional = models.FloatField(name = 'venta_importe_nacional',null = True) 
    importe_nacional_anno_ant = models.FloatField(name = 'venta_anno_ant_importe_nacional',null = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'venta_linea_complejo')
        ]

class Compra_Linea_Complejo(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='compra_cantidad',null = True)
    costo = models.FloatField(name='compra_costo',null = True) 
    cant_anno_anterior = models.FloatField(name='compra_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='compra_anno_ant_costo',null = True)
    costo_nacional= models.FloatField(name = 'compra_costo_nacional',null = True)
    costo_nacional_anno_ant = models.FloatField(name = 'compra_anno_ant_costo_nacional',null = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'compra_linea_complejo')
        ]

class Inventario_Linea_Complejo(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='inv_cantidad',null = True)
    costo = models.FloatField(name='inv_costo',null = True)
    dias_existencia = models.IntegerField(name='inv_dias_existencia',null = True)
    pot_dias_existencia = models.IntegerField(name='inv_potencias_dias_existencia',null = True)
    cant_inicial = models.IntegerField(name='inv_inicial_cantidad',null = True)
    costo_inicial = models.FloatField(name='inv_inicial_costo',null = True)
    mes_cant_prom = models.IntegerField( name='inv_prom_mes_cantidad',null = True)
    mes_costo_prom = models.FloatField(name= 'inv_prom_mes_costo',null = True)
    cant_prom = models.FloatField(name= 'inv_prom_cantidad',null = True,max_length=53)
    costo_prom = models.FloatField(name= 'inv_prom_costo',null = True)
    dias_existencia_semestre = models.IntegerField(name='inv_semestre_dias_existencia',null = True)
    uso_semestre= models.FloatField(name='inv_semestre_uso',null = True)
    cant_anno_anterior = models.FloatField(name='inv_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='inv_anno_ant_costo',null = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'inv_linea_complejo')
        ]

class Ajuste_Linea_Complejo(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='ajuste_cantidad',max_length=53,null=True)
    costo = models.FloatField(name ='ajuste_costo',null=True)
    importe = models.FloatField(name ='ajuste_importe',null=True)
    cantidad_anno_ant = models.FloatField(name='ajuste_anno_ant_cantidad',max_length=53)
    costo_anno_ant = models.FloatField(name ='ajuste_anno_ant_costo',null=True)
    importe_anno_ant = models.FloatField(name ='ajuste_anno_ant_importe',null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'ajuste_linea_complejo')
        ]

class Transferencia_Linea_Complejo(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)
    
    #attributes
    cantidad = models.FloatField(name='transf_cantidad',max_length=53,null=True)
    costo = models.FloatField(name ='transf_costo',null=True)
    cantidad_anno_ant = models.FloatField(name='transf_anno_ant_cantidad',max_length=53)
    costo_anno_ant = models.FloatField(name ='transf_anno_ant_costo',null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'transf__linea_complejo')
        ]


#Linea_Sucursal
class Ventas_Linea_Sucursal(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='venta_cantidad',null = True)
    costo = models.FloatField(name='venta_costo',null = True)
    importe = models.FloatField(name='venta_importe',null = True)
    cantidad_prom = models.FloatField(name='venta_prom_cantidad',null = True)
    costo_prom = models.FloatField(name='venta_prom_costo',null = True)
    importe_prom = models.FloatField(name='venta_prom_importe',null = True)
    cant_semestre = models.FloatField(name='venta_semestre_cantidad',null = True)
    costo_semestre = models.FloatField(name='venta_semestre_costo',null = True)
    importe_semestre = models.FloatField(name='venta_semestre_importe',null = True)
    cant_anno_anterior = models.FloatField(name='venta_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='venta_anno_ant_costo',null = True)
    importe_anno_anterior = models.FloatField(name='venta_anno_ant_importe',null = True)
    importe_nacional = models.FloatField(name = 'venta_importe_nacional',null = True) 
    importe_nacional_anno_ant = models.FloatField(name = 'venta_anno_ant_importe_nacional',null = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'venta_linea_sucursal')
        ]

class Compra_Linea_Sucursal(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='compra_cantidad',null = True)
    costo = models.FloatField(name='compra_costo',null = True) 
    cant_anno_anterior = models.FloatField(name='compra_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='compra_anno_ant_costo',null = True)
    costo_nacional= models.FloatField(name = 'compra_costo_nacional',null = True)
    costo_nacional_anno_ant = models.FloatField(name = 'compra_anno_ant_costo_nacional',null = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'compra_linea_sucursal')
        ]

class Inventario_Linea_Sucursal(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='inv_cantidad',null = True)
    costo = models.FloatField(name='inv_costo',null = True)
    dias_existencia = models.IntegerField(name='inv_dias_existencia',null = True)
    pot_dias_existencia = models.IntegerField(name='inv_potencias_dias_existencia',null = True)
    cant_inicial = models.IntegerField(name='inv_inicial_cantidad',null = True)
    costo_inicial = models.FloatField(name='inv_inicial_costo',null = True)
    mes_cant_prom = models.IntegerField( name='inv_prom_mes_cantidad',null = True)
    mes_costo_prom = models.FloatField(name= 'inv_prom_mes_costo',null = True)
    cant_prom = models.FloatField(name= 'inv_prom_cantidad',null = True,max_length=53)
    costo_prom = models.FloatField(name= 'inv_prom_costo',null = True)
    dias_existencia_semestre = models.IntegerField(name='inv_semestre_dias_existencia',null = True)
    uso_semestre= models.FloatField(name='inv_semestre_uso',null = True)
    cant_anno_anterior = models.FloatField(name='inv_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='inv_anno_ant_costo',null = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'inv_linea_sucursal')
        ]

class Ajuste_Linea_Sucursal(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='ajuste_cantidad',max_length=53,null=True)
    costo = models.FloatField(name ='ajuste_costo',null=True)
    importe = models.FloatField(name ='ajuste_importe',null=True)
    cantidad_anno_ant = models.FloatField(name='ajuste_anno_ant_cantidad',max_length=53)
    costo_anno_ant = models.FloatField(name ='ajuste_anno_ant_costo',null=True)
    importe_anno_ant = models.FloatField(name ='ajuste_anno_ant_importe',null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'ajuste_linea_sucursal')
        ]

class Transferencia_Linea_Sucursal(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)
    
    #attributes
    cantidad = models.FloatField(name='transf_cantidad',max_length=53,null=True)
    costo = models.FloatField(name ='transf_costo',null=True)
    cantidad_anno_ant = models.FloatField(name='transf_anno_ant_cantidad',max_length=53)
    costo_anno_ant = models.FloatField(name ='transf_anno_ant_costo',null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'transf_linea_sucursal')
        ]


#Departamento_Establecimiento
class Ventas_Departamento_Establecimiento(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='venta_cantidad',null = True)
    costo = models.FloatField(name='venta_costo',null = True)
    importe = models.FloatField(name='venta_importe',null = True)
    cantidad_prom = models.FloatField(name='venta_prom_cantidad',null = True)
    costo_prom = models.FloatField(name='venta_prom_costo',null = True)
    importe_prom = models.FloatField(name='venta_prom_importe',null = True)
    cant_semestre = models.FloatField(name='venta_semestre_cantidad',null = True)
    costo_semestre = models.FloatField(name='venta_semestre_costo',null = True)
    importe_semestre = models.FloatField(name='venta_semestre_importe',null = True)
    cant_anno_anterior = models.FloatField(name='venta_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='venta_anno_ant_costo',null = True)
    importe_anno_anterior = models.FloatField(name='venta_anno_ant_importe',null = True)
    importe_nacional = models.FloatField(name = 'venta_importe_nacional',null = True) 
    importe_nacional_anno_ant = models.FloatField(name = 'venta_anno_ant_importe_nacional',null = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'venta_dep_est')
        ]

class Compra_Departamento_Establecimiento(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='compra_cantidad',null = True)
    costo = models.FloatField(name='compra_costo',null = True) 
    cant_anno_anterior = models.FloatField(name='compra_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='compra_anno_ant_costo',null = True)
    costo_nacional= models.FloatField(name = 'compra_costo_nacional',null = True)
    costo_nacional_anno_ant = models.FloatField(name = 'compra_anno_ant_costo_nacional',null = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'compra_dep_est')
        ]

class Inventario_Departamento_Establecimiento(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='inv_cantidad',null = True)
    costo = models.FloatField(name='inv_costo',null = True)
    dias_existencia = models.IntegerField(name='inv_dias_existencia',null = True)
    pot_dias_existencia = models.IntegerField(name='inv_potencias_dias_existencia',null = True)
    cant_inicial = models.IntegerField(name='inv_inicial_cantidad',null = True)
    costo_inicial = models.FloatField(name='inv_inicial_costo',null = True)
    mes_cant_prom = models.IntegerField( name='inv_prom_mes_cantidad',null = True)
    mes_costo_prom = models.FloatField(name= 'inv_prom_mes_costo',null = True)
    cant_prom = models.FloatField(name= 'inv_prom_cantidad',null = True,max_length=53)
    costo_prom = models.FloatField(name= 'inv_prom_costo',null = True)
    dias_existencia_semestre = models.IntegerField(name='inv_semestre_dias_existencia',null = True)
    uso_semestre= models.FloatField(name='inv_semestre_uso',null = True)
    cant_anno_anterior = models.FloatField(name='inv_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='inv_anno_ant_costo',null = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'inv_dep_est')
        ]

class Ajuste_Departamento_Establecimiento(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='ajuste_cantidad',max_length=53,null=True)
    costo = models.FloatField(name ='ajuste_costo',null=True)
    importe = models.FloatField(name ='ajuste_importe',null=True)
    cantidad_anno_ant = models.FloatField(name='ajuste_anno_ant_cantidad',max_length=53)
    costo_anno_ant = models.FloatField(name ='ajuste_anno_ant_costo',null=True)
    importe_anno_ant = models.FloatField(name ='ajuste_anno_ant_importe',null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'ajuste_dep_est')
        ]

class Transferencia_Departamento_Establecimiento(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)
    
    #attributes
    cantidad = models.FloatField(name='transf_cantidad',max_length=53,null=True)
    costo = models.FloatField(name ='transf_costo',null=True)
    cantidad_anno_ant = models.FloatField(name='transf_anno_ant_cantidad',max_length=53)
    costo_anno_ant = models.FloatField(name ='transf_anno_ant_costo',null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'transf_dep_est')
        ]

#Departamento_Complejo
class Ventas_Departamento_Complejo(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='venta_cantidad',null = True)
    costo = models.FloatField(name='venta_costo',null = True)
    importe = models.FloatField(name='venta_importe',null = True)
    cantidad_prom = models.FloatField(name='venta_prom_cantidad',null = True)
    costo_prom = models.FloatField(name='venta_prom_costo',null = True)
    importe_prom = models.FloatField(name='venta_prom_importe',null = True)
    cant_semestre = models.FloatField(name='venta_semestre_cantidad',null = True)
    costo_semestre = models.FloatField(name='venta_semestre_costo',null = True)
    importe_semestre = models.FloatField(name='venta_semestre_importe',null = True)
    cant_anno_anterior = models.FloatField(name='venta_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='venta_anno_ant_costo',null = True)
    importe_anno_anterior = models.FloatField(name='venta_anno_ant_importe',null = True)
    importe_nacional =  models.FloatField(name = 'venta_importe_nacional',null = True) 
    importe_nacional_anno_ant = models.FloatField(name = 'venta_anno_ant_importe_nacional',null = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'venta_dep_complejo')
        ]

class Compra_Departamento_Complejo(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='compra_cantidad',null = True)
    costo = models.FloatField(name='compra_costo',null = True) 
    cant_anno_anterior = models.FloatField(name='compra_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='compra_anno_ant_costo',null = True)
    costo_nacional= models.FloatField(name = 'compra_costo_nacional',null = True)
    costo_nacional_anno_ant = models.FloatField(name = 'compra_anno_ant_costo_nacional',null = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'compra_dep_complejo')
        ]

class Inventario_Departamento_Complejo(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='inv_cantidad',null = True)
    costo = models.FloatField(name='inv_costo',null = True)
    dias_existencia = models.IntegerField(name='inv_dias_existencia',null = True)
    pot_dias_existencia = models.IntegerField(name='inv_potencias_dias_existencia',null = True)
    cant_inicial = models.IntegerField(name='inv_inicial_cantidad',null = True)
    costo_inicial = models.FloatField(name='inv_inicial_costo',null = True)
    mes_cant_prom = models.IntegerField( name='inv_prom_mes_cantidad',null = True)
    mes_costo_prom = models.FloatField(name= 'inv_prom_mes_costo',null = True)
    cant_prom = models.FloatField(name= 'inv_prom_cantidad',null = True,max_length=53)
    costo_prom = models.FloatField(name= 'inv_prom_costo',null = True)
    dias_existencia_semestre = models.IntegerField(name='inv_semestre_dias_existencia',null = True)
    uso_semestre= models.FloatField(name='inv_semestre_uso',null = True)
    cant_anno_anterior = models.FloatField(name='inv_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='inv_anno_ant_costo',null = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'inv_dep_complejo')
        ]

class Ajuste_Departamento_Complejo(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='ajuste_cantidad',max_length=53,null=True)
    costo =   models.FloatField(name ='ajuste_costo',null=True)
    importe = models.FloatField(name ='ajuste_importe',null=True)
    cantidad_anno_ant = models.FloatField(name='ajuste_anno_ant_cantidad',max_length=53)
    costo_anno_ant =   models.FloatField(name ='ajuste_anno_ant_costo',null=True)
    importe_anno_ant = models.FloatField(name ='ajuste_anno_ant_importe',null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'ajuste_dep_complejo')
        ]

class Transferencia_Departamento_Complejo(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)
    
    #attributes
    cantidad = models.FloatField(name='transf_cantidad',max_length=53,null=True)
    costo = models.FloatField(name ='transf_costo',null=True)
    cantidad_anno_ant = models.FloatField(name='transf_anno_ant_cantidad',max_length=53)
    costo_anno_ant = models.FloatField(name ='transf_anno_ant_costo',null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'transf_dep_complejo')
        ]


#Departamento_Sucursal
class Ventas_Departamento_Sucursal(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='venta_cantidad',null = True)
    costo = models.FloatField(name='venta_costo',null = True)
    importe = models.FloatField(name='venta_importe',null = True)
    cantidad_prom = models.FloatField(name='venta_prom_cantidad',null = True)
    costo_prom = models.FloatField(name='venta_prom_costo',null = True)
    importe_prom = models.FloatField(name='venta_prom_importe',null = True)
    cant_semestre = models.FloatField(name='venta_semestre_cantidad',null = True)
    costo_semestre = models.FloatField(name='venta_semestre_costo',null = True)
    importe_semestre = models.FloatField(name='venta_semestre_importe',null = True)
    cant_anno_anterior = models.FloatField(name='venta_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='venta_anno_ant_costo',null = True)
    importe_anno_anterior = models.FloatField(name='venta_anno_ant_importe',null = True)
    importe_nacional = models.FloatField(name = 'venta_importe_nacional',null = True) 
    importe_nacional_anno_ant = models.FloatField(name = 'venta_anno_ant_importe_nacional',null = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'venta_dep_sucursal')
        ]

class Compra_Departamento_Sucursal(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='compra_cantidad',null = True)
    costo = models.FloatField(name='compra_costo',null = True) 
    cant_anno_anterior = models.FloatField(name='compra_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='compra_anno_ant_costo',null = True)
    costo_nacional= models.FloatField(name = 'compra_costo_nacional',null = True)
    costo_nacional_anno_ant = models.FloatField(name = 'compra_anno_ant_costo_nacional',null = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'compra_dep_sucursal')
        ]

class Inventario_Departamento_Sucursal(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='inv_cantidad',null = True)
    costo = models.FloatField(name='inv_costo',null = True)
    dias_existencia = models.IntegerField(name='inv_dias_existencia',null = True)
    pot_dias_existencia = models.IntegerField(name='inv_potencias_dias_existencia',null = True)
    cant_inicial = models.IntegerField(name='inv_inicial_cantidad',null = True)
    costo_inicial = models.FloatField(name='inv_inicial_costo',null = True)
    mes_cant_prom = models.IntegerField( name='inv_prom_mes_cantidad',null = True)
    mes_costo_prom = models.FloatField(name= 'inv_prom_mes_costo',null = True)
    cant_prom = models.FloatField(name= 'inv_prom_cantidad',null = True,max_length=53)
    costo_prom = models.FloatField(name= 'inv_prom_costo',null = True)
    dias_existencia_semestre = models.IntegerField(name='inv_semestre_dias_existencia',null = True)
    uso_semestre= models.FloatField(name='inv_semestre_uso',null = True)
    cant_anno_anterior = models.FloatField(name='inv_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='inv_anno_ant_costo',null = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'inv_dep_sucursal')
        ]

class Ajuste_Departamento_Sucursal(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='ajuste_cantidad',max_length=53,null=True)
    costo = models.FloatField(name ='ajuste_costo',null=True)
    importe = models.FloatField(name ='ajuste_importe',null=True)
    cantidad_anno_ant = models.FloatField(name='ajuste_anno_ant_cantidad',max_length=53)
    costo_anno_ant = models.FloatField(name ='ajuste_anno_ant_costo',null=True)
    importe_anno_ant = models.FloatField(name ='ajuste_anno_ant_importe',null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'ajuste_dep_sucursal')
        ]

class Transferencia_Departamento_Sucursal(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)
    
    #attributes
    cantidad = models.FloatField(name='transf_cantidad',max_length=53,null=True)
    costo = models.FloatField(name ='transf_costo',null=True)
    cantidad_anno_ant = models.FloatField(name='transf_anno_ant_cantidad',max_length=53)
    costo_anno_ant = models.FloatField(name ='transf_anno_ant_costo',null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'transf_dep_sucursal')
        ]


#Seccion_Establecimiento
class Ventas_Seccion_Establecimiento(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='venta_cantidad',null = True)
    costo = models.FloatField(name='venta_costo',null = True)
    importe = models.FloatField(name='venta_importe',null = True)
    cantidad_prom = models.FloatField(name='venta_prom_cantidad',null = True)
    costo_prom = models.FloatField(name='venta_prom_costo',null = True)
    importe_prom = models.FloatField(name='venta_prom_importe',null = True)
    cant_semestre = models.FloatField(name='venta_semestre_cantidad',null = True)
    costo_semestre = models.FloatField(name='venta_semestre_costo',null = True)
    importe_semestre = models.FloatField(name='venta_semestre_importe',null = True)
    cant_anno_anterior = models.FloatField(name='venta_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='venta_anno_ant_costo',null = True)
    importe_anno_anterior = models.FloatField(name='venta_anno_ant_importe',null = True)
    importe_nacional = models.FloatField(name = 'venta_importe_nacional',null = True) 
    importe_nacional_anno_ant = models.FloatField(name = 'venta_anno_ant_importe_nacional',null = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'venta_seccion_prod')
        ]

class Compra_Seccion_Establecimiento(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='compra_cantidad',null = True)
    costo = models.FloatField(name='compra_costo',null = True) 
    cant_anno_anterior = models.FloatField(name='compra_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='compra_anno_ant_costo',null = True)
    costo_nacional= models.FloatField(name = 'compra_costo_nacional',null = True)
    costo_nacional_anno_ant = models.FloatField(name = 'compra_anno_ant_costo_nacional',null = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'compra_seccion_prod')
        ]

class Inventario_Seccion_Establecimiento(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)


    #attributes
    cantidad = models.FloatField(name='inv_cantidad',null = True)
    costo = models.FloatField(name='inv_costo',null = True)
    dias_existencia = models.IntegerField(name='inv_dias_existencia',null = True)
    pot_dias_existencia = models.IntegerField(name='inv_potencias_dias_existencia',null = True)
    cant_inicial = models.IntegerField(name='inv_inicial_cantidad',null = True)
    costo_inicial = models.FloatField(name='inv_inicial_costo',null = True)
    mes_cant_prom = models.IntegerField( name='inv_prom_mes_cantidad',null = True)
    mes_costo_prom = models.FloatField(name= 'inv_prom_mes_costo',null = True)
    cant_prom = models.FloatField(name= 'inv_prom_cantidad',null = True,max_length=53)
    costo_prom = models.FloatField(name= 'inv_prom_costo',null = True)
    dias_existencia_semestre = models.IntegerField(name='inv_semestre_dias_existencia',null = True)
    uso_semestre= models.FloatField(name='inv_semestre_uso',null = True)
    cant_anno_anterior = models.FloatField(name='inv_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='inv_anno_ant_costo',null = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'inv_seccion_prod')
        ]

class Ajuste_Seccion_Establecimiento(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)


    #attributes
    cantidad = models.FloatField(name='ajuste_cantidad',max_length=53,null=True)
    costo = models.FloatField(name ='ajuste_costo',null=True)
    importe = models.FloatField(name ='ajuste_importe',null=True)
    cantidad_anno_ant = models.FloatField(name='ajuste_anno_ant_cantidad',max_length=53)
    costo_anno_ant = models.FloatField(name ='ajuste_anno_ant_costo',null=True)
    importe_anno_ant = models.FloatField(name ='ajuste_anno_ant_importe',null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'ajuste_seccion_prod')
        ]

class Transferencia_Seccion_Establecimiento(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)
    
    #attributes
    cantidad = models.FloatField(name='transf_cantidad',max_length=53,null=True)
    costo = models.FloatField(name ='transf_costo',null=True)
    cantidad_anno_ant = models.FloatField(name='transf_anno_ant_cantidad',max_length=53)
    costo_anno_ant = models.FloatField(name ='transf_anno_ant_costo',null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'transf_seccion_prod')
        ]


#Seccion_Complejo
class Ventas_Seccion_Complejo(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='venta_cantidad',null = True)
    costo = models.FloatField(name='venta_costo',null = True)
    importe = models.FloatField(name='venta_importe',null = True)
    cantidad_prom = models.FloatField(name='venta_prom_cantidad',null = True)
    costo_prom = models.FloatField(name='venta_prom_costo',null = True)
    importe_prom = models.FloatField(name='venta_prom_importe',null = True)
    cant_semestre = models.FloatField(name='venta_semestre_cantidad',null = True)
    costo_semestre = models.FloatField(name='venta_semestre_costo',null = True)
    importe_semestre = models.FloatField(name='venta_semestre_importe',null = True)
    cant_anno_anterior = models.FloatField(name='venta_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='venta_anno_ant_costo',null = True)
    importe_anno_anterior = models.FloatField(name='venta_anno_ant_importe',null = True)
    importe_nacional = models.FloatField(name = 'venta_importe_nacional',null = True) 
    importe_nacional_anno_ant = models.FloatField(name = 'venta_anno_ant_importe_nacional',null = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'venta_seccion_complejo')
        ]

class Compra_Seccion_Complejo(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='compra_cantidad',null = True)
    costo = models.FloatField(name='compra_costo',null = True) 
    cant_anno_anterior = models.FloatField(name='compra_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='compra_anno_ant_costo',null = True)
    costo_nacional= models.FloatField(name = 'compra_costo_nacional',null = True)
    costo_nacional_anno_ant = models.FloatField(name = 'compra_anno_ant_costo_nacional',null = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'compra_seccion_complejo')
        ]

class Inventario_Seccion_Complejo(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='inv_cantidad',null = True)
    costo = models.FloatField(name='inv_costo',null = True)
    dias_existencia = models.IntegerField(name='inv_dias_existencia',null = True)
    pot_dias_existencia = models.IntegerField(name='inv_potencias_dias_existencia',null = True)
    cant_inicial = models.IntegerField(name='inv_inicial_cantidad',null = True)
    costo_inicial = models.FloatField(name='inv_inicial_costo',null = True)
    mes_cant_prom = models.IntegerField( name='inv_prom_mes_cantidad',null = True)
    mes_costo_prom = models.FloatField(name= 'inv_prom_mes_costo',null = True)
    cant_prom = models.FloatField(name= 'inv_prom_cantidad',null = True,max_length=53)
    costo_prom = models.FloatField(name= 'inv_prom_costo',null = True)
    dias_existencia_semestre = models.IntegerField(name='inv_semestre_dias_existencia',null = True)
    uso_semestre= models.FloatField(name='inv_semestre_uso',null = True)
    cant_anno_anterior = models.FloatField(name='inv_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='inv_anno_ant_costo',null = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'inv_seccion_complejo')
        ]

class Ajuste_Seccion_Complejo(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='ajuste_cantidad',max_length=53,null=True)
    costo = models.FloatField(name ='ajuste_costo',null=True)
    importe = models.FloatField(name ='ajuste_importe',null=True)
    cantidad_anno_ant = models.FloatField(name='ajuste_anno_ant_cantidad',max_length=53)
    costo_anno_ant = models.FloatField(name ='ajuste_anno_ant_costo',null=True)
    importe_anno_ant = models.FloatField(name ='ajuste_anno_ant_importe',null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'ajuste_seccion_complejo')
        ]

class Transferencia_Seccion_Complejo(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)
    
    #attributes
    cantidad = models.FloatField(name='transf_cantidad',max_length=53,null=True)
    costo = models.FloatField(name ='transf_costo',null=True)
    cantidad_anno_ant = models.FloatField(name='transf_anno_ant_cantidad',max_length=53)
    costo_anno_ant = models.FloatField(name ='transf_anno_ant_costo',null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'transf_seccioncomplejo')
        ]


#Seccion_Sucursal
class Ventas_Seccion_Sucursal(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='venta_cantidad',null = True)
    costo = models.FloatField(name='venta_costo',null = True)
    importe = models.FloatField(name='venta_importe',null = True)
    cantidad_prom = models.FloatField(name='venta_prom_cantidad',null = True)
    costo_prom = models.FloatField(name='venta_prom_costo',null = True)
    importe_prom = models.FloatField(name='venta_prom_importe',null = True)
    cant_semestre = models.FloatField(name='venta_semestre_cantidad',null = True)
    costo_semestre = models.FloatField(name='venta_semestre_costo',null = True)
    importe_semestre = models.FloatField(name='venta_semestre_importe',null = True)
    cant_anno_anterior = models.FloatField(name='venta_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='venta_anno_ant_costo',null = True)
    importe_anno_anterior = models.FloatField(name='venta_anno_ant_importe',null = True)
    importe_nacional = models.FloatField(name = 'venta_importe_nacional',null = True) 
    importe_nacional_anno_ant = models.FloatField(name = 'venta_anno_ant_importe_nacional',null = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'venta_seccion_sucursal')
        ]

class Compra_Seccion_Sucursal(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='compra_cantidad',null = True)
    costo = models.FloatField(name='compra_costo',null = True) 
    cant_anno_anterior = models.FloatField(name='compra_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='compra_anno_ant_costo',null = True)
    costo_nacional= models.FloatField(name = 'compra_costo_nacional',null = True)
    costo_nacional_anno_ant = models.FloatField(name = 'compra_anno_ant_costo_nacional',null = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'compra_seccion_sucursal')
        ]

class Inventario_Seccion_Sucursal(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='inv_cantidad',null = True)
    costo = models.FloatField(name='inv_costo',null = True)
    dias_existencia = models.IntegerField(name='inv_dias_existencia',null = True)
    pot_dias_existencia = models.IntegerField(name='inv_potencias_dias_existencia',null = True)
    cant_inicial = models.IntegerField(name='inv_inicial_cantidad',null = True)
    costo_inicial = models.FloatField(name='inv_inicial_costo',null = True)
    mes_cant_prom = models.IntegerField( name='inv_prom_mes_cantidad',null = True)
    mes_costo_prom = models.FloatField(name= 'inv_prom_mes_costo',null = True)
    cant_prom = models.FloatField(name= 'inv_prom_cantidad',null = True,max_length=53)
    costo_prom = models.FloatField(name= 'inv_prom_costo',null = True)
    dias_existencia_semestre = models.IntegerField(name='inv_semestre_dias_existencia',null = True)
    uso_semestre= models.FloatField(name='inv_semestre_uso',null = True)
    cant_anno_anterior = models.FloatField(name='inv_anno_ant_cantidad',null = True)
    costo_anno_anterior = models.FloatField(name='inv_anno_ant_costo',null = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'inv_seccion_sucursal')
        ]

class Ajuste_Seccion_Sucursal(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)

    #attributes
    cantidad = models.FloatField(name='ajuste_cantidad',max_length=53,null=True)
    costo = models.FloatField(name ='ajuste_costo',null=True)
    importe = models.FloatField(name ='ajuste_importe',null=True)
    cantidad_anno_ant = models.FloatField(name='ajuste_anno_ant_cantidad',max_length=53)
    costo_anno_ant = models.FloatField(name ='ajuste_anno_ant_costo',null=True)
    importe_anno_ant = models.FloatField(name ='ajuste_anno_ant_importe',null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'ajuste_seccion_sucursal')
        ]

class Transferencia_Seccion_Sucursal(models.Model):
    #key
    
    fam_id = models.ForeignKey(N_Familia,name = 'familia',on_delete=models.CASCADE, default = '')
    est_id = models.ForeignKey(N_Establecimiento,name='est_id',on_delete=models.CASCADE)
    prov_id = models.ForeignKey(N_Proveedor,name = 'prov_id',on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(N_Periodo,name= 'periodo_id',on_delete=models.CASCADE)
    act_id = models.ForeignKey(N_Actividad, name = 'act_id',on_delete=models.CASCADE)
    area_tipo = models.ForeignKey(N_TipoArea, name='area_tipo',on_delete=models.CASCADE)
    tipo_cod_id = models.ForeignKey(N_TipoCodigo,name = "tipo_cod_id",on_delete=models.CASCADE)
    
    #attributes
    cantidad = models.FloatField(name='transf_cantidad',max_length=53,null=True)
    costo = models.FloatField(name ='transf_costo',null=True)
    cantidad_anno_ant = models.FloatField(name='transf_anno_ant_cantidad',max_length=53)
    costo_anno_ant = models.FloatField(name ='transf_anno_ant_costo',null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['familia','est_id','prov_id','periodo_id','act_id','area_tipo','tipo_cod_id'],name= 'transf_seccion_sucursal')
        ]


