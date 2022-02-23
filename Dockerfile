FROM python:3.10.2-alpine3.15

WORKDIR /usr/src/app
COPY requirements.txt server.py .
RUN \
    pip install --quiet --requirement requirements.txt &&\
    :

EXPOSE 6543
ENTRYPOINT ["/usr/local/bin/python3"]
CMD ["/usr/src/app/server.py"]
