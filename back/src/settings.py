from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    FOO: str  # プログラムで扱う環境変数を定義
    BAR: int

settings = Settings()

