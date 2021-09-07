FROM kenhv/kensurbot:debian

RUN set -ex \
    && git clone -b master https://github.com/etahamad/Android-12-Checker /root/userbot \
    && chmod 777 /root/userbot

WORKDIR /root/userbot/

RUN sudo pip3 install -r requirements.txt

CMD ["python3", "main.py"]
