dbuild:
	docker build -t opening_hours .

drun:
	docker run -it -p 5000:5000 opening_hours

test:
	curl -X POST --header 'Content-Type: application/json' \
		-d @data/schedule2.json http://localhost:5000/open-hours