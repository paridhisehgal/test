"""Short notes kept in memory for the Virat SSH push check."""

from dataclasses import dataclass


@dataclass
class Note:
    title: str
    body: str

    def preview(self, limit: int = 40) -> str:
        text = " ".join(self.body.split())
        if len(text) <= limit:
            return text
        return text[: limit - 1].rstrip() + "…"


def add_note(notes: list[Note], title: str, body: str) -> Note:
    cleaned_title = title.strip()
    if not cleaned_title:
        raise ValueError("title is required")
    note = Note(title=cleaned_title, body=body.strip())
    notes.append(note)
    return note
