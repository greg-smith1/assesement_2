#!/usr/bin/env bash

#nohup python3 run/wsgi.py &

# Set-up
rm -rf run/instance
rm run/datastore/master.db
python3 setup/schema.py
python3 setup/seed.py
#python3 setup/text_cleaning.py

# Runtime
#python3 run/wsgi.py


# Clean up
rm -rf core/controllers/__pycache__
rm -rf core/__pycache__
