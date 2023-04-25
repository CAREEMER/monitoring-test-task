from sqlmodel import func, select
from sqlmodel.ext.asyncio.session import AsyncSession

from models.metrics import MetricsUnit
from schemas.aggregated_metrics import AggregatedMetricsByPath


async def create_metrics_unit(metrics: MetricsUnit, session: AsyncSession) -> MetricsUnit:
    session.add(metrics)
    await session.commit()
    await session.refresh(metrics)

    return metrics


async def get_metrics_aggregation_by_service_name(
    service_name: str, session: AsyncSession
) -> list[AggregatedMetricsByPath]:
    query = (
        select(
            MetricsUnit.path,
            func.min(MetricsUnit.response_time_ms),
            func.max(MetricsUnit.response_time_ms),
            func.avg(MetricsUnit.response_time_ms),
        )
        .where(MetricsUnit.service_name == service_name)
        .group_by(MetricsUnit.path)
    )

    result = (await session.execute(query)).all()
    return [AggregatedMetricsByPath(path=el.path, average=el.avg, max=el.max, min=el.min) for el in result]
