from fastapi import APIRouter

from .metrics import router as metrics_router

api_router = APIRouter()
api_router.include_router(metrics_router, prefix="/metrics")
