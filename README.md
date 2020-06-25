<h1 align="center">Welcome to Rent-A-Car 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-V 1.0.0-blue.svg?cacheSeconds=2592000" />
  <a href="#" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
</p>

## Prerequisites

[python 3](https://www.python.org)
<p> pip 3 | viene con python <p>

> API sobre servicio de renta de carros (Python 3)

## Instalar requerimientos

```sh
pip3 install -r requirements.txt
```

## Correr la App

```sh
python3 -m app.py
```

>Tambien puede ser realizado dentro de un entorno ENV o con una Env Variable.

## EndPoints

>Base Url

__localhost:5000/__

<p> URL creado automaticamente al momento de correr la app. En caso de que el puerto cause conflicto puede 
el puerto puede ser cambiado dentro de el archivo app.py de la siguiente manera

```python
app.run(port="puerto_deseado")
```

#### Rutas de Usuario

__/register__

<p>[methods=”POST”]: Te permite registrarte como un usuario en la API. En caso de no estar registrado no podras realizar login, lo cual limitara el uso de la app y evitara que puedas rentar un carro.</p>

```json
{
  “username”: user_username,
  “password”: user_password
}
```
_Nota: El password se encriptara automaticamente. Los valores enviado deben ser de tipo String._

__/login__

<p>[methods=”GET”,”POST”]: Al utilizer el metodo GET y estar loggeado te notificara bajo que usuario te encuentras loggeado, en caso de no estar loggeado, te solicitara que hagas login mediante a un POST request.</p>

```json
{
  “username”: user_username, 
  “password”: user_password
}
```

_Nota: El password es desencriptado automaticamente. En caso de no coincidir con el password seleccionado durante el registro no podras loggearte._

__/user/<username>__

<p>[methods=”GET”]: Podras ver la informacion (perfil) de el usuario en el cual te encuentres actualmente.<p>

**Necesitas estar loggeado para ver la información**

_Nota: Username es una variable utilizada dentro de el programa. Esto quiere decir que <username> en el endpoint debe ser igual al nombre del usuario. Por ejemplo: Inicie sesión como “jose12”entonces /user/jose12 seria el endpoint al que deberías acceder para ver tu perfil._

__/user/list_users__

<p>[methods=”GET”]: Al hacer un GET request a este endpoint obtenemos la informacion de todos los usuarios registrados. </p>

**Necesitas estar loggeado para ver la información**

__/logout__

<p>[methods=”GET”]: Haces logout de la app.<p>

#### Rutas de Carros

__/nuevo_carro__

<p>[methods=”POST”] : Te permite crear un nuevo carro en la base de datos. <p>

**Necesitas estar loggeado para realizar esta acción**

```json
{
  “modelo”: modelo, 
  “marca”: marca ,
	“año”: año,
	“kilometraje”: kilometraje
}
```

__/carros__

<p>[methods=”GET”]: Te permite obtener una lista de todos los carros dentro de la base de datos que esten disponibles para ser alquilados. Si hay un carro que no aparezca aquí es debido a que se encuentra alquilado. Para ver la informacion de ese carro debemos ver la lista de los usuarios y buscar el carro por marca especificamente.<p>

__/carros/<marca>__

<p>[methods=“GET”]: Nos permite obtener la información de una marca de carros especificos. < marca > funciona como una variable en el endpoint, esto quiere decir que puede ser intercambiable. Por ejemplo: si quiero buscar los carros de la marca “Honda” basta con ir al endpoint <em>/carros/Honda</em> y recibiremos un listado de todos los carros de la marca Honda.</p>

__/editar_carro/<_id>__

<p>[methods=”PUT”]: Nos permite editar un carro especifico al proveer el id que este tiene dentro de la base de datos. La variable < _id > es intercambiable, el resultado sera diferente dependiendo de el id provisto.<p>

**Necesitas estar loggeado para realizar esta acción**

```json
{
  “modelo”: nuevo_modelo, 
  “marca”: nueva_marca ,
	“año”: nuevo_año
	“kilometraje”: nuevo_kilometraje
}
```

__/eliminar_carro/<_id>__

<p> [methods=”DELETE”]: Elimina un carro. El carro se eliminara de acuerdo al < _id > en el endpoint. <p>

__/rentar/<_id>__

<p>[methods=”GET”,”POST”]: Nos permite rentar un carro. El usuario loggeado puede seleccionar, basado en la lista de carros, el < _id > que quiera alquilar. El carro sera asociado directamente al usuario que se envie en el POST request. </p>

**Necesitas estar loggeado para realizar esta acción**

```json
{
      “username”: username
}
```

## Author

👤 **Roger Urrutia**

* Github: [@rogeralexei](https://github.com/rogeralexei)
