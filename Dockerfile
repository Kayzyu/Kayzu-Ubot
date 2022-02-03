# Using Python Slim-Buster
FROM kayex/kayzu-usbot:buster
#━━━━━ Userbot Telegram ━━━━━
#━━━━━ By Kayzu-Ubot ━━━━━

RUN git clone -b Kayzu-Ubot https://github.com/Kayzyu/Kayzu-Ubot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/Kayzyu/Kayzu-Ubot/Kayzu-Ubot/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3", "-m", "userbot"]
