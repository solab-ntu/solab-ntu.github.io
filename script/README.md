# script

1. 修改 `main_dump.py` 的內容，每新增一個人就必須複製以下的程式碼，執行後會在產生 `script/people.json` 檔案。

```python
i += 1
pp = tool.People()
pp["name"]["chi"] = ""
pp["name"]["eng"] = ""
pp["year"] =
pp["alumni"] = False
pp["lab_id"] = "碩士班學生 M.S. Student"
pp["degrees"][0] = {"chi": "", "eng": ""}
pp["degrees"][1] = {"chi": "", "eng": ""}
pp["jobs"][0] = {
    "chi": "",
    "eng": "",
    "web": ""}
pp["thesis"] = {
    "chi": "",
    "eng": "",
    "file": "",
    "drive": ""}
pp["research"] = {
    "chi": "",
    "eng": ""}
pp["papers"][0] = {
    "ref": """""",
    "file": "",
    "drive": "",
    "type": "",
    "year": }
pp.set_first_second()
data[i] = pp
```

2. 照片大小修改為 300x225，放在資料夾 `People/files` 底下，檔名請使用上述變數 `pp["name"]["eng"]`，並使用 jpg。
3. 執行 `main_member.py` 會變更 `People/Member` 與 `People/Alumni` 底下的網頁
4. 若發表的文章 (papers) 有更動，則執行 `main_publish.py`，會根據 `people.json` 的內容自動修改網頁 `Publication/Publication.html`。
