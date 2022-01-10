FROM python:3-slim
USER root

# ENV LANG ja_JP.UTF-8
# ENV LANGUAGE ja_JP:ja
# ENV LC_ALL ja_JP.UTF-8
# ENV TZ JST-9
# ENV TERM xterm 

RUN apt-get update && \
    apt-get install -y git && \
    apt-get install -y vim less && \
    pip3 install --upgrade pip && \
    pip3 install --upgrade beautifulsoup4 && \
    pip3 install --upgrade Flask
    # pip3 install --upgrade setuptools && \
    # pip3 install --upgrade jupyterlab
    