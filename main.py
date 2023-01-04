from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routers.api import router as api_marvel

app = FastAPI()
app.include_router(api_marvel)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"status": "Pagina inicial"}
