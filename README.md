# Python CLI Docker Project

This is a simple Python CLI utility that counts the number of lines in a log file.

## Run Locally
```
python cli_tool/log_analyzer.py sample.log
```

## Docker
Build and run:
```
docker build -t python-cli-docker .
docker run --rm -v $(pwd):/data python-cli-docker /data/sample.log
```

## CI/CD to Docker Hub
- Add secrets `DOCKER_USERNAME` and `DOCKER_PASSWORD` in your GitHub repo settings.
- On push to main, GitHub Actions will build and push the image to Docker Hub.
