from collections import OrderedDict
import json

from tool import FILE

if __name__ == "__main__":
    with open(FILE / "people.json", encoding="utf-8") as fp:
        data = json.loads(fp.read())

    data = {int(k): v for k, v in data.items()}
    data = sorted(
        data.items(), key=lambda x: (x[1]["name"]["first"], x[1]["name"]["second"])
    )
    data = OrderedDict(data)
