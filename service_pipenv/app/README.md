# app

* Pythonアプリのルート
* ここでエディタを開く

## poetry

1. install poetry.

    ```sh
    curl -sSL https://install.python-poetry.org | python3 -
    poetry config virtualenvs.create false
    # 諸説ある。
    # :pos: docker使うなら…
    # :neg: systemのpython環境から分離できない
    ```

1. registar dependancies

    ```sh
    poetry add fastapi numpy
    ```

1. registar develop dependancies

    ```sh
    poetry add black ruff isort mypy --group dev
    ```

1. install dependancies

    ```sh
    poetry install
    ```

1. install develop dependancies
    ```sh
    poetry install
