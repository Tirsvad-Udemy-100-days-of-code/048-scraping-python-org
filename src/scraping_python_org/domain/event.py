"""The Event value object."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Event:
    """An upcoming event with its date text and name."""

    time: str
    name: str

    def to_dict(self) -> dict[str, str]:
        """Return the event as a plain dictionary."""
        return {"time": self.time, "name": self.name}
