#!/usr/bin/env sh

pyinstaller --noconfirm \
 --onefile \
 thor_alerts/__main__.py \
 --add-data="thor_alerts/icons.json":"." \
 --add-data="thor_alerts/assets/icons":"assets/icons" \
 --hiddenimport=desktop_notifier.resources
