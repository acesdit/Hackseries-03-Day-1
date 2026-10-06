# Level 1 — Setup and the shell mental model (slides 3–8)

Start in this folder:

```sh
cd 01-setup-and-shell
pwd
ls
```

Check `vim` and `curl` with `command -v vim` and `command -v curl`. The terminal is the window; the shell reads your commands. `echo "$SHELL"` shows the shell named in your environment.

On the slides, `$` represents the prompt; do not type it. Names such as `HOST` and `<filename>` are placeholders. For example, type `cat clue.txt` here, not `cat <filename>`.

Try the navigation sequence from slide 8:

```sh
pwd
ls
cd ..
pwd
cd -
```

Try `cd "My Projects"` to see why quoting a name with spaces matters. Return with `cd ..` before moving to Level 2. `grep -n "ERROR" access.log` from slide 7 is a command anatomy example; its runnable log is in Level 3.
