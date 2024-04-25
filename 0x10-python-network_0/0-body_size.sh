#!/bin/bash
# Get the HTTP response for a url
curl -s "$1" | wc -c
