from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .models import *
from django.db.models import Max
from  .utils import *
from django.views.generic import ListView
from itertools import chain
from django.db.models import Sum, Subquery

# Create your views here.

def index(request):
    return render(request, 'index1.html')


def login(request):
    return render(request, 'login.html')

def report(request):
    if request.method == "POST":
        #obtener lista checkbocks y ratios marcados
        nivel_detallado = request.POST.getlist("selected_nivel_detalle")[0]
        totales = request.POST.getlist("selected_totales")
        metricas = request.POST.getlist("selected_metricas")
        
        filtro_est = request.POST.getlist("selected_entidad_est")
        filtro_comp = request.POST.getlist("selected_entidad_comp")
        filtro_suc = request.POST.getlist("selected_entidad_suc")

        filtro_secc = request.POST.getlist("selected_fam_sec")
        filtro_lin = request.POST.getlist("selected_fam_lin")
        filtro_dep = request.POST.getlist("selected_fam_dep")
        
        #de momento solo un total seleccionado=> len(agrupac)=1
        #construir el QS con los datos a mostrar de las agrupacione
        modelo,datos_a_mostrar = get_model_detail(totales[0])
        qs_datos_total = modelo.objects.values_list(*datos_a_mostrar)
    
        
        #construir el query set con los datos a mostrar del nivel detallado

        #obtener {proc ->> metricas}
        procesos_seleccionados = build_select(metricas)# diccionario proceso--> lista de metrica(ej. compra->[compra cant, compra_costo])

        primer_proceso = list(procesos_seleccionados.keys())[0]
        q = None
        for met in procesos_seleccionados[primer_proceso]:
            modelo = get_model(primer_proceso,nivel_detallado,totales[0])
            id_agrup = get_id(totales[0])
            id_detalle = get_id(nivel_detallado)
            try:
                q = q.annotate(Sum(met))
            except:
                q = modelo.objects.values(id_detalle,id_agrup).annotate(Sum(met))
        print("primera parte",q)

        list_proc_selecc = list(procesos_seleccionados.keys())[1:]
        for proc in list_proc_selecc:
            m = procesos_seleccionados[proc]

            #obtener modelo al que se va a hacer la consulta
            modelo = get_model(proc,nivel_detallado,totales[0])

            for _,met in enumerate(m):
                q = q.annotate(alias = Subquery(modelo.objects.values(id_detalle,id_agrup).annotate(Sum(met)).values(met+"__sum")))

            #q = q.annotate(Subquery(modelo.objects.values(id_detalle,id_agrup).annotate(Sum(m))))

            #q = modelo.objects.values(id_detalle,id_agrup).annotate(Sum(m[0]))
            #for _,met in enumerate(m, start = 1):
            #    q = q.annotate(Sum(met))


        print('table', q[:10])
        '''
            id_agrup = get_id(totales[0])
            id_detalle = get_id(nivel_detallado)
            agrup =  q.values(id_agrup).annotate(Sum(m[0]))
            for _,met in enumerate(m, start = 1):
                agrup = agrup.annotate(Sum(met))
            
            print("Agrupacion",agrup[:10])

            agrup = agrup[:10]
            for a in agrup:
                a = a[id_agrup]
                print(a)
                kwargs = {id_agrup: a} #build_kwargs_filter(id_agrup,a)
                print(kwargs , id_detalle)
                r = q.filter(**kwargs).values(id_detalle)[:10]
                print(r)
            '''

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
    




