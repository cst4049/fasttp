from app import create_app
from settings import app_settings


app = create_app()


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host=app_settings.host, port=app_settings.port,
                reload=True)
