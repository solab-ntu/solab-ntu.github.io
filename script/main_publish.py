from collections import OrderedDict
import json
import os

import tool
from tool import REPO, FILE

if __name__ == "__main__":
    # 刪除 Publication.html
    try:
        os.remove(REPO / "Publication/Publication.html")
    except Exception:
        pass

    # 讀取人員資料
    with open(FILE / "people.json", encoding="utf-8") as fp:
        data = json.loads(fp.read())

    data = {int(k): v for k, v in data.items()}
    data = sorted(
        data.items(), key=lambda x: (x[1]["name"]["first"], x[1]["name"]["second"])
    )
    data = OrderedDict(data)

    # 產生 Publication.html
    pubs = tool.Publication(data)
    pubs.sort()
    pubs.create_page()
