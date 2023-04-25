from fastapi import APIRouter, Depends

from core.db import get_session
from models.metrics import MetricsUnit
from schemas.aggregated_metrics import AggregatedMetricsByPath
from services.metrics import (
    create_metrics_unit,
    get_metrics_aggregation_by_service_name,
)

router = APIRouter()


@router.post("/", response_model=MetricsUnit)
async def create_metrics(metrics_unit: MetricsUnit, session=Depends(get_session)) -> MetricsUnit:
    return await create_metrics_unit(metrics_unit, session)


@router.get("/{service_name}/", response_model=list[AggregatedMetricsByPath])
async def get_metrics_aggregation(service_name: str, session=Depends(get_session)) -> list[AggregatedMetricsByPath]:
    return await get_metrics_aggregation_by_service_name(service_name, session)
