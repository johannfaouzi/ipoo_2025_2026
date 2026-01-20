#!/bin/sh

# Install packages and VSCode extensions
# Expected parameters : None

pip install black==25.1.0 mypy==1.17.0 pytest==8.4.1 pytest-cov==6.2.1 ruff==0.12.4

code-server --install-extension charliermarsh.ruff  # Ruff
code-server --install-extension ms-python.mypy-type-checker  # Mypy
code-server --install-extension LittleFoxTeam.vscode-python-test-adapter  # Python Test Explorer
code-server --install-extension ms-python.black-formatter  # Black
code-server --uninstall-extension ms-python.flake8  # Flake8
