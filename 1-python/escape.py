#!/usr/bin/env python
import string, sys

#
# Escape simple quote an backslashes in the given string
#
def escape(str):
    # First replace backslashes to not interfer with quote escaping
    # backslashes
    return escape_quotes(escape_backslashes(str))
#
# Escape backslashes
#
def escape_backslashes(str):
    return string.replace(str, "\\", r"\\")

#
# Escape quotes
#
def escape_quotes(str):
    return string.replace(str, "'", r"\'")

#
# Main script
#
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("""Usage: escape.py \"STRING\"""")
        sys.exit(0)

    print(escape(sys.argv[1]))
