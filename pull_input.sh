#!/bin/bash

YEAR="2025"
ROOT=$(dirname ${BASH_SOURCE[0]})

DAY=$1

if [ ! -f "${ROOT}/cookie.txt" ]; then
	echo "Missing cookie.txt"
	exit 1
fi

if [ -z "${DAY}" ]; then
	echo "Missing day input"
	exit 1
fi

if [ -f "${ROOT}/${YEAR}/${DAY}/input.txt" ]; then
	echo "Input file already exists: ${ROOT}/${YEAR}/${DAY}/input.txt"
	exit 1
fi

curl --cookie "${ROOT}/cookie.txt" "https://adventofcode.com/${YEAR}/day/${DAY}/input" > "${ROOT}/${YEAR}/${DAY}/input.txt"
