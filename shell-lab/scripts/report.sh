#!/usr/bin/env bash
# Print how many data rows each raw CSV contains (header excluded).
for f in data/raw/*.csv; do
  rows=$(($(wc -l < "$f") - 1))
  echo "$f: $rows rows"
done
