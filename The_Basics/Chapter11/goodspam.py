#! /usr/bin/env python

import string
times = "MORNING:EVENING:AFTERNOON"
periods = string.split(times, ":")
print "Good---", periods[1]
