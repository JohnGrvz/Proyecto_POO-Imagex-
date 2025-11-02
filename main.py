from dotenv import load_dotenv
import os
from app.api.Api_manager import ApiManager
from app.Interfaz_grafica.interfaz import InterfazEditor

load_dotenv()
api_key = os.getenv("API_KEY")

Api_manager = ApiManager(api_key=api_key)

if __name__ == "__main__":
    InterfazEditor(api_manager=Api_manager)

