from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .models import *
from django.db.models import Max
from  .utils import *
from django.views.generic import ListView
from itertools import chain
from django.db.models import Sum, Subquery
from django.db import connection


# Create your views here.

def index(request):
    return render(request, 'index1.html')


def login(request):
    return render(request, 'login.html')

'''
def report(request):
    if request.method == "POST":
        #obtener lista checkbocks y ratios marcados
        nivel_detallado = request.POST.getlist("selected_nivel_detalle")[0]
        totales = request.POST.getlist("selected_totales")
        print(nivel_detallado)
        metricas = request.POST.getlist("selected_metricas")
        
        filtro_est = request.POST.getlist("selected_entidad_est")
        filtro_comp = request.POST.getlist("selected_entidad_comp")
        filtro_suc = request.POST.getlist("selected_entidad_suc")

        filtro_secc = request.POST.getlist("selected_fam_sec")
        filtro_lin = request.POST.getlist("selected_fam_lin")
        filtro_dep = request.POST.getlist("selected_fam_dep")
        

        #datos a mostrar del total
        modelo_total,datos_a_mostrar_total = get_model_detail(totales[0])
        
        #datos a mostrar del nivel detallado
        modelo_detalle,datos_a_mostrar_detalle = get_model_detail(totales[0])
        
        #obtener {proc ->> metricas}
        procesos_seleccionados = build_select(metricas)# diccionario proceso--> lista de metrica(ej. compra->[compra cant, compra_costo])
        
        modelos = []#[(modelo_detalle, modelo_agrup]
        for proc in procesos_seleccionados:
            modelo = 'estad_minoristas_' + proc + '_'+ nivel_detallado.lower() + '_' + totales[0].lower()
            modelos.append((proc,modelo))

        id_detalle = get_id(nivel_detallado)
        id_total = get_id(totales[0])
        
        query = build_init_query(id_detalle,id_total,procesos_seleccionados, modelos)
        print(query)

        q = my_custom_sql(query)
        print(q)

        #unir los qs de cada metrica
        context = {
            'app_path' : request.get_full_path(),

        }

        return TemplateResponse(request, 'table.html', context)

    else:
        pass

    #construir contexto pagina principal de reportes

    #general
    actividades = N_Actividad.objects.all()
    areas_minoristas = N_TipoArea.objects.all()
    tipos_codigos = N_TipoCodigo.objects.all()
    origen_productos = ['Desconocido','Nacional','Importado']

    #familia
    lineas = N_Familia.objects.exclude(lin_descripcion = None, lin_id_oltp = None).values('lin_id_oltp','lin_descripcion').distinct().order_by('lin_id_oltp')
    secciones = N_Familia.objects.exclude(sec_descripcion = None, sec_id_oltp = None).values('sec_id_oltp','sec_descripcion').distinct().order_by('sec_id_oltp')
    departamentos = N_Familia.objects.exclude(dep_descripcion = None, dep_id_oltp = None).values('dep_id_oltp','dep_descripcion').distinct().order_by('dep_id_oltp')
    
    #proveedor
    prov_desconocidos = N_Proveedor.objects.filter(prov_tipo_mup = '_Desconocido' ).values('prov_codigo_panamericano','prov_nombre')
    prov_nacional = N_Proveedor.objects.filter(prov_tipo_mup = 'Nacional' ).values('prov_codigo_panamericano','prov_nombre')
    prov_extranjero = N_Proveedor.objects.filter(prov_tipo_mup = 'Extranjero' ).values('prov_codigo_panamericano','prov_nombre')
    prov_distribuidora = N_Proveedor.objects.filter(prov_tipo_mup = 'Distribuidora' ).values('prov_codigo_panamericano','prov_nombre')
    
    #entidades 
    sucursales = N_Establecimiento.objects.exclude(suc_codigo = None).values('suc_codigo','suc_nombre').distinct().order_by('suc_codigo')
    establecimientos = N_Establecimiento.objects.values('est_id_ods','est_codigo','est_descripcion').distinct().order_by('est_id_ods')
    complejos = N_Establecimiento.objects.values('comp_codigo','comp_nombre').distinct().order_by('comp_codigo')

    context = {
        'app_path' : request.get_full_path(),
        'actividades' : actividades,
        'areas_minoristas' :areas_minoristas,
        'tipos_codigos' : tipos_codigos,
        'origen_productos' : origen_productos,
        'departamentos' : departamentos,
        'secciones' : secciones,
        'lineas' : lineas,
        'prov_desconocidos' : prov_desconocidos,
        'prov_nacional' : prov_nacional,
        'prov_extranjero' : prov_extranjero,
        'prov_distribuidora' : prov_distribuidora,
        'sucursales' : sucursales,
        'complejos' : complejos,
        'establecimientos' : establecimientos,
    } 
    return TemplateResponse(request, 'test1.html',context)

'''

