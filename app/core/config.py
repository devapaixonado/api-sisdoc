from dotenv import dotenv_values

ENV = dotenv_values('.env')

class Settings:
    def __init__(self):
        self.POSTGRES_USER = ENV.get("POSTGRES_USER")
        self.POSTGRES_PASSWORD = ENV.get("POSTGRES_PASSWORD")
        self.POSTGRES_HOST = ENV.get("POSTGRES_HOST", "localhost")
        self.POSTGRES_PORT = ENV.get("POSTGRES_PORT", "5432")
        self.POSTGRES_DB = ENV.get("POSTGRES_DB")
        
    @property
    def DATABASE_URL(self):
        return (
            f"postgresql+psycopg2://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

settings = Settings()
