FROM python:3.10-slim

WORKDIR /termes-account

COPY ./requirements.txt /termes-account/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /termes/requirements.txt

COPY ./src /termes-account/src

RUN export PYTHONPATH="$PYTHONPATH:/termes-account/src"

CMD ["python3", "-m", "account"]