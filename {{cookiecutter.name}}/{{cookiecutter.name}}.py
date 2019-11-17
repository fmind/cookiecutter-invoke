"""Tasks of the project."""

from invoke import task

from pathlib import Path

@task
def venv(c, force=False):
    """Create a virtual environment."""
    if not Path("venv").exists() or force:
        c.run("python3 -m venv venv --clear")
    c.run("venv/bin/pip install --editable .")
    c.run("venv/bin/pip install -r requirements.txt")