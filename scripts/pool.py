#!/usr/bin/env python

import os
import sys
import yaml
import subprocess

if len(sys.argv) != 3:
    print("Usage, python pool.py <destination> <yaml config>")
    sys.exit(1)

destination = sys.argv[1]
if not os.path.exists(destination):
    os.makedirs(destination)
elif len(os.listdir(destination)) != 0:
    print("Destination not empty")
    sys.exit(1)

config = sys.argv[2]
if not os.path.exists(config):
    print("Argument is not a file path")
    sys.exit(1)

with open(config, 'r') as stream:
    try:
        data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print("Invalid yaml format")
        sys.exit(1)

for entry in data:
    for tmp, v in entry.items():
        dest = os.path.join(destination, v["name"])
        subprocess.run(["git", "clone", tmp, dest])
        for t, dep in v["depends"].items():
            cmd = "./%s/scripts/dep.bash" % dest
            subprocess.run([cmd, dep, t])