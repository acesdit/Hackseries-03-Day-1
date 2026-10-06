# Level 4 — Vim (slides 23–26)

From the repository root, run `cd 04-vim`, then `vim notes.txt`.

The starting file contains a misspelled word and one line of junk. Follow slide 26:

1. Press `i` to enter Insert mode and change `eror` to `error` in the first line.
2. Press `Esc` to return to Normal mode.
3. Type `/eror` and press Enter to find the remaining misspelling.
4. Move to the junk line and press `dd` to delete that whole line.
5. Type `:wq` and press Enter to save and quit.

To leave without saving, press `Esc`, type `:q!`, then Enter. If you want to restart the exercise after editing, get a fresh copy of `notes.txt` from the repository.
