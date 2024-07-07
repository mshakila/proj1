import os
from pathlib import Path

pack_name = "PricePred"

list_of_files = [
    "github/workflows/.gitkeep",
    f"src/{pack_name}/__init__.py",
    f"src/{pack_name}/components/__init__.py",
    f"src/{pack_name}/components/data_ingestion.py" ,
    f"src/{pack_name}/components/data_transformation.py" ,
    f"src/{pack_name}/components/model_trainer.py" ,
    f"src/{pack_name}/pipelines/__init__.py" ,
    f"src/{pack_name}/pipelines/training_pipeline.py" , 
    f"src/{pack_name}/pipelines/prediction_pipeline.py" ,
    f"src/{pack_name}/logger.py" ,
    f"src/{pack_name}/exception.py" ,
    f"src/{pack_name}/utils/__init__.py" ,
    "notebooks/research.ipynb",
    "notebooks/data/.gitkeep" ,
    "requirements.txt" ,
    "setup.py" ,
    "init_setup.sh"
    
]

    # create dir

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir , filename = os.path.split(filepath)

    if filedir != "" :
        os.makedirs(filedir , exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)== 0):
        with open(filepath , "w") as f:
            pass
    else:
        print("file already exists")
        

    