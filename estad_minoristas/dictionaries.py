from .models import *
process = {
        'venta_cantidad' : 'ventas',
        'venta_costo' : 'ventas',
        'venta_importe' : 'ventas',
        'compra_cantidad' : 'compra',
        'compra_costo' : 'compra',
        'inventario_cantidad' : 'inventario',
        'inventario_costo' : 'inventario',
        
    }
model_table = {
    ('ventas','Producto','Establecimiento'): (Ventas_Producto_Establecimiento,'ventas_producto_establecimiento'),
    ('ventas','Linea','Establecimiento'): (Ventas_Linea_Establecimiento,'ventas_linea_establecimiento'),
    ('ventas','Seccion','Establecimiento'): (Ventas_Seccion_Establecimiento,'ventas_seccion_establecimiento'),
    ('ventas','Departamento','Establecimiento'): (Ventas_Departamento_Establecimiento,'ventas_departamento_establecimiento'),
    ('compra','Producto','Establecimiento'): (Compra_Producto_Establecimiento,'compra_producto_establecimiento'),
    ('compra','Linea','Establecimiento'): (Compra_Linea_Establecimiento,'compra_linea_establecimiento'),
    ('compra','Seccion','Establecimiento'): (Compra_Seccion_Establecimiento,'compra_seccion_establecimiento'),
    ('compra','Departamento','Establecimiento'): (Compra_Departamento_Establecimiento,'compra_departamento_establecimiento'),
    ('inventario','Producto','Establecimiento'): (Inventario_Producto_Establecimiento,'inventario_producto_establecimiento'),
    ('inventario','Linea','Establecimiento'): (Inventario_Linea_Establecimiento,'inventario_linea_establecimiento'),
    ('inventario','Seccion','Establecimiento'): (Inventario_Seccion_Establecimiento,'inventario_seccion_establecimiento'),
    ('inventario','Departamento','Establecimiento'): (Inventario_Departamento_Establecimiento,'inventario_departamento_establecimiento'),

    ('ventas','Producto','Complejo'): (Ventas_Producto_Complejo,'ventas_producto_complejo'),
    ('ventas','Linea','Complejo'): (Ventas_Linea_Complejo,'ventas_linea_complejo'),
    ('ventas','Seccion','Complejo'): (Ventas_Seccion_Complejo,'ventas_seccion_complejo'),
    ('ventas','Departamento','Complejo'): (Ventas_Departamento_Complejo,'ventas_departamento_complejo'),
    ('compra','Producto','Complejo'): (Compra_Producto_Complejo,'compra_producto_complejo'),
    ('compra','Linea','Complejo'): (Compra_Linea_Complejo,'compra_linea_complejo'),
    ('compra','Seccion','Complejo'): (Compra_Seccion_Complejo,'compra_seccion_complejo'),
    ('compra','Departamento','Complejo'): (Compra_Departamento_Complejo,'compra_departamento_complejo'),
    ('inventario','Producto','Complejo'): (Inventario_Producto_Complejo,'inventario_producto_complejo'),
    ('inventario','Linea','Complejo'): (Inventario_Linea_Complejo,'inventario_linea_complejo'),
    ('inventario','Seccion','Complejo'): (Inventario_Seccion_Complejo,'inventario_seccion_complejo'),
    ('inventario','Departamento','Complejo'): (Inventario_Departamento_Complejo,'inventario_departamento_complejo'),
    
    ('ventas','Producto','Sucursal'): (Ventas_Producto_Sucursal,'ventas_producto_sucursal'),
    ('ventas','Linea','Sucursal'): (Ventas_Linea_Sucursal,'ventas_linea_sucursal'),
    ('ventas','Seccion','Sucursal'): (Ventas_Seccion_Sucursal,'ventas_seccion_sucursal'),
    ('ventas','Departamento','Sucursal'): (Ventas_Departamento_Sucursal,'ventas_departamento_sucursal'),
    ('compra','Producto','Sucursal'): (Compra_Producto_Sucursal,'compra_producto_sucursal'),
    ('compra','Linea','Sucursal'): (Compra_Linea_Sucursal,'compra_linea_sucursal'),
    ('compra','Seccion','Sucursal'): (Compra_Seccion_Sucursal,'compra_seccion_sucursal'),
    ('compra','Departamento','Sucursal'): (Compra_Departamento_Sucursal,'compra_departamento_sucursal'),
    ('inventario','Producto','Sucursal'): (Inventario_Producto_Sucursal,'inventario_producto_sucursal'),
    ('inventario','Linea','Sucursal'): (Inventario_Linea_Sucursal,'inventario_linea_sucursal'),
    ('inventario','Seccion','Sucursal'): (Inventario_Seccion_Sucursal,'inventario_seccion_sucursal'),
    ('inventario','Departamento','Sucursal'): (Inventario_Departamento_Sucursal,'inventario_departamento_sucursal'),
    


}

nomenclator = {
    'Establecimiento' : N_Establecimiento,
    'Producto': N_Producto,
    
}