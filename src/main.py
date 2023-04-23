from fastapi import FastAPI
from .user.router import router as user_route
from .company.router import router as company_route
from .task.router import router as task_route
from .authent.router import router as auth_route
app = FastAPI()

app.include_router(user_route)
app.include_router(company_route)
app.include_router(task_route)
app.include_router(auth_route)