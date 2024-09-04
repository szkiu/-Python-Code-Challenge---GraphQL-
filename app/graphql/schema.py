from ariadne import QueryType, make_executable_schema, gql
from .resolvers import resolve_get_data

type_defs = gql(
    """
    type Query {
        getData: [Data]
    }

    type Data {
        desc_ga_sku_producto: String
        desc_ga_marca_producto: String
    }
"""
)

query = QueryType()
query.set_field("getData", resolve_get_data)

schema = make_executable_schema(type_defs, query)
