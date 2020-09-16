Aiohttp Cache Benchmark
=======================

A simple benchmark test to check cache performance with Python Asyncio, Aiohttp and Uvloop.

Install
-------

Make sure you have Python >=3.7, create a [virtualenv](https://virtualenv.pypa.io/en/latest/)
and execute:

```
make requirements-dev
```

[Install K6](https://k6.io/docs/getting-started/installation#linux) to execute load tests.

Run
---

Execute:

```
make run W=2
```

The `W` parameter define the number of [Gunicorn Workers](https://docs.gunicorn.org/en/stable/run.html#commands).

Tests
-----

To execute tests:

```
make test
```

To execute a specific test:

```
make test-matching Q=<test_name>
```

To check coverage:

```
make test-coverage
```
