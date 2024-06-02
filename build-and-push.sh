#!/usr/bin/env sh

docker buildx create --use

docker buildx build \
	--platform linux/arm64/v8,linux/amd64 \
	-t matthewwright/external-ip-checker:latest \
	--push \
	.
