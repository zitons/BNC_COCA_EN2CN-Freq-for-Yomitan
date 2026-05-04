import csv, json, zipfile, re

def list_to_rank(lst: str) -> int:
    s = lst.strip().lower()
    if s.endswith('k'):
        try:
            n = int(s[:-1])
            return (n - 1) * 1000 + 500
        except Exception:
            pass
    return 99999

# 一定要是这一行，注意两个反斜杠：\\s* 和 \\(
FORM_PAT = re.compile(r'([a-z]+)\s*\(')
word_best_rank = {}

with open('BNC_COCA_EN2CN/BNC_COCA_lists.csv', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        band_str = row.get('List ', '') or row.get('List', '')
        headword = (row.get('Headword ', '') or row.get('Headword', '') or '').strip().lower()
        related = row.get('Related forms', '') or ''

        if not band_str:
            continue
        rank = list_to_rank(band_str)

        if headword and re.fullmatch(r'[a-z]+', headword):
            old = word_best_rank.get(headword)
            if old is None or rank < old:
                word_best_rank[headword] = rank

        for form in FORM_PAT.findall(related.lower()):
            form = form.strip()
            if not re.fullmatch(r'[a-z]+', form):
                continue
            old = word_best_rank.get(form)
            if old is None or rank < old:
                word_best_rank[form] = rank

entries = [[w, "freq", r] for w, r in word_best_rank.items()]
entries.sort(key=lambda x: x[2])

print(f"共 {len(entries)} 个词形，前 5 个: {entries[:5]}")

index = {
    "title": "COCA Frequency (BNC_COCA_Lists with families)",
    "format": 3,
    "revision": "1",
    "sequenced": True
}

with zipfile.ZipFile('/sdcard/Download/coca-freq-yomitan.zip', 'w', zipfile.ZIP_DEFLATED) as zf:
    zf.writestr("index.json", json.dumps(index, ensure_ascii=False))
    for i in range(0, len(entries), 10000):
        chunk = entries[i:i+10000]
        zf.writestr(f"term_meta_bank_{i//10000+1}.json", json.dumps(chunk, ensure_ascii=False))

print("完成！")
