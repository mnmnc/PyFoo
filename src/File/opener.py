
def open_file(filename, mode):
	# 'r'       open for reading (default)
    # 'w'       open for writing, truncating the file first
    # 'x'       create a new file and open it for writing
    # 'a'       open for writing, appending to the end of the file if it exists
    # 'b'       binary mode
    # 't'       text mode (default)
    # '+'       open a disk file for updating (reading and writing)
    # 'U'       universal newline mode (for backwards compatibility; unneeded
    #           for new code)
	of = open(filename, mode)
	return of

def open_read(filename):
	return open(filename, 'r')

def open_write(filename):
	return open(filename, 'w')

def open_create_write(filename):
	return open(filename, 'x')

def open_append(filename):
	return open(filename, 'a')

def open_binary(filename):
	return open(filename, 'b')

def open_text(filename):
	return open(filename, 'b')