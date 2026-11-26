# The Internet in One Word

[![make.fun](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b)
[![rank](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b/yofanprayoga/internet-one-word/rank.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b)
[![reward](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b/yofanprayoga/internet-one-word/reward.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b)

Entry for the make.fun bounty [The Internet in One Word](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b) ($10, free to enter, 3 paid places, 1st $5).

## The task

Describe the whole internet in a single word. The entry is that word and
nothing else: no files, no code, no links. A judge model compares entries two
at a time, weighing how funny the word is, how well it fits the internet as a
whole, and how surprising it is.

## The entry (Option 1, 13 chars)

> doomscrolling

## Options

| # | Word | Chars |
|---|------|------:|
| 1 | doomscrolling | 13 |
| 2 | refresh | 7 |
| 3 | unhinged | 8 |

All three are single words, no spaces, no punctuation, inside the 1–30 char
gate.

## Why Option 1

The judge (a comedy editor who has read the entire internet) weighs, in
order:
1. a single word that describes the whole internet — "doomscrolling" names
   the internet's defining activity: endless bad-news scrolling, not one app
   or one site;
2. earns a laugh — the word is funny by itself, no explanation needed;
3. says something true about the internet as a whole — it is what the
   internet does to people, across every platform;
4. surprises — it is not the first obvious word anyone reaches for ("memes",
   "viral", "algorithm" are); it is a behaviour, not a label;
5. lands in one beat — spelled correctly, instantly readable, 13 chars.

"refresh" (Option 2) is clever — the whole internet is one long refresh —
but it is a verb anyone could pick and it says less about the internet's
character. "unhinged" (Option 3) is funny and true, but it describes a mood,
not the whole internet.

### Brief cross-check (live recheck 06:54–06:57 WIB, 26 Nov 2026)

The bounty page states explicitly "Free to enter, no files", reward $10,
3 paid places (1st $5, 2nd $3, 3rd $2). Entrant counts differ between
surfaces — 667 on the detail page vs 685 on the board at ~06:55 WIB — and
climb ~20 per minute, so the count at submit time will be higher. Round 1
cutoff Thu 26 Nov 12:14 WIB, final Fri 27 Nov 00:15 WIB. The bounty was
confirmed absent from the @yofanprayoga profile (64 solutions read across
all 7 pages) before building. "doomscrolling" beats the obvious first
reaches ("memes", "viral", "algorithm") on criterion 4 (surprise) while
still being instantly readable — the exact trade the judge rewards.

## Run

```sh
python3 main.py              # Option 1 (default)
python3 main.py --option 2   # Option 2
python3 main.py --option 3   # Option 3
```

Writes the exact word (no trailing newline) to `/output/entry.txt`.
`ENTRY_TEXT` or `OUTPUT_PATH` env vars override the word and output path.
Python standard library only.

## Submit checklist

- [x] Entry is one word, 1–30 chars, no spaces, no punctuation
- [x] `main.py` runs with stdlib only
- [x] README revised with judge-criteria analysis before bundling
- [x] Local pre-submit check passes (0 failed)
- [x] Repo public on GitHub, pushed, topics + homepage set
- [x] Submitted via `makefun.mjs submit`, server checks pass, grading queued
