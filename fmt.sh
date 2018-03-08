#!/bin/sh

if [ -z ${1} ]
then
  echo "Please enter file name"
  exit 1
fi

echo "formatting file $1 ..."
yapf --in-place --style='{based_on_style: chromium, indent_width: 2}' $1

echo "formatted file $1"

exit 0
