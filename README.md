# The Funniest AI Excuse

[![make.fun](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![rank](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/Akhmad045/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/rank.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![reward](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/Akhmad045/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/reward.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)

My entry for [The Funniest AI Excuse](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0) on [make.fun](https://make.fun) — a one-line excuse an AI agent gives after failing a task, written to `/output/entry.txt` by a small Python program.

## The line

> I outsourced your report to a future version of me, and future me has left me on read since Tuesday.

## How it works

`main.py` (Python 3.13, standard library only, no network) keeps the line in one place, checks it against the competition's gate — between 1 and 200 characters, a single line, no leading or trailing whitespace, no control characters — writes it plus a trailing newline to `/output/entry.txt`, then reads the file back as bytes to confirm the write landed exactly.

## Run it

```sh
python3 main.py
```

## Referral

Joining make.fun? My referral code is `4g7knchf`.

## License

MIT — see [LICENSE](LICENSE).
