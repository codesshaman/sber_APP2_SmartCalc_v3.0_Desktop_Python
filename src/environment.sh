python3.10 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install tk
touch requirements.txt
pip freeze >> requirements.txt
pip install -r requirements.txt
pip freeze