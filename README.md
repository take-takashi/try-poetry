# try-poetry
poetryを試してみる試み

## setup
```sh
poetry new project --src
```

## test
事前に`pyproject.toml`に設定を追記する。

また、VSCODE標準のテスト機能は使わずに、ターミナルから`poetry run pytest`した方がややこしくなくて良い。

（VSCODE標準はどうせパスが解決しにくい）
```sh
cd project
poetry run pytest

```