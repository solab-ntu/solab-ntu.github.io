from collections import OrderedDict
import json
import os
import shutil
import time

import tool
from tool import REPO, FILE

if __name__ == "__main__":
    # 移除成員資料夾
    try:
        shutil.rmtree(REPO / "People/Member", ignore_errors=True)
    except Exception:
        pass
    finally:
        time.sleep(1)
        os.mkdir(REPO / "People/Member")

    # 移除校友資料夾
    try:
        shutil.rmtree(REPO / "People/Alumni", ignore_errors=True)
    except Exception:
        pass
    finally:
        time.sleep(1)
        os.mkdir(REPO / "People/Alumni")

    # 讀取成員資料
    with open(FILE / "people.json", encoding="utf-8") as fp:
        data = json.loads(fp.read())

    data = {int(k): v for k, v in data.items()}
    data = sorted(
        data.items(), key=lambda x: (x[1]["name"]["first"], x[1]["name"]["second"])
    )
    data = OrderedDict(data)

    # 建立成員頁面
    member = tool.Member(data)
    member.create_member_page()
    member.create_member_pages()
    member.create_alumni_page()
    member.create_alumni_pages()
