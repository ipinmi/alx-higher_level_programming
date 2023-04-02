#!/bin/bash
#sends a JSON POST request to a URL passed as the first argument,
# and displays the body of the response.
curl -s -H "Content-type: application/json" -d @"$2" -X POST "$1"
