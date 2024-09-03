from fastapi import FastAPI, Depends, APIRouter, HTTPException, status
from ariadne.asgi import GraphQL
from .graphql.schema import schema
from .services.auth import auth_router, verify_token

app = FastAPI()
graphql_router = APIRouter()

graphql_app = GraphQL(schema)


@graphql_router.get("/graphql", dependencies=[Depends(verify_token)])
@graphql_router.post("/graphql", dependencies=[Depends(verify_token)])
async def graphql_server(request: object):
    return await graphql_app.handle(request)


app.include_router(graphql_router)
app.include_router(auth_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
