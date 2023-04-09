FROM python:3.9

WORKDIR /var/www

# pipenv
RUN pip install pipenv
COPY ./Pipfile ./Pipfile.lock /var/www/
# RUN pipenv sync
RUN pipenv sync --dev

COPY ./* /var/www/

CMD bash
