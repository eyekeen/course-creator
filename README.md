python 3.12.2

python3 -m venv .venv or python -m venv .venv

pip install requirements.txt

widnows: .venv\Scripts\activate
linux: .venv/bin/activate

flask --app ./ run --debug