@echo off
echo Starting local HTTP server on port 8000...
echo Opening HermitUI in your default browser...



:: Start the Python HTTP server (blocks the terminal until stopped)
python -m http.server 8000



:: Open the browser in the background
start http://localhost:8000/dist/hermit-ui-wllama.html