# Python Coding Challenge - GraphQL API

## Descripción

Este proyecto implementa una API utilizando FastAPI con un endpoint GraphQL, documentación Swagger y un servicio opcional de autenticación utilizando OAuth2. La API lee datos de un archivo CSV y los expone a través de GraphQL.

## Características

- **Data Service**: Proporciona acceso a los datos del archivo CSV utilizando un endpoint GraphQL.
- **Auth Service**: Implementa el flujo de credenciales de cliente OAuth2 y devuelve un token JWT. Los endpoints de Data Service requieren un JWT válido para acceder.

## Requisitos

- Docker
- Docker Compose (opcional)

## Instalación

### Clonar el Repositorio

```bash
git clone <repo-url>
cd graphql-api
```

### Construir la Imagen de Docker

```bash
docker build -t graphql-api .
```

### Ejecutar el Contenedor Docker

```bash
docker run -p 8080:8000 graphql-api
```

Esto expondrá la API en http://localhost:8080.

## Uso

### Acceso a la Documentación de la API

Puedes acceder a la documentación Swagger para interactuar con los endpoints en:

```bash
http://localhost:8080/docs
```

## Acceso al Playground de GraphQL

### Para acceder al endpoint de GraphQL y ejecutar consultas, utiliza:

```bash
http://localhost:8080/graphql
```

### Autenticación

#### Obtener un Token JWT:

Para obtener un token JWT, realiza una solicitud POST al endpoint /token con un client_id y client_secret válidos:

```bash
curl -X POST "http://localhost:8080/token"
-H "Content-Type: application/x-www-form-urlencoded"
-d "client_id=test_client_id&client_secret=test_client_secret"
```

#### Usar el Token JWT:

Utiliza el token JWT recibido para acceder a los endpoints protegidos de la API, como el endpoint de GraphQL.

Ejemplo de uso con curl:

```bash
curl -L -X POST http://localhost:8080/graphql
-H "Content-Type: application/json"
-H "Authorization: Bearer <your-bearer-token>"
-d '{"query": "{ getData { desc_ga_sku_producto, desc_ga_marca_producto } }"}'
```

Reemplaza <your_token> con el token JWT obtenido del paso anterior.

## Dependencias

El proyecto utiliza las siguientes dependencias:

- `fastapi==0.78.0`
- `uvicorn==0.22.0`
- `ariadne==0.16.0`
- `pandas==1.5.3`
- `PyJWT==2.8.0`
- `numpy==1.23.5`
- `python-multipart==0.0.9`

Asegúrate de que estas dependencias estén correctamente instaladas en el contenedor Docker.

## Notas Adicionales

- Asegúrate de que Docker esté instalado y en funcionamiento en tu máquina antes de ejecutar los comandos.
- Puedes modificar el esquema de GraphQL y los resolvers según tus necesidades.
- Asegúrate de que el archivo CSV esté ubicado en el directorio correcto o que la ruta esté configurada adecuadamente en el código.
