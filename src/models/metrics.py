from humps import camelize
from sqlmodel import Field, SQLModel


class MetricsUnit(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    service_name: str = Field(index=True)
    path: str = Field(index=True)
    response_time_ms: int

    class Config:
        alias_generator = camelize
        allow_population_by_field_name = True
