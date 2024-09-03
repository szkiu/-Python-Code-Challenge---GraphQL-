from fastapi import FastAPI
from ariadne.asgi import GraphQL
from .graphql.schema import schema
from .services.auth import auth_router
import uvicorn

app = FastAPI()

# Mount GraphQL
graphql_app = GraphQL(schema)
app.mount("/graphql", graphql_app)

# Include auth router
app.include_router(auth_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
