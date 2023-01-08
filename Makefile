lint:
	mypy app main.py
	flake8 app main.py

lint-report:
	mypy app main.py >> ./lint_report.txt
	flake8 app main.py >> ./lint_report.txt