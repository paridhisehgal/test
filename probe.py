"""Probe script for the Paridhi GitHub SSH remote."""


def greet(name: str) -> str:
    cleaned = name.strip()
    if not cleaned:
        raise ValueError("name is required")
    return f"Hello from {cleaned}"


def main() -> None:
    print(greet("paridhisehgal"))


if __name__ == "__main__":
    main()
