# Level 5 — curl and HTTP (slides 27–30)

Start the server in a second terminal, from the repository root:

```sh
python3 05-curl/workshop_server.py
```

In your first terminal, run `cd 05-curl`. `HOST` on the slides is `localhost` when you run the server yourself. Port `8000` is the service, and `/clue.txt` is the requested path.

```sh
curl http://localhost:8000/clue.txt
curl -I http://localhost:8000/clue.txt
curl -o clue.txt http://localhost:8000/clue.txt
curl -L http://localhost:8000/old
curl -sS http://localhost:8000/clue.txt
curl -I http://localhost:8000/nope.txt
```

The `-o` command creates a local `clue.txt` in this folder. The `/old` path redirects to `/clue.txt`; `-L` follows that redirect. `/nope.txt` deliberately returns HTTP 404. The service also has a `/final?ip=...` endpoint used in the boss challenge.

Stop the server with `Ctrl+C` when you finish. If port 8000 is already in use, run `python3 05-curl/workshop_server.py --port 8001` and replace `:8000` with `:8001` in the commands.
