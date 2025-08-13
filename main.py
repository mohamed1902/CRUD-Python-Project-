#Main
from fastapi import FastAPI
from routes import routeUser , routeTeatcher 

app = FastAPI()


@app.get("/", tags=["Messeage"])
def messeage():
    return{"Messeage": "Welcome Users"}


app.include_router(routeUser.router , prefix="/users")
app.include_router(routeTeatcher.router , prefix="/teatchers")