PACKAGE := "antel_f660_bruteforce.py"

install:
	python -m venv .venv
	.venv/bin/pip install -r requirements.txt
	.venv/bin/pip install -e .

lint:
	make install
	.venv/bin/pip install -r requirements.dev.txt
	.venv/bin/black $(PACKAGE)
	.venv/bin/flakeheaven lint $(PACKAGE)
	.venv/bin/mypy $(PACKAGE)