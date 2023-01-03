from fastapi import FastAPI

from routers.api import router as api_marvel

app = FastAPI()
app.include_router(api_marvel)


@app.get("/")
async def main():
    return {"status": "Pagina inicial"}
