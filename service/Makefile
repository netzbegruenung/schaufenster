
build:
	docker build -t quay.io/netzbegruenung/schaufenster-service .

run:
	docker run -p 5000:5000 --rm quay.io/netzbegruenung/schaufenster-service

serve:
	gunicorn --reload -b 0.0.0.0:5000 api.main:app

test:
	pytest tests
