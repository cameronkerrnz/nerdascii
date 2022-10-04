#!/bin/sh

# Pretend this gets added in iteration1
#
#   ... but what happens when I want to run this on Windows now?

# Not sure how this is versioned
# File format: https://onnx.ai/

if [ \! -f ./cache/u2net.onnx ]; then
    echo "Downloading AI model for background removal"
    curl -o ./cache/u2net.onnx https://drive.google.com/uc?id=1tCU5MM1LhRgGou5OpmpjBQbSrYIUoYab
fi

docker build -f Dockerfile.iteration1 -t "nerdascii:latest" .
