python 3.12.2

python3 -m venv .venv or python -m venv .venv


widnows: .venv\Scripts\activate
linux: .venv/bin/activate

pip install -r requirements.txt

flask --app ./ run --debug