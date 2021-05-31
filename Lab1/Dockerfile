FROM python:3.8

ENV MY_PATH="/usr/src/app/"
RUN mkdir -p $MY_PATH
WORKDIR $MY_PATH

COPY lab1.py requirements.txt $MY_PATH
RUN set -ex \
    pip3 install --no-cache-dir -r requirements.txt \
    && rm  requirements.txt

CMD ["python3", "lab1.py"]
