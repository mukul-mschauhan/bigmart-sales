import os
from pathlib import Path # to autodetect the path of files

project_name = "bigmart_sales"

list_of_files = [
    f"{project_name}/__init__.py" # Constructor File
    f"{project_name}/components/__init__.py"
    f"{project_name}/components/data_ingestion.py"
    f"{project_name}/components/data_validation.py"
    f"{project_name}/components/data_transformation.py"
    f"{project_name}/components/model_trainer.py"
    f"{project_name}/components/model_evaluation.py"
    f"{project_name}/components/model_pusher.py"
    
]
