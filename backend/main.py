from app import create_app
from utils.logger import logger

app = create_app()
logger.info("Aplicación Flask iniciada")


if __name__ == "__main__":
    app.run(debug=True)


