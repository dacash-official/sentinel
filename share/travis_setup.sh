#!/bin/bash
set -evx

mkdir ~/.dacashcore

# safety check
if [ ! -f ~/.dacashcore/dacash.conf ]; then
  cp share/dacash.conf.example ~/.dacashcore/dacash.conf
fi
