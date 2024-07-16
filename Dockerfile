FROM python:3.9-slim

WORKDIR /app

COPY requirements/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN pip install gunicorn

ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.settings

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]
