"""Probe script for the Paridhi GitHub SSH remote."""


def greet(name: str) -> str:
    cleaned = name.strip()
    if not cleaned:
        raise ValueError("name is required")
    return f"Hello from {cleaned}"


def count_letters(name: str) -> int:
    return len(name.strip())


def main() -> None:
    who = "paridhisehgal"
    print(greet(who))
    print(f"letters: {count_letters(who)}")


if __name__ == "__main__":
    main()
