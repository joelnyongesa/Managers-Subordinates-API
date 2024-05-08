# Managers-Subordinates API

This is a simple API for showing managers and their respective subordinates (people who report directly to them).

## Getting Started.

Before getting started, you will need to have Python 3.9+ installed. Once done follow the steps below:

1. To get started, fork and clone this repository.
2. Run `pipenv install` to install the project dependencies, and `pipenv shell` to activate your virtual environment.
3. Set the environment variables as follows:

```
export FLASK_APP=server/app.py
export FLASK_RUN_PORT=8000
```

4. You will then nee to run the migrations. To do this, use `flask db upgrade head`. This will create the database and tables in the database.

5. Now run the command flask run` to have the app run on port 8000.

## API Endpoints Available.

These are the various endpoints available:

### 1. Subordinates

This is an endpoint for reading and creating new subordinates.

```http
GET /subordinates
```

#### Response

```javascript
{
    "name": string,
    "manager_id": string
}
```

| Status Code | Description |
| :-- | :-- |
| 200 | `Successful` |


```http
POST /subordinates
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
|`name`| `string` | **Required**. A subordinate's name |
|`manager_id` | `integer` | **Optional**. The subordinate's manager |

#### Responses

```javascript
{
    "name": string,
    "manager_id": integer,
}
```

| Status Code | Description |
| :-- | :-- |
| 201 | `OK` |

## Technologies Used.
1. Flask

## Author

Made with ♥️ by Joel Nyongesa