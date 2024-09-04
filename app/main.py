from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from ariadne.asgi import GraphQL
from app.graphql.schema import schema
from app.services.auth import verify_token, auth_router

# Create an instance of the GraphQL app
graphql_app = GraphQL(schema, debug=True)

# Initialize FastAPI
app = FastAPI()

# Include any existing routers for authentication or other purposes
app.include_router(auth_router)


# Middleware to verify token only for /graphql route
@app.middleware("http")
async def graphql_auth_middleware(request: Request, call_next):
    if request.url.path == "/graphql":
        try:
            token = request.headers.get("Authorization")
            if not token:
                raise HTTPException(status_code=401, detail="Missing token")
            # Assuming 'verify_token' accepts a token string and raises HTTPException if invalid
            await verify_token(token.split(" ")[1])
        except HTTPException as http_exc:
            return JSONResponse(
                status_code=http_exc.status_code, content={"message": http_exc.detail}
            )
        except Exception as e:
            return JSONResponse(status_code=400, content={"message": str(e)})

    response = await call_next(request)
    return response


# Mount GraphQL ASGI app directly to handle HTTP and WebSocket
app.mount("/graphql", graphql_app)

# Run the application
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
