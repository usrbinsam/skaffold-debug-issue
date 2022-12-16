## Steps to Reproduce

1. Skaffold Debug.
2. Set a breakpoint in main.py, lines 15 or 12.
3. Open http://localhost:8080 and execute the corresponding endpoint.
4. Remove the `--reload` parameter from Dockerfile.
5. Re-run skaffold debug (image should rebuild as expected).
6. Repeat steps 2 and 3, and breakpoint should now hit.