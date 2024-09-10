from ariadne import QueryType, make_executable_schema, gql
from .resolvers import resolve_get_data

type_defs = gql(
    """
    type Query {
        getData: [Data]
    }

    type Data {
        id_tie_fecha_valor: Int
        id_cli_cliente: Int
        id_ga_vista: Int
        id_ga_tipo_dispositivo: Int
        id_ga_fuente_medio: Int
        desc_ga_sku_producto: String
        desc_ga_categoria_producto: String
        fc_agregado_carrito_cant: Int
        fc_ingreso_producto_monto: Float
        fc_retirado_carrito_cant: Float
        fc_detalle_producto_cant: Int
        fc_producto_cant: Int
        desc_ga_nombre_producto: String
        fc_visualizaciones_pag_cant: String
        flag_pipol: Int
        SASASA: String
        id_ga_producto: Int
        desc_ga_nombre_producto_1: String
        desc_ga_sku_producto_1: String
        desc_ga_marca_producto: String
        desc_ga_cod_producto: Float
        desc_categoria_producto: String
        desc_categoria_prod_principal: String
    }
"""
)

query = QueryType()
query.set_field("getData", resolve_get_data)

schema = make_executable_schema(type_defs, query)
