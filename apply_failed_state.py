#!/usr/local/bin/python
# How to use
# $ ./update_state.sh

import os
import re
import sys
import glob
import fnmatch
import json

delimeter_line=re.compile("^--")

def find_files(directory, pattern):
	ret_files = []
	for root, dirs, files in os.walk(directory):
		for basename in files:
			if fnmatch.fnmatch(basename, pattern):
				path = os.path.join(root, basename)
				ret_files.append(path)
	return ret_files

filename=sys.argv[1]
with open(filename) as f:
	test_filename=""
	test_fork=""
	test_idx=0
	for line in f:
		if delimeter_line.match(line):
			pass
		elif len(test_filename) == 0:
			m = re.search("--- FAIL: TestState/.*/(.*\.json)/([0-9a-zA-Z]+)/([0-9]+) \(.*", line)
			test_filename = m.group(1)
			test_fork = m.group(2)
			test_idx = int(m.group(3))
			files = find_files(".", test_filename)
			if len(files) != 1:
				m = re.search("--- FAIL: TestState/.*?([^/]*/.*\.json)/([0-9a-zA-Z]+)/([0-9]+) \(.*", line)
				filenameWithPath = m.group(1)
				filesSecond = []
				for fi in files:
					if re.search(".*%s" % (filenameWithPath), fi) is not None:
						filesSecond.append(fi)
				if len(filesSecond) != 1:
					print "Filename %s matched multiple times. %s" % (test_filename, files)
					exit(0)
				files = filesSecond
			test_filename = files[0]
		else:
			m = re.search("^.*got ([0-9a-zA-Z]+), want ([0-9a-zA-z]+)", line)
			got = m.group(1)
			want = m.group(2)
			print "Processing file %s..." % (test_filename)
			content = ""
			new_content = ""
			with open(test_filename) as jsonf:
				matched_hash = 0
				matched_logs = 0
				for jsonl in jsonf:
					if re.match("^\s+\"hash\"\s*:", jsonl):
						if matched_hash == test_idx:
							jsonl = re.sub(want, got, jsonl)
						matched_hash += 1
					elif re.match("^\s+\"logs\"\s*:", jsonl):
						if matched_logs == test_idx:
							jsonl = re.sub(want, got, jsonl)
						matched_logs += 1

					new_content += jsonl

			with open(test_filename, "w") as jsonf:
				jsonf.write(new_content)
			test_filename=""
