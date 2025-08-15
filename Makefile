.PHONY: install test ui docker

install:
	pip install -r requirements.txt

test:
	pytest -q

ui:
	streamlit run ui/app.py

docker:
	docker build -t oddsbot .
