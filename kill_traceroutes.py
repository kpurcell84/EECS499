#!/bin/bash

ps aux | grep "python traceroute_test.py" | awk {'print $2'} | xargs kill
