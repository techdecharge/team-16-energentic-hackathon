from app import app
from app.api.actions import router as action_router
from app.api.battery_sim import router as battery_sim_router

app.include_router(action_router)
app.include_router(battery_sim_router)