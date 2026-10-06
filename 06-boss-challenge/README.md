# Boss challenge — Find, count, request (slide 31)

From the repository root, run `cd 06-boss-challenge`. Start the Python server in a second terminal as described in the [main README](../README.md). Work with a partner if you like.

1. Find a hidden file in this folder and read its instruction.
2. Use a pipeline on `access.log` to identify the IP with the most `ERROR` lines. The staged commands on slides 21–22 are your toolbox.
3. Put that IP in the `ip=` part of the URL from the hidden instruction and request the final clue with `curl`.
4. Submit the final clue **and the commands** you used.

The HTTP service returns a helpful error if the IP is wrong. If the server is unavailable, pause at this step and share the IP and commands you found with the workshop leader.
