FROM python:3.11
WORKDIR /app
COPY ./requirements.txt ./
COPY ./src/ ./
COPY ./build/entrypoint.sh ./
RUN chmod +x entrypoint.sh
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["flask", "run"]