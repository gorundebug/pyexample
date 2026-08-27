#!/bin/sh
set -eu

source_dir="${1:?source directory is required}"
work_dir="${2:?work directory is required}"

test -f "$source_dir/pyproject.toml"
work_parent="$(dirname "$work_dir")"
mkdir -p "$work_parent"
cd "$work_parent"
rm -rf "$work_dir"
mkdir -p "$work_dir"
cp -a "$source_dir/." "$work_dir/"