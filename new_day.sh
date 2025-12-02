#!/bin/bash

ROOT=$(dirname "${BASH_SOURCE[0]}")
YEAR=2025
DAY=$1

if [ -z "${DAY}" ]; then
	echo "Missing day input; ex. \"new_day.sh 1\""
	exit 1
fi

DIR="${ROOT}/${YEAR}/${DAY}"

if [ -f "${DIR}/day${DAY}.py" ]; then
    echo "Source for day ${DAY} already exists!"
    exit 1
fi

mkdir -p "$DIR"

cp "${ROOT}/template.py" "${DIR}/day${DAY}.py"

chmod +x "${DIR}/day${DAY}.py"

bash "${ROOT}/pull_input.sh" "${DAY}"
