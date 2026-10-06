# Level 3 — Streams and pipelines (slides 17–22)

From the repository root, run `cd 03-streams-and-pipelines`. `access.log` begins with the sample lines shown on slide 21 and contains enough entries to rank the error IPs.

## Redirect output and errors (slides 18–19)

```sh
ls -l > output.txt
ls -l >> output.txt
sort < output.txt
grep "ERROR" access.log > errors.txt
wc -l < errors.txt
ls nope 2> err.txt
```

`output.txt`, `errors.txt`, and `err.txt` are created by those commands. `ls nope` is supposed to fail; its error is saved in `err.txt`.

## Build the pipeline (slides 20–22)

```sh
grep "ERROR" access.log | wc -l
grep ' ERROR ' access.log
grep ' ERROR ' access.log | cut -d' ' -f1
grep ' ERROR ' access.log | cut -d' ' -f1 | sort
grep ' ERROR ' access.log | cut -d' ' -f1 | sort | uniq -c | sort -nr | head -3
```

Ask what each stage outputs before adding the next one. To save the final ranking, append `> top-ips.txt` to the last command. The highest count will also matter in the boss challenge.

Slide 20's `ls -l | grep "Oct"` depends on the date shown by your computer, so it may display no lines. The log pipeline above gives the same pipe practice on stable data.
