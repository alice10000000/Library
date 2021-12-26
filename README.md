## Dependency issue fixed （2021/12/26）
 - fix dependencies issue
 - python version used in project: 3.10

## Run project (2021/10)

```bash
$ # Activae virtual env
$ cd env\Scripts
$ activate

$cd ../..
$ pip3 install -r requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application 
$ python manage.py runserver 

```
