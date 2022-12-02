from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .models import *
from django.db.models import Max
from  .utils import *
from django.views.generic import ListView
from itertools import chain


# Create your views here.

def index(request):
    return render(request, 'index1.html')


def login(request):
    return render(request, 'login.html')

def report(request):
    print("entre enla vista")
    if request.method == "POST":
        #obtener lista checkbocks y ratios marcados
        nivel_detallado = request.POST.getlist("selected_nivel_detalle")
        totales = request.POST.getlist("selected_totales")
        metricas = request.POST.getlist("selected_metricas")
        
        #obtener {proc ->> metricas}
        procesos_seleccionadas = build_select(metricas)# diccionario proceso--> lista de metrica(ej. compra->[compra cant, compra_costo])
        
        queries = []# lista de [listas de (tuplas)]

        # construir las queries 
        for proc in procesos_seleccionadas:
            #obtener metricas
            m =  procesos_seleccionadas[proc]
            
            #obtener modelo donde se va a hacer la query
            model = get_model(proc, nivel_detallado[0],totales[0])#totales[0] de momento, solo voy a seleccionar una agrupacion y una metrica

            #query
            #falta comprobar filtros(periodo, tipo de area, origen de producto, tipo de codigo)
            objects =  model.objects.filter(id__lte=4075236,id__gte= 4075226).values_list(*m)
            queries.append(objects)

            print(proc ,objects)
            #queries = list(chain(queries,objects))
        
        #construir la tabla a imprimir con todos los procesos
        q = []
        for i in range(0,len(queries[0])):
            q.append(list(chain(*[o[i] for o in queries])))
        
        
        print("tabla de query",queries)
        print("query lista para imprimir",q)

        context = {
            'app_path' : request.get_full_path(),
            'metricas' : metricas,
            'table' : q,
            'detalle' : nivel_detallado[0],

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
    #departamentos = N_Familia.objects.values('dep_id_oltp','dep_descripcion').distinct()
    #secciones = N_Familia.objects.values('sec_id_oltp','sec_descripcion').distinct()
    #lineas = N_Familia.objects.values('lin_id_oltp','lin_descripcion').distinct()
    lineas = N_Familia.objects.exclude(lin_descripcion = None, lin_id_oltp = None).values('lin_id_oltp','lin_descripcion').distinct()
    secciones = N_Familia.objects.exclude(sec_descripcion = None, sec_id_oltp = None).values('sec_id_oltp','sec_descripcion').distinct()
    departamentos = N_Familia.objects.exclude(dep_descripcion = None, dep_id_oltp = None).values('dep_id_oltp','dep_descripcion').distinct()
    
    #proveedor
    prov_desconocidos = N_Proveedor.objects.filter(prov_tipo_mup = '_Desconocido' ).values('prov_codigo_panamericano','prov_nombre')
    prov_nacional = N_Proveedor.objects.filter(prov_tipo_mup = 'Nacional' ).values('prov_codigo_panamericano','prov_nombre')
    prov_extranjero = N_Proveedor.objects.filter(prov_tipo_mup = 'Extranjero' ).values('prov_codigo_panamericano','prov_nombre')
    prov_distribuidora = N_Proveedor.objects.filter(prov_tipo_mup = 'Distribuidora' ).values('prov_codigo_panamericano','prov_nombre')


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
    

class ListReport(ListView):
    pass
    



