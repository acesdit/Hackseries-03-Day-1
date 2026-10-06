# Level 2 — Navigation, files, and search (slides 9–16)

From the repository root, run `cd 02-navigation-and-files`. Stay here for the slide commands. This folder contains a hidden clue, `clue.txt`, and a short `access.log`. There is deliberately **no** `notes` or `test` directory at the start: you create them.

## List and create (slides 10–11)

```sh
ls
ls -a
ls -l
ls -lah
mkdir test
touch file1.txt
cat file1.txt
mkdir notes
touch notes/todo.txt
ls notes
```

`cat file1.txt` prints nothing because the new file is empty.

## Copy, move, and remove (slides 12–13)

```sh
cp clue.txt backup.txt
mv backup.txt old.txt
mv old.txt notes/
rmdir test
rmdir notes
```

The last command should fail: `notes` contains files. To practice `rm` safely, remove only files you created inside this exercise folder. For example, after inspecting `notes/old.txt`, run `rm notes/old.txt`.

Slide 13's `rm backup.txt` is a separate example. The sequence above has already renamed and moved `backup.txt`, so copy `clue.txt` to `backup.txt` again before trying that exact command.

## Hidden-file side quest (slide 14)

Find and display `.first-clue` without opening this README for the answer. `ls -la` and `cat` are enough.

## Read and search (slides 15–16)

```sh
cat clue.txt
less access.log
head -5 access.log
tail -5 access.log
wc -l access.log
find . -name "*.txt"
grep -n "ERROR" access.log
grep -i "error" access.log
grep -R "FLAG" .
```

Press `q` to leave `less`. The recursive `grep` should find a practice marker in a text file below this folder.
