from fastapi import APIRouter, Depends

from core.db import get_session
from models.metrics import MetricsUnit
from schemas.aggregated_metrics import AggregatedMetricsByPath
from services.metrics import create_metrics_unit, get_metrics_by_service_name

router = APIRouter()


@router.post("/")
async def create_metrics(metrics_unit: MetricsUnit, session=Depends(get_session)):
    return await create_metrics_unit(metrics_unit, session)


@router.get("/{service_name}/", response_model=list[AggregatedMetricsByPath])
async def get_metrics(service_name: str, session=Depends(get_session)):
    return await get_metrics_by_service_name(service_name, session)
