"""Markdown cli filter.

Add tags to any markdown file using a comment header. This header can include
varaibles in the `yaml` format.
"""
import os

import yaml


def extract_md_header(file):
    """Extract the header from the input markdown file.

    Paramters
    ---------
    file : generator
        A generator that generates lines.

    Returns
    -------
    string | None
        The extracted header content or `None`.
    """
    first_line = True
    header_content = ""
    for line in file:
        if first_line:
            if line.strip() != "<!--":
                return None
            first_line = False
            continue

        if line.strip() == "-->":
            return header_content

        header_content += line

    return None


PARSERS = {
    '.md': extract_md_header
}


def extract_header(filename):
    """Extract the yaml variables from the header string.

    Paramter
    --------
    header : string
        The header content

    Returns
    -------
    dictionary
        The extracted variables.
    """
    # check file ending
    _, ext = os.path.splitext(filename)

    if ext not in PARSERS:
        return None

    file = open(filename)
    header = PARSERS[ext](file)
    file.close()

    if header is None:
        return None

    try:
        return yaml.load(header)
    except yaml.scanner.ScannerError:
        return None


def read_directory(path):
    """Read all files in a specified directory.

    Read every file and extract the markdown-header, if possible.

    Paramters
    ---------
    path : string
        The directory path.

    Returns
    -------
    array, shape(n,)
        An array containing a dictionary for every valid file.
    """
    filenames = os.listdir(path)
    filenames = [os.path.join(path, filename) for filename in filenames]
    headers = [extract_header(filename) for filename in filenames]
    result = zip(filenames, headers)
    result = [t for t in result if t[1] is not None]

    return result
