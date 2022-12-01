from .dictionaries import *

def get_table(kpi, detail, group):
    #obtengo el proceso(venta, compra,...)
    process_name = process[kpi]
    return 'estad_minoristas' + process_name + model_table[(kpi,detail,group)][1]
    
def get_model(proc, detail, group):
    #process_name = process[proc]
    #print('process name',process_name)
    return model_table[(proc,detail,group)][0]

def build_select(metric_list):
    dict_proc_metric = {}
    for metric in metric_list:
        p = process[metric]
        try:
            dict_proc_metric[p].append(metric)
        except:
            dict_proc_metric[p] = [metric]
    
    return dict_proc_metric
