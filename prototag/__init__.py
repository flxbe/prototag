#!/usr/bin/env python
"""
Prototag

Usage:
    ptag [options] [<dir>]

Options:
    -h --help
    -v --version
    -t <selector>, --tag <selector>
    -a <selector>, --author <selector>

Selectors:
    One can use logical AND and OR conditions to filter the found files with
    valid headers. AND terms are combined using `,` and OR terms are
    combined using `:`. OR terms are evaluated before AND terms. The OR
    conditions are not exclusive

    tag1,tag2       Select all files, that have both tag1 and tag2.
    tag1:tag2       Select all files, that have at least one of both tags.
    tag1,tag2:tag3  Select all files, that have either tag1 and tag2 or tag3
                    or both.

Examples:
    ptag                    List all files with a valid header in the cwd.
    ptag -t idea ./dir      Find all files with the tag 'idea' in ./dir
    ptag -t idea,python     Find all files with the tags 'idea' and 'python'.
    ptag -t idea:python     Find all files with the tags 'idea' and/or 'python'.

Description:
    Filter all .md files in a directory by values in a comment header.
"""
from __future__ import print_function
import os

from docopt import docopt

import prototag.prototag as pt
import prototag.selector as selector

__version__ = '0.1.1'


def main():
    """main
    """
    options = docopt(__doc__)

    if options['--version']:
        print(__version__)
        return

    if options['<dir>'] is not None:
        srcdir = options['<dir>']
    else:
        srcdir = '.'

    selectors = {
        'tag': options['--tag'],
        'author': options['--author']
    }

    results = pt.read_directory(srcdir)
    results = selector.select_results(results, selectors)

    filenames = [os.path.basename(f) for f, _ in results]
    filenames.sort()

    for filename in filenames:
        print(filename)
