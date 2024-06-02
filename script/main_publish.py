from collections import OrderedDict
import json
import os
from pathlib import Path

import tool

FILE = Path(__file__).resolve()
REPO = FILE.parents[1]

if __name__ == "__main__":
    try:
        os.remove(REPO / "Publication/Publication.html")
    except Exception:
        pass

    # --

    with open(REPO / "people.json", encoding="utf-8") as fp:
        data = json.loads(fp.read())

    data = {int(k): v for k, v in data.items()}
    data = sorted(
        data.items(), key=lambda x: (x[1]["name"]["first"], x[1]["name"]["second"])
    )
    data = OrderedDict(data)

    # --

    pubs = tool.Publication(data)
    pubs.sort()
    pubs.create_page()
