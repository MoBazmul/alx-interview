#!/usr/bin/python3

import sys
import re
from collections import defaultdict

def process_line(line, stats):
    """Process each line and update the statistics."""
    log_pattern = re.compile(
        r'^(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'
    )
    match = log_pattern.match(line)
    
    if match:
        status_code = match.group(3)
        file_size = int(match.group(4))
        
        stats['total_size'] += file_size
        
        if status_code in stats['status_codes']:
            stats['status_codes'][status_code] += 1
        else:
            stats['status_codes'][status_code] = 1

def print_stats(stats):
    """Print the accumulated statistics."""
    print(f"File size: {stats['total_size']}")
    for code in sorted(stats['status_codes']):
        print(f"{code}: {stats['status_codes'][code]}")
