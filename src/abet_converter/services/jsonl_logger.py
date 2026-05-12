from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class JsonlLogger:
    def __init__(self, path: Path, run_id: str, dataset_id: str, step_name: str) -> None:
        self.path = path
        self.run_id = run_id
        self.dataset_id = dataset_id
        self.step_name = step_name
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def log(self, event_type: str, message: str, **context: Any) -> None:
        record = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "run_id": self.run_id,
            "dataset_id": self.dataset_id,
            "step_name": self.step_name,
            "event_type": event_type,
            "message": message,
            "context": context,
        }
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, ensure_ascii=True) + "\n")
