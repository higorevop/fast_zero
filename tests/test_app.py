from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get("/")  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {"message": "Olá Mundo!"}  # Assert


def test_create_user(client):
    response = client.post(
        "/users/",
        json={
            "username": "testeusername",
            "password": "password",
            "email": "teste@teste.com",
        },
    )

    # Validar UserPublic
    assert response.status_code == HTTPStatus.CREATED

    assert response.json() == {
        "username": "testeusername",
        "email": "teste@teste.com",
        "id": 1,
    }


def test_read_users(client):
    response = client.get("/users/")

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {
        "users": [
            {
                "username": "testeusername",
                "email": "teste@teste.com",
                "id": 1,
            }
        ]
    }


def test_read_user(client):
    response = client.get("/users/1/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "username": "testeusername",
        "email": "teste@teste.com",
        "id": 1,
    }


def test_read_user_not_found(client):
    response = client.get("/users/2/")
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found"}


def test_update_user(client):
    response = client.put(
        "/users/1/",
        json={
            "username": "testeusername2",
            "email": "teste@teste.com",
            "password": "password",
        },
    )

    assert response.status_code == HTTPStatus.ACCEPTED

    assert response.json() == {
        "username": "testeusername2",
        "email": "teste@teste.com",
        "id": 1,
    }


def test_update_user_not_found(client):
    response = client.put(
        "/users/2/",
        json={
            "username": "testeusername2",
            "email": "teste@teste.com",
            "password": "password",
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found"}


def test_delete_user(client):
    response = client.delete(
        "/users/1/",
    )

    assert response.status_code == HTTPStatus.NO_CONTENT


def test_delete_user_not_found(client):
    response = client.delete("/users/2/")

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found"}
