from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .models import *
from django.db.models import Max
from  .utils import *
from django.views.generic import ListView

# Create your views here.

def index(request):
    return render(request, 'index1.html')


def login(request):
    return render(request, 'login.html')

def report(request):
    if request.method == "POST":
        nivel_detallado = request.POST.getlist("selected_nivel_detalle")
        totales = request.POST.getlist("selected_ruptura")
        metricas = request.POST.getlist("selected_indicadores")
        print('nivel de detalle', nivel_detallado)
        procesos_seleccionadas = build_select(metricas)# diccionario proceso--> lista de metrica(ej. compra->[compra cant, compra_costo])
        models = []
        queries = []
        print(procesos_seleccionadas)

        for proc in procesos_seleccionadas:
            m =  procesos_seleccionadas[proc]
            model = get_model(proc, nivel_detallado[0],totales[0])#totales[0] de momento, solo voy a seleccionar una agrupacion y una metrica
            objects =  model.objects.filter(id__lte=10).values_list(*m)
            print(proc ,objects)
            queries.extend(objects)
        
        print("tabla de query",queries)

        context = {
            'app_path' : request.get_full_path(),
            'selected_checkboxes_nivel_detalle' : nivel_detallado,
            'selected_checkboxes_ruptura' : totales,
            'metricas' : metricas,
            'table' : queries,
            'detalle' : nivel_detallado[0],

        }

        return TemplateResponse(request, 'table.html', context)

    else:
        pass
    
    context = {
        'app_path' : request.get_full_path()
    }
    return TemplateResponse(request, 'test1.html')


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
    



