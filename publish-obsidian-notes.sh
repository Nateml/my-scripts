#!/bin/bash

QUARTZDIR=$HOME/quartz
VAULTDIR="$HOME/Documents/Knowledge Base"

rm -r $QUARTZDIR/content/*
cp -r "$VAULTDIR"/* $QUARTZDIR/content/
find $QUARTZDIR/content/. -name '*.md' ! -type d -exec bash -c 'expand -t 4 "$0" > /tmp/e && mv /tmp/e "$0"' {} \;
cd $QUARTZDIR
hugo-obsidian -input=content -output=data -index=true
hugo
cd public
git add --all
git commit -m "added new content from vault via bash script (via bash script)"
git push origin main

