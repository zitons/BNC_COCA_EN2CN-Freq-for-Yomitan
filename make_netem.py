import json, zipfile

with open('/sdcard/Download/netem_full_list.json', encoding='utf-8') as f:
    data = json.load(f)

entries = []
for item in data['5530考研词汇词频排序表']:
    rank = item['序号']
    word = item['单词'].strip().lower()
    if word:
        entries.append([word, 'freq', rank])
    other = item.get('其他拼写')
    if other:
        for w in other.replace('，', ',').split(','):
            w = w.strip().lower()
            if w and w != word:
                entries.append([w, 'freq', rank])

entries.sort(key=lambda x: x[2])
print(f'共 {len(entries)} 个词形，前 5 个: {entries[:5]}')

index = {
    'title': '考研词频 (5530 netem)',
    'format': 3,
    'revision': '1',
    'sequenced': True
}

with zipfile.ZipFile('/sdcard/Download/netem-freq-yomitan.zip', 'w', zipfile.ZIP_DEFLATED) as zf:
    zf.writestr('index.json', json.dumps(index, ensure_ascii=False))
    for i in range(0, len(entries), 10000):
        chunk = entries[i:i+10000]
        zf.writestr(f'term_meta_bank_{i//10000+1}.json', json.dumps(chunk, ensure_ascii=False))

print('完成！')
