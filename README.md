# BNC_COCA_EN2CN-Freq-for-Yomitan

Frequency dictionaries for [Yomitan](https://github.com/themoeway/yomitan), based on data from [BNC_COCA_EN2CN](https://github.com/changhongzi/BNC_COCA_EN2CN).

---

## 📦 Dictionary

### `coca-freq-yomitan.zip` — BNC/COCA Frequency

- **Source**: [changhongzi/BNC_COCA_EN2CN](https://github.com/changhongzi/BNC_COCA_EN2CN) (`BNC_COCA_lists.csv`)
- **Entries**: ~76,000 word forms (including inflections)
- **Rank**: Based on BNC/COCA graded word lists (1k, 2k, …, 25k); rank = `(n-1) × 1000 + 500`
- **Note**: Word families expanded — e.g. `ability`, `abilities`, `able` share the same rank

## 🚀 Import to Yomitan

1. Open Yomitan extension settings (click icon → ⚙️)
2. Go to **Dictionaries** → **Import**
3. Select `coca-freq-yomitan.zip` to import

## 📊 Frequency Distribution

| Band | Rank Range | Entries (approx.) |
|------|------------|-------------------|
| Core 1k | 1–1,000 | ~1,000 |
| 2k–5k | 1,001–5,000 | ~4,000 |
| 6k–10k | 5,001–10,000 | ~5,000 |
| 11k–25k | 10,001–25,000 | ~15,000 |
| **Total (all forms)** | — | **76,062** |

> Rank is encoded as `(band n - 1) × 1000 + 500`. All word forms within the same band share one rank value.

## 🛠️ Build

Requires Python 3 standard library only (`csv`, `json`, `zipfile`, `re`).

```bash
python3 make_coca.py
```

## 📄 Credits

Original data compiled by [@changhongzi](https://github.com/changhongzi), released at [BNC_COCA_EN2CN](https://github.com/changhongzi/BNC_COCA_EN2CN). Please refer to the original repository for licensing details.

Yomitan dictionary format: [themoeway/yomitan](https://github.com/themoeway/yomitan).

---

## 中文说明
由于Yomitan英文词典比较匮乏，本仓库收集优质的Yomitan英文词频词典，帮助Yomitan英文学习者。
### `coca-freq-yomitan.zip` — BNC/COCA 词频词典

- **来源**：[changhongzi/BNC_COCA_EN2CN](https://github.com/changhongzi/BNC_COCA_EN2CN)（`BNC_COCA_lists.csv`）
- **词条数**：约 76,000 个词形（含派生与屈折变化形式）
- **排名方式**：基于 BNC/COCA 分级词表（1k、2k、……、25k），rank = `(n-1) × 1000 + 500`
- **说明**：同一词族的所有词形共享同一 rank，例如 `ability`、`abilities`、`able` 排名相同

### 导入方法

1. 打开 Yomitan 扩展设置（点击图标 → ⚙️）
2. 进入 **Dictionaries** → **Import**
3. 选择 `coca-freq-yomitan.zip` 导入

### 分布统计

| 分级 | Rank 范围 | 词条数（约） |
|------|-----------|-------------|
| 核心 1k | 1–1,000 | ~1,000 |
| 2k–5k | 1,001–5,000 | ~4,000 |
| 6k–10k | 5,001–10,000 | ~5,000 |
| 11k–25k | 10,001–25,000 | ~15,000 |
| **全部词形** | — | **76,062** |

> Rank 采用 `(分级 n - 1) × 1000 + 500` 编码，同一级别所有词形共享同一 rank 值。

### 构建脚本

仅依赖 Python 3 标准库（`csv`、`json`、`zipfile`、`re`），无需额外安装。

```bash
python3 make_coca.py
```

### 数据来源

原始数据由 [@changhongzi](https://github.com/changhongzi) 整理发布，详见 [BNC_COCA_EN2CN](https://github.com/changhongzi/BNC_COCA_EN2CN)，授权协议请参考原仓库。

---

## 🎁 彩蛋：考研词频

本仓库包含考研真题词频词典 `netem-freq-yomitan.zip`，面向备考考研的中国学习者。

数据来自 [exam-data/NETEMVocabulary](https://github.com/exam-data/NETEMVocabulary)（`netem_full_list.json`），收录 **5,530 考研核心词条**，以考研真题语料库词频排序（序号 1 = 最高频）。154 词含变体拼写，已全部展开为独立词条。

### 导入方法

1. 打开 Yomitan 扩展设置（点击图标 → ⚙️）
2. 进入 **Dictionaries** → **Import**
3. 选择 `netem-freq-yomitan.zip` 导入

两个词典可同时启用，互不冲突。

### 词频分布

| 词频段 | 词条数 | 说明 |
|--------|--------|------|
| 10,000 次以上 | 14 | the、be、a 等核心虚词 |
| 5,000–10,000 | 18 | to、of、and 等 |
| 1,000–5,000 | 151 | 高频实词与功能词 |
| 500–1,000 | 175 | 考研高频词 |
| 100–500 | 1,051 | 中频词 |
| 0–100 | 4,121 | 低频长尾词（约占 75%） |

词频中位数为 **30 次**，即半数词汇在考研真题中出现不超过 30 次。

### 构建脚本

```bash
python3 make_netem.py
```
