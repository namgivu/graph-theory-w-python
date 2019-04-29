#!/usr/bin/env bash
s=$BASH_SOURCE ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ; SCRIPT_HOME="$s" # get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path

export PYTHONPATH="$SCRIPT_HOME:$PYTHONPATH"; pipenv run pytest -x -n2
