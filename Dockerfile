FROM python:3.10-buster 
ENV PYTHONUNBUFFERED=1

WORKDIR /src 

ARG USER_NAME=vscode 
ARG UID=1000
ARG GID=$UID 

RUN groupadd --gid $GID $USER_NAME \
  && useradd --uid $UID --gid=$GID -m $USER_NAME \
  && apt-get update \
  && apt-get install -y sudo \
  && echo $USER_NAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USER_NAME \
  && chmod 0440 /etc/sudoers.d/$USER_NAME 

COPY pyproject.toml* poetry.lock* ./
RUN pip install --upgrade pip \
  && pip install poetry \
  && poetry config virtualenvs.in-project true \
  && if [ f pyproject.toml ]; then poetry install; fi \
  && pip cache purge 