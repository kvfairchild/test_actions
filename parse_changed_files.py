import logging
import sys

PLUGIN_DIRS = ['benchmarks', 'data', 'models', 'metrics']

changed_files = sys.argv[1]
plugin_files_changed = []
non_plugin_files_changed = []
for f in changed_files:
	if not any(plugin_dir in f for plugin_dir in PLUGIN_DIRS):
    	print(f)
    	non_plugin_files_changed.append(f)
    else:
    	print(f"plugin file {f} changed")
    	plugin_files_changed.append(f)

if len(non_plugin_files_changed) > 0:
	print("stop")
else:
	print("continue")