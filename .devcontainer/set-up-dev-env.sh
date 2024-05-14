#!/bin/bash
set -euxo pipefail

poetry completions bash >> ~/.bash_completion
poetry install
poetry run pre-commit install
