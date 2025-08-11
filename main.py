#Main
from fastapi import FastAPI
from models.modelUser import Base
from models.modelTeatcher import Base
from pgAdmin.Connection import engine
from routes import routeUser , routeTeatcher 

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/", tags=["Messeage"])
def messeage():
    return{"Messeage": "Welcome"}


app.include_router(routeUser.router , prefix="/users")
app.include_router(routeTeatcher.router , prefix="/teatchers")