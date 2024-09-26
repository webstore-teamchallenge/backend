FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache bash
WORKDIR /code/

COPY /requirements/ /code/requirements/
RUN pip install --no-cache-dir -r requirements/local.txt

COPY . /code/

EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# RUN chmod +x /code/Docker/local/entrypoint.sh


# ENTRYPOINT ["/code/Docker/local/entrypoint.sh"]