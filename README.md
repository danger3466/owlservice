# owlservice

## API Examples
- Получение Token
```shell script
curl -X POST -H 'Accept: application/json' -H 'Content-Type: application/json' -i 'http://127.0.0.1:8000/api/v1.0/auth/token/login/' --data '{"username":"test","password":"testpassword"}'
```
```json
{"auth_token":"54e34d1a00f1884a53d8ef757fdece5dcd6bc405"}
```
- Создание модели телефона
```shell script
curl -X POST -H 'Accept: application/json' -H 'Content-Type: application/json' -H 'Authorization: Token 54e34d1a00f1884a53d8ef757fdece5dcd6bc405' -i 'http://127.0.0.1:8000/api/v1.0/models/' --data '{"model_name":"Nokia 3100"}'
```
```json
{"id":9588,"model_name":"Nokia 3100"}
```
- Получение списка моделей
```shell script
curl -X GET -H 'Accept: application/json' -H 'Authorization: Token 54e34d1a00f1884a53d8ef757fdece5dcd6bc405' -i 'http://127.0.0.1:8000/api/v1.0/models/'
```
```json
[{"id":9586,"model_name":"test model"},{"id":9587,"model_name":"Nokia 3100"}]
```
- Создание заявки
```shell script
curl -X POST -H 'Accept: application/json' -H 'Content-Type: application/json' -H 'Authorization: Token 54e34d1a00f1884a53d8ef757fdece5dcd6bc405' -i 'http://127.0.0.1:8000/api/v1.0/tickets/' --data '{"model":9587, "client_name":"Bond","client_phone":"+72222222222","imei":1231321321}'
```
```json
{"id":5204,"date_create":"2020-03-04T12:14:06.196612Z","model_name":"Nokia 3100","status_name":"Ожидает","client_name":"Bond","client_phone":"+72222222222","imei":1231321321,"model":9587,"status":1}
```
- Список заявок
```shell script
curl -X GET -H 'Accept: application/json' -H 'Content-Type: application/json' -H 'Authorization: Token 54e34d1a00f1884a53d8ef757fdece5dcd6bc405' -i 'http://127.0.0.1:8000/api/v1.0/tickets/'
```
```json
[{"id":5203,"date_create":"2020-03-04T11:21:31Z","model_name":"test model","status_name":"Ожидает","client_name":"х/з кто","client_phone":"+79222550000","imei":null,"model":9586,"status":1},{"id":5204,"date_create":"2020-03-04T12:14:06Z","model_name":"Nokia 3100","status_name":"Ожидает","client_name":"Bond","client_phone":"+72222222222","imei":1231321321,"model":9587,"status":1},{"id":5205,"date_create":"2020-03-04T12:15:08Z","model_name":"Nokia 3100","status_name":"Ожидает","client_name":"Bond","client_phone":"+72222222222","imei":null,"model":9587,"status":1}]
```
- Конкретная заявка
```shell script
curl -X GET -H 'Accept: application/json' -H 'Content-Type: application/json' -H 'Authorization: Token 54e34d1a00f1884a53d8ef757fdece5dcd6bc405' -i 'http://127.0.0.1:8000/api/v1.0/tickets/5203/'
```
```json
{"id":5203,"date_create":"2020-03-04T11:21:31Z","model_name":"test model","status_name":"Ожидает","client_name":"х/з кто","client_phone":"+79222550000","imei":null,"model":9586,"status":1}
```
- Добавить коментарий
```shell script
curl -X POST -H 'Accept: application/json' -H 'Content-Type: application/json' -H 'Authorization: Token 54e34d1a00f1884a53d8ef757fdece5dcd6bc405' -i 'http://127.0.0.1:8000/api/v1.0/comments/' --data '{"ticket":5203, "comment":"Wow first comment!"}'
```
```json
{"comment_id":14422,"comment":"Wow first comment!","date_create":"2020-03-04T12:08:37.548819Z","ticket":5203}
```