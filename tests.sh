#!/bin/bash

pytest --cache-clear --junitxml=pytest.xml --cov=server server/ | tee pytest-coverage.txt
