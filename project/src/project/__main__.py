from schemas.sample_schema import sample_schema

def main() -> None:
    print(sample_schema)
    hello()

def hello() -> str:
    return "hello"

main()