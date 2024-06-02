from collections import OrderedDict
import json
from pathlib import Path

FILE = Path(__file__).resolve()
REPO = FILE.parents[1]

if __name__ == "__main__":
    with open(REPO / "people.json", encoding="utf-8") as fp:
        data = json.loads(fp.read())

    data = {int(k): v for k, v in data.items()}
    data = sorted(
        data.items(), key=lambda x: (x[1]["name"]["first"], x[1]["name"]["second"])
    )
    data = OrderedDict(data)
