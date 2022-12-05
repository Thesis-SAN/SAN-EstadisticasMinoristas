from .dictionaries import *

def get_table(kpi, detail, group):
    #obtengo el proceso(venta, compra,...)
    process_name = process[kpi]
    return 'estad_minoristas' + process_name + model_table[(kpi,detail,group)][1]
    
def get_model(proc, detail, group):
    #process_name = process[proc]
    #print('process name',process_name)
    return model_table[(proc,detail,group)][0]

#de momento solo establecimiento que es el q tiene nomenclador (n_nombre)
#en este metodo anadir en que nivel buscar si hay varias agrupaciones (ej. si agrup sucursal, complejo-> tabla )
def get_model_detail(detail):
    return nomenclator[detail]

def build_select(metric_list):
    dict_proc_metric = {}
    for metric in metric_list:
        p = process[metric]
        try:
            dict_proc_metric[p].append(metric)
        except:
            dict_proc_metric[p] = [metric]
    
    return dict_proc_metric

def get_id(total):
    return agrup_id[total]

def build_kwargs_filter(field, value):
    return {field:value}