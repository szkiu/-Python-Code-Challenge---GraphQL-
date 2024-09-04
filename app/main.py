from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from ariadne.asgi import GraphQL
from app.graphql.schema import schema
from app.services.auth import verify_token, auth_router
from fastapi.openapi.utils import get_openapi


graphql_app = GraphQL(schema, debug=True)

app = FastAPI()


@app.get("/graphql-info", tags=["GraphQL Info"])
async def graphql_info():
    return {
        "message": "This is a dummy endpoint to provide information about how to use the GraphQL endpoint.",
        "instructions": "To interact with the GraphQL API, use the /graphql endpoint with POST requests containing a valid GraphQL query.",
    }


app.include_router(auth_router)


@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    if request.url.path not in [
        "/docs",
        "/redoc",
        "/token",
        "/openapi.json",
        "/graphql-info",
    ]:
        try:
            token = request.headers.get("Authorization")
            if not token:
                raise HTTPException(status_code=401, detail="Missing token")
            await verify_token(token.split(" ")[1])
        except HTTPException as http_exc:
            return JSONResponse(
                status_code=http_exc.status_code, content={"message": http_exc.detail}
            )
        except Exception as e:
            return JSONResponse(status_code=400, content={"message": str(e)})

    response = await call_next(request)
    return response


app.mount("/graphql", graphql_app)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Python Code Challenge - GraphQL",
        version="1.0.0",
        description="Docs for the Python Code Challenge - GraphQL",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
