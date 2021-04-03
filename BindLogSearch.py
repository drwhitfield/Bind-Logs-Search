#/usr/bin/python

"""

DESCRIPTION:    Script to quickly perform bulk pattern matching against set of files in directory
USAGE:          'python bindlogsearch.py'

"""

__author__='Donald R. Whitfield'
__status__='Development'
__copyright__='S-Box Security, LLC'



import re
import os
import glob


keyword = raw_input("Search For: ")
output_filename = '/tmp/output.txt'

with open(output_filename, "w") as out_file:
        root_dir = "/var/log/named"
        for root, dirs, files in os.walk(root_dir, onerror=None):
                for filename in files:
                        file_path = os.path.join(root, filename)
                        try:
                                with open(file_path, "rb") as f:
                                        for line in f:
                                                if keyword in line: #search for keyword
                                                        print(line)  # print the matching line
                                                        out_file.write(line)
                        except (IOError, OSError):  # ignore read and permission errors
                                pass



