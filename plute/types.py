from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Intent:
    """
    An intent type.
    """

    type: str
    name: str
    parser: str
    score: Optional[float] = None
