#! /bin/bash
# usage : tree [TARGET_PATH] -J | ./filter.sh
jq . -c | python3 filter.py
