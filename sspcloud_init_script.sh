#!/bin/sh

# Install packages and VSCode extensions
# Expected parameters : None

pip install black==25.1.0 mypy==1.17.0 pytest==8.4.1 pytest-cov==6.2.1 ruff==0.12.4

code-server --install-extension charliermarsh.ruff@2026.34.0  # Ruff
code-server --install-extension ms-python.mypy-type-checker@2025.2.0  # Mypy
code-server --install-extension LittleFoxTeam.vscode-python-test-adapter@0.8.2  # Python Test Explorer
code-server --install-extension ms-python.black-formatter@2025.2.0  # Black
code-server --uninstall-extension ms-python.flake8  # Flake8
