# BNG-HUAWEI

Simple scripts written for helping me to configure Huaweis BNGs NE40/NE8000.

## Installation

```bash
git clone https://github.com/aweher/bng-huawei.git

cd bng-huawei/
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp perfiles.yaml.example perfiles.yaml
```

Then you must edit `perfiles.yaml` before running the `main.py` script.

```bash
python3 main.py
```
