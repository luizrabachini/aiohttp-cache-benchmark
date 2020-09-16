run:
	@gunicorn aiohttp_cache_benchmark:app --bind localhost:8080 --workers ${W} --worker-class aiohttp.worker.GunicornUVLoopWebWorker -e SIMPLE_SETTINGS=aiohttp_cache_benchmark.settings.development --capture-output --log-level debug

run-k6-aioredis:
	@k6 run --vus 8 --duration 30s k6/aioredis.js --rps 80

clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name ".cache" -type d | xargs rm -rf

requirements-test:
	@pip install -r requirements/test.txt

requirements-dev:
	@pip install -r requirements/dev.txt

test:
	@SIMPLE_SETTINGS=aiohttp_cache_benchmark.settings.test py.test aiohttp_cache_benchmark

test-matching:
	@SIMPLE_SETTINGS=aiohttp_cache_benchmark.settings.test pytest -rxs -k${Q} aiohttp_cache_benchmark

test-coverage:
	@SIMPLE_SETTINGS=aiohttp_cache_benchmark.settings.test pytest --cov=aiohttp_cache_benchmark aiohttp_cache_benchmark --cov-report term-missing

lint:
	@flake8
	@isort --check

detect-outdated-dependencies:
	@sh -c 'output=$$(pip list --outdated); echo "$$output"; test -z "$$output"'