def report(request):
    if request.method == "POST":
        #obtener lista checkbocks y ratios marcados
        nivel_detallado = request.POST.getlist("selected_nivel_detalle")[0]
        totales = request.POST.getlist("selected_totales")
        print(nivel_detallado)
        metricas = request.POST.getlist("selected_metricas")
        
        filtro_est = request.POST.getlist("selected_entidad_est")
        filtro_comp = request.POST.getlist("selected_entidad_comp")
        filtro_suc = request.POST.getlist("selected_entidad_suc")

        filtro_secc = request.POST.getlist("selected_fam_sec")
        filtro_lin = request.POST.getlist("selected_fam_lin")
        filtro_dep = request.POST.getlist("selected_fam_dep")
        

        #datos a mostrar del total
        #modelo_total,datos_a_mostrar_total = get_model_detail(totales[0])
        #query_datos_total = modelo_total.objects.values(*datos_a_mostrar_total).distinct()
        #print(query_datos_total)

        #datos a mostrar del nivel detallado
        #modelo_detalle,datos_a_mostrar_detalle = get_model_detail(nivel_detallado)
        #query_datos_detalle = modelo_detalle.objects.values(*datos_a_mostrar_detalle).distinct()
        #print(query_datos_detalle)
        
        #obtener {proc ->> metricas}
        procesos_seleccionados = build_select(metricas)# diccionario proceso--> lista de metrica(ej. compra->[compra cant, compra_costo])
        modelo_1 =  get_model(list(procesos_seleccionados.keys())[0],nivel_detallado,totales[0])

        modelos = []#[(modelo_detalle, modelo_agrup]
        for proc in procesos_seleccionados:
            modelo = 'estad_minoristas_' + proc + '_'+ nivel_detallado.lower() + '_' + totales[0].lower()
            modelos.append((proc,modelo))

        id_detalle = get_id(nivel_detallado)
        id_total = get_id(totales[0])
        
        #construir query
        query = build_init_query(id_detalle,id_total,procesos_seleccionados, modelos,nivel_detallado, totales[0])
        print(query)
        
        # raw_query = modelo_1.objects.raw(query) 
        # print(raw_query)
        q = fetchall_sql_query(query)
        print(q)

        #unir los qs de cada metrica
        context = {
            'app_path' : request.get_full_path(),
            'query' : q
        }

        return TemplateResponse(request, 'table.html', context)

    else:
        pass

    #construir contexto pagina principal de reportes

    #general
    actividades = N_Actividad.objects.all()
    areas_minoristas = N_TipoArea.objects.all()
    tipos_codigos = N_TipoCodigo.objects.all()
    origen_productos = ['Desconocido','Nacional','Importado']

    #familia
    lineas = N_Familia.objects.exclude(lin_descripcion = None, lin_id_oltp = None).values('lin_id_oltp','lin_descripcion').distinct().order_by('lin_id_oltp')
    secciones = N_Familia.objects.exclude(sec_descripcion = None, sec_id_oltp = None).values('sec_id_oltp','sec_descripcion').distinct().order_by('sec_id_oltp')
    departamentos = N_Familia.objects.exclude(dep_descripcion = None, dep_id_oltp = None).values('dep_id_oltp','dep_descripcion').distinct().order_by('dep_id_oltp')
    
    #proveedor
    prov_desconocidos = N_Proveedor.objects.filter(prov_tipo_mup = '_Desconocido' ).values('prov_codigo_panamericano','prov_nombre')
    prov_nacional = N_Proveedor.objects.filter(prov_tipo_mup = 'Nacional' ).values('prov_codigo_panamericano','prov_nombre')
    prov_extranjero = N_Proveedor.objects.filter(prov_tipo_mup = 'Extranjero' ).values('prov_codigo_panamericano','prov_nombre')
    prov_distribuidora = N_Proveedor.objects.filter(prov_tipo_mup = 'Distribuidora' ).values('prov_codigo_panamericano','prov_nombre')
    
    #entidades 
    sucursales = N_Establecimiento.objects.exclude(suc_codigo = None).values('suc_codigo','suc_nombre').distinct().order_by('suc_codigo')
    establecimientos = N_Establecimiento.objects.values('est_id_ods','est_codigo','est_descripcion').distinct().order_by('est_id_ods')
    complejos = N_Establecimiento.objects.values('comp_codigo','comp_nombre').distinct().order_by('comp_codigo')

    context = {
        'app_path' : request.get_full_path(),
        'actividades' : actividades,
        'areas_minoristas' :areas_minoristas,
        'tipos_codigos' : tipos_codigos,
        'origen_productos' : origen_productos,
        'departamentos' : departamentos,
        'secciones' : secciones,
        'lineas' : lineas,
        'prov_desconocidos' : prov_desconocidos,
        'prov_nacional' : prov_nacional,
        'prov_extranjero' : prov_extranjero,
        'prov_distribuidora' : prov_distribuidora,
        'sucursales' : sucursales,
        'complejos' : complejos,
        'establecimientos' : establecimientos,
    } 
    return TemplateResponse(request, 'test1.html',context)


def  test_table(request):
    if request.method == "POST":
        field_list_est = ["est_id",'codigo','descripcion','codigo_estructurado','suc_id','suc_codigo','suc_nombre','comp_id','comp_codigo','comp_nombre','es_interno' ,'padre_id','padre_codigo','padre_descripcion','nivel' ,'codigo_actividad','actividad' ,'codigo_clasif_id',"codigo_clasificacion" ,'clasificacion','inv_sist_inf_codigo' ,'sist_inv' ,'es_dependiente' ,'dpa' ,'cod_tipo_est_id' ,'tipo_est_cod','tipo_est' ,'mt_fecha_actualizacion' ,'path' ,'mt_activo' ,'sist_inv_id_ods','sist_inv_nombre']
        list_est = N_Establecimiento.objects.filter(est_id_ods__lte=24)
        total_establecimientos = N_Establecimiento.objects.count()
        prod_mayor_venta = Ventas_Producto_Establecimiento.objects.aggregate(Max('venta_cantidad'))
    
        context = {
            'field_list' : field_list_est,
            'est_table' : list_est,
            'total_est' : total_establecimientos,
            'prod_mas_vendido' : prod_mayor_venta['venta_cantidad__max'],
        }

    return render(request, 'table.html',context)
    




