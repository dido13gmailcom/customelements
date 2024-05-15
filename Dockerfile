FROM python:3.12

	
ENV TZ="Europe/Paris"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends
RUN apt-get update -y && apt-get install -y chromium

RUN pip install --upgrade pip

RUN echo 'export CHROMIUM_FLAGS="$CHROMIUM_FLAGS --no-sandbox"' >> /etc/chromium.d/default-flags
RUN echo "clear" >> /root/.bashrc
RUN echo "cat /etc/motd" >> /root/.bashrc

WORKDIR /custom_elements_server
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY app .

RUN mkdir /logs 
RUN echo "" > /logs/logs_bo_docker_pre.txt
RUN echo "" > /logs/logs_bo_docker_pro.txt
EXPOSE 5027
CMD ["uvicorn", "--proxy-headers", "app:app", "--host", "0.0.0.0", "--port", "5027", "--workers","1", "--reload"]