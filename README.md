git clone https://github.com/OzymandiasKok/AddaDjango.git
cd AddaDjango

se linux
python3 -m venv venv
source venv/bin/activate

se windows

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

para acessar o django admin crie um super usuário
python manage.py createsuperuser
