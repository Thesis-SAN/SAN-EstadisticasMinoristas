from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .models import *
from django.db.models import Max

# Create your views here.

def index(request):
    return render(request, 'index1.html')


def login(request):
    return render(request, 'login.html')

def test(request):
    if request.method == "POST":
        selected_list_nivel_detalle = request.POST.getlist("selected_nivel_detalle")
        selected_list_ruptura= request.POST.getlist("selected_ruptura")
        selected_list_metricas = request.POST.getlist("selected_metricas")
        selected_list_indicadores = request.POST.getlist("selected_indicadores")
        context ={
            'app_path' : request.get_full_path(),
            'selected_checkboxes_nivel_detalle' : selected_list_nivel_detalle,
            'selected_checkboxes_ruptura' : selected_list_ruptura,
            'selected_checkboxes_indicadores' : selected_list_indicadores,
            'selected_checkboxes_metricas' : selected_list_metricas,
        }
        return TemplateResponse(request, 'test1.html', context)

    else:
        pass
    
    context = {
        'app_path' : request.get_full_path()
    }
    return TemplateResponse(request, 'test1.html')


def  test_table(request):
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

    