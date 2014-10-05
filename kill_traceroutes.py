#!/bin/bash

ps aux | grep "python traceroute_test*" | awk {'print $2'} | xargs kill