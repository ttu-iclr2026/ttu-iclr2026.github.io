#!/bin/bash

set -xe

DOCKERNAME=shifthappens/sphinx
docker build -t $DOCKERNAME -f - docs << EOF
FROM sphinxdoc/sphinx:7.4.7
COPY requirements.txt .
RUN pip install --no-cache -r requirements.txt sphinx-autobuild
EOF

docker run \
    -p 127.0.0.1:8000:8000 \
    --rm \
    --user $(id -u) \
    -v $(pwd)/docs:/docs \
    -v $(pwd):/code \
    -e PYTHONPATH=/code \
    --env SPHINXBUILD=sphinx-autobuild \
    --env SPHINXOPTS="--port 8000 --host 0.0.0.0" \
    -it $DOCKERNAME make html
