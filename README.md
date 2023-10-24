# Kidney-Disease-Classification-MLFlow


## Workflows

1. Update config.yaml
2. Update secret.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml


...
# HOW TO RUN?
...
### STEPS:

Clone the repository

```bash
https://github.com/RG-Le/Kidney-Disease-Classification-MLFlow
```
...

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n cnncls python=3.8 -y
```

```bash
conda activate cnncls
```


### STEP 02- Install the requirements
```bash
pip install -r requirements.txt
```

#### MLFLOW 
###### cmd
- mlflow ui

### Dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/RG-Le/Kidney-Disease-Classification-MLFlow.mlflow \
MLFLOW_TRACKING_USERNAME=RG-Le \
MLFLOW_TRACKING_PASSWORD=c9385918b480d09da6663c4a7f67a55fdce010aa \
python script.py

Run this to export as env variables

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/RG-Le/Kidney-Disease-Classification-MLFlow.mlflow

export MLFLOW_TRACKING_USERNAME=RG-Le

export MLFLOW_TRACKING_PASSWORD=c9385918b480d09da6663c4a7f67a55fdce010aa
```