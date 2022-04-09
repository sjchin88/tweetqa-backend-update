FROM python:3.8

ENV RUNNER_IP=172.17.0.2

# Install OpenJDK-11
RUN apt-get update && \
    apt-get install -y openjdk-11-jre-headless && \
    apt-get clean

ADD . /app/
WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

# CMD gunicorn -b :8080 'main:start(runner_ip="$r_ip")'
CMD ./run_app.sh ${SECRET_KEY} ${RUNNER_IP} ${GMAIL_PWD}
