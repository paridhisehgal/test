"""Tiny text stats used alongside the notes module."""


def letter_count(text: str) -> int:
    return sum(1 for char in text if char.isalpha())


def word_count(text: str) -> int:
    return len(text.split())


def summarize(text: str) -> str:
    return f"{word_count(text)} words, {letter_count(text)} letters"
