"""Read and cache directory listings.

The listdir() routine returns a sorted list of the files in a directory,
using a cache to avoid reading the directory more often than necessary.
The annotate() routine appends slashes to directories."""
from warnings import warnpy3k
warnpy3k("the dircache module has been removed in Python 3.0", stacklevel=2)
del warnpy3k

import os

__all__ = ["listdir", "opendir", "annotate", "reset"]

cache = {}

def reset():
    """Reset the cache completely."""
    global cache
    cache = {}

def listdir(path):
    """List directory contents, using cache."""
    try:
        cached_mtime, list = cache[path]
        del cache[path]
    except KeyError:
        cached_mtime, list = -1, []
    mtime = os.stat(path).st_mtime
    if mtime != cached_mtime:
        list = os.listdir(path)
        list.sort()
    cache[path] = mtime, list
    return list

opendir = listdir # XXX backward compatibility

def annotate(head, list):
    """Add '/' suffixes to directories."""
    for i in xrange(len(list)):
        if os.path.isdir(os.path.join(head, list[i])):
            list[i] = list[i] + '/'
