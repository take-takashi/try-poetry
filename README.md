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

## project02 setup
```sh
poetry new project02 --src
# pyproject.tomlの編集を忘れずに行うこと。
cd project-2/src/project02
poetry add jupyter ipykernel # インタープリターが選択できない
# direnvも試してみているが、まだわからない
# poetry config virtualenvs.in-project true --local # このコマンドは大事
# .venvが作られるようにはなったが、インタプリターが選択できない
```