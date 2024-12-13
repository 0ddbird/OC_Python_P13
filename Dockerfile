FROM python:3.11-slim

WORKDIR /app

COPY requirements/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.settings

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
