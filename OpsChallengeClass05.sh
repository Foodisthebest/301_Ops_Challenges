#!/bin/bash

# use the stat command to check the size of the /var/log/syslog and 
# /var/log/wtmp files

syslog_size=$(stat -c%s /var/log/syslog)
wtmp_size=$(stat -c%s /var/log/wtmp)

# Use the gzip command to compress each log file
# -c option tells gzip to compress the data and print it to the standard output
# compresses files with timestamp in the name

gzip -c /var/log/syslog > /var/log/backups/syslog-$(date +%Y%m%d%H%M%S).zip
gzip -c /var/log/wtmp > /var/log/backups/wtmp-$(date +%Y%m%d%H%M%S).zip

# use the truncate -s 0 command to clear the contents of 
# both original log files

truncate -s 0 /var/log/syslog
truncate -s 0 /var/log/wtmp

# These lines use the stat command again to check 
# the size of the compressed files
# stores the number of files in two new variables: 
# syslog_compressed_size and wtmp_compressed_size

syslog_compressed_size=$(stat -c%s /var/log/backups/syslog-$(date +%Y%m%d%H%M%S).zip)
wtmp_compressed_size=$(stat -c%s /var/log/backups/wtmp-$(date +%Y%m%d%H%M%S).zip)

# Lines that calculate the percentage reduction in size for each log file
# syslog_reduction and wtmp_reduction are where the results of the reduction are stored

syslog_reduction=$((100 * ($syslog_size - $syslog_compressed_size) / $syslog_size))
wtmp_reduction=$((100 * ($wtmp_size - $wtmp_compressed_size) / $wtmp_size))

# Prints the following:
    # Original size of each log file
    # The compressed size of each log file
    # Percentage reduction in size for each log file
    
echo "Original syslog size: $syslog_size bytes"
echo "Compressed syslog size: $syslog_compressed_size bytes"
echo "Reduction: $syslog_reduction%"
echo ""
echo "Original wtmp size: $wtmp_size bytes"
echo "Compressed wtmp size: $wtmp_compressed_size bytes"
echo "Reduction: $wtmp_reduction%"
