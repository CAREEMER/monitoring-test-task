from pydantic import BaseSettings


class Config(BaseSettings):
    HOST: str = "localhost"
    PORT: int = 8000
    ENV: str = "local"
    DATABASE_URL: str = "postgresql+asyncpg://sample_user:sample_user@localhost:5432/sample_user"

    @property
    def IS_LOCAL(self) -> bool:
        return self.ENV == "local"


app_config = Config()
