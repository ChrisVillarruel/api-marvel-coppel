FROM python:3.10
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /code

EXPOSE 90

# Servicio Backend
CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "90", "--reload"]

