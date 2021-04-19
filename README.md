# Restaurant Opening Hours

This is example of HTTP API service for converting JSON string with the opening hours into human readable format.

## Commands

All you need is python3 + docker environment. 

- First of all, build and run the docker container on 5000 port:
```bash
make dbuild
make drun
```
- Then you can test the API on http://localhost:5000:
```bash
make test
```
or send the POST request directly:
```bash
curl -X POST --header 'Content-Type: application/json' \
	-d '{"monday":[{"type":"close","value":3600}],"tuesday":[{"type":"open","value":36000},{"type":"close","value":64800}],"wednesday":[],"thursday":[{"type":"open","value":36000},{"type":"close","value":64800}],"friday":[{"type":"open","value":36000}],"saturday":[{"type":"close","value":3600},{"type":"open","value":36000}],"sunday":[{"type":"close","value":3600},{"type":"open","value":43200}]}' \
	http://localhost:5000/open-hours
```

- In return, you will get this response:
```text
Monday: Closed
Tuesday: 10 AM - 6 PM
Wednesday: Closed
Thursday: 10 AM - 6 PM
Friday: 10 AM - 1 AM
Saturday: 10 AM - 1 AM
Sunday: 12 PM - 1 AM
```
