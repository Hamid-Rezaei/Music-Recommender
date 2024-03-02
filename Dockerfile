FROM python:3.11

LABEL authors="hamid"

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100


# Copy only requirements to cache them in docker layer
WORKDIR /code
ENV PYTHONPATH "${PYTHONPATH}:/your/custom/path"

# Project initialization and System Dependecy:
RUN pip install --upgrade pip


COPY requirements.txt /code/

RUN pip install -r requirements.txt

# Creating folders, and files for a project:
COPY . /code

CMD ["sh", "entrypoint.sh" ]
