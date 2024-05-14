FROM mcr.microsoft.com/devcontainers/python:1-3.10-bookworm

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive

USER vscode

# Install Poetry
ENV POETRY_VERSION=1.6.1
RUN curl -sSL https://install.python-poetry.org | python3 -

# Handy alias
RUN echo 'alias ll="ls --show-control-chars -F --color -la $*"' >> ~/.bash_aliases
