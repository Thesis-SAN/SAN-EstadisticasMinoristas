from .dictionaries import *
from django.db import connection

def get_modelo_detalle_total(d_or_t):
    return agrup[d_or_t]

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


def build_select_q(id_detalle,id_total,proc,campos_a_mostrar,indicadores):
    calculo_ind = ''
    for ind in indicadores:
       calculo_ind+= calculo_indicadores[ind]
    return "SELECT " + campos_a_mostrar  + calculo_ind +'\n'

def build_sum(dict_proc_metricas):
    result = ''
    for proc in dict_proc_metricas:
        list_m = dict_proc_metricas[proc]
        for m in list_m:
            s = proc[0] + '.' + m
            result += ' SUM('+ s + ') as '+ m +',' 
        ##############'SUM(v.venta_cantidad)
    result = result[0:len(result)-1] + '\n'
    return result


def build_from(proc, modelo_from):
    return 'FROM '+ modelo_from + ' as ' + proc[0]+ '\n'

def build_inner_join(modelos, id_detalle):#modelos[1:], el primer modelo va en el FROM
    result = ''
    proc_inicial = modelos[0][0]
    for modelo in modelos[1:]:
        proc = modelo[0]
        result += 'INNER JOIN  ' + modelo[1] +' as ' + proc[0] +'\n'
        result+= 'ON ' + proc[0] + '.' + id_detalle + '=' +  proc_inicial[0] + '.' + id_detalle + '\n'
    return result

def build_inner_join_nomenclator(nivel_detallado,total,alias_modelo_inicial,id_detalle_modelo_inicial):
    print(alias_modelo_inicial)
    result =''
    #Nivel detallado, total
    modelos_det_tot = []
    nombre_det, id_det = get_modelo_detalle_total(nivel_detallado)
    nombre_total, id_total = get_modelo_detalle_total(total)
    ids = [id_det,id_total]

    modelos_det_tot.append('estad_minoristas_n_' + nombre_det )
    modelos_det_tot.append('estad_minoristas_n_' + nombre_total)
    _,_,alias_det = get_model_detail(nivel_detallado)
    _,_,alias_total = get_model_detail(total)

    alias = [alias_det,alias_total]

    for i,modelo in enumerate(modelos_det_tot):
        result+= 'INNER JOIN  ' + modelo + ' as ' + alias[i] + '\n'
        result+= 'ON ' +  alias_modelo_inicial + '.' + id_detalle_modelo_inicial[i] + '=' + alias[i] + '.' + ids[i] + '\n'

    print('inner join 2', result)
    return result

def build_group_by(id_detalle, id_total,proc,campos_a_mostrar):

    return 'GROUP BY ' + campos_a_mostrar + proc[0] + '.' + id_detalle + ', ' + proc[0] + '.' + id_total 

def build_fields_to_show(nivel_detalle,total):
    _,campos_a_mostrar_detalle,alias_det =get_model_detail (nivel_detalle)
    _,campos_a_mostrar_total,alias_total =get_model_detail (total)
    result = ''
    for campo in campos_a_mostrar_detalle:
        result+= alias_det + '.'+ campo + ', '
    for campo in campos_a_mostrar_total:
        result+= alias_total + '.'+ campo + ', '
    return result

def build_where(indicadores):
    result = ''
    if 'margen' in indicadores:
        result+= ' WHERE v.venta_costo != 0 \n'
    return result

def build_order_by():
    return ' ORDER BY p.prod_recno DESC \n'
    
def build_init_query(id_detalle,id_total, procesos_seleccionados,modelos,nivel_detallado,total,indicadores):
    id_detalle = id_detalle +'_id' 
    id_total = id_total +'_id' 
    campos_a_mostrar = build_fields_to_show(nivel_detallado,total)

    select = build_select_q(id_detalle,id_total,modelos[0][0],campos_a_mostrar,indicadores)
    sum = build_sum(procesos_seleccionados)
    from_ = build_from(modelos[0][0],modelos[0][1])
    inner_join = build_inner_join(modelos,id_detalle)
    inner_join_nom = build_inner_join_nomenclator(nivel_detallado,total,modelos[0][0][0],[id_detalle,id_total])
    group_by = build_group_by(id_detalle,id_total,modelos[0][0],campos_a_mostrar)
    where = build_where(indicadores)
    order_by = build_order_by()
    return select + sum + from_ + inner_join + inner_join_nom+ where  + group_by + order_by + '\nLIMIT 100'

def build_head_query():
    pass

#connection
def my_custom_sql(query_sql):
    with connection.cursor() as cursor:
        cursor.execute(query_sql)
        row = cursor.fetchone()
    return row

def fetchall_sql_query(query_sql):
    with connection.cursor() as cursor:
        cursor.execute(query_sql)
        q = cursor.fetchall()
        cursor.close()
    return q

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [ dict(zip(columns, row))  for row in cursor.fetchall() ]


def build_header(nivel_detallado,total,metricas, indicadores):
    header = []

