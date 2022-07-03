FROM python:3.10.5-slim-bullseye
LABEL domnenko@mail.ru  @domnenko_a_n

WORKDIR ./docker

COPY ./requirements.txt ./
COPY ./source ./

# RUN apt-get update && apt-get -y install net-tools curl procps

RUN pip3 install -r requirements.txt

ENV FLASK_APP="main.py"

EXPOSE 5000

# CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
CMD ["python3", "main.py"]
