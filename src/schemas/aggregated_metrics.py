from pydantic import BaseModel


class AggregatedMetricsByPath(BaseModel):
    path: str
    average: str
    min: str
    max: str
