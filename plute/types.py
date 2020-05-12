from dataclasses import dataclass
from typing import Optional, List, Dict


@dataclass(frozen=True)
class Intent:
    """
    An intent type.
    """

    type: str
    name: str
    parser: str
    score: Optional[float] = None


Transcript = str
Alternative = Dict
Utterance = List[Alternative]
