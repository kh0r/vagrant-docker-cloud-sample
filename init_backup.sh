#!/bin/bash

gem install fakes3

if crontab -l | grep '@reboot (fakes3 -r /tmp/fakes3 -p 4567 > file 2>&1 &)'; then
  echo crontab already installed
else
  (crontab -l 2>/dev/null; echo "@reboot (fakes3 -r /tmp/fakes3 -p 4567 > file 2>&1 &)") | crontab -
  echo crontab installed
  echo Rebooting....
  reboot
fi
