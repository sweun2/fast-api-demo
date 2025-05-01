from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_HOST: str = "localhost"
    MYSQL_PORT: int = 3306
    MYSQL_DB: str

    @property
    def db_url(self) -> str:
        return (
            f"mysql+pymysql://{self.MYSQL_USER}:"
            f"{self.MYSQL_PASSWORD}@"
            f"{self.MYSQL_HOST}:{self.MYSQL_PORT}/"
            f"{self.MYSQL_DB}"
        )

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",      # 정의되지 않은 env 변수들은 무시
    )

settings = Settings()
