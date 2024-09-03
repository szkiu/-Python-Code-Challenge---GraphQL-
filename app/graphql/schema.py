from ariadne import QueryType, make_executable_schema, gql
from .resolvers import resolve_get_data

type_defs = gql(
    """
    type Query {
        getData: [Data]
    }

    type Data {
        column1: String
        column2: String
        # Agregar más campos según las columnas del CSV
    }
"""
)

query = QueryType()
query.set_field("getData", resolve_get_data)

schema = make_executable_schema(type_defs, query)
