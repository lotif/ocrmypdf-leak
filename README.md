# ocrmypdf high memory usage and possible memory leak

1. Build docker image:
```shell
docker build -t ocrmypdf_leak:latest .
```
2. Start the docker image 
```shell
docker run -it --memory=3g --memory-swap=3g --name=ocrmypdf_leak ocrmypdf_leak /bin/bash
```
3. Install tesseract:
```shell
add-apt-repository ppa:alex-p/tesseract-ocr5 -y
apt-get -y install tesseract-ocr libtesseract-dev
```
4. Run the script:
```shell
python -m leak
```
5. Watch as the memory usage slowly climbs enough until it expolodes. It may take some time.
