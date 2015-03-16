# -*- coding: utf-8 -*-

"""Provides the entry point of the PDFextract script."""

__author__ = 'Markus Günther <markus.guenther@gmail.com>'
__license__ = 'MIT License'
__version = '0.1.0'
__help__ = '''PDFextract v0.1.0

PDFextract is a convenient-to-use CLI wrapper for the pdftk tool which enables the user to easily extract multiple page
ranges from a PDF file.

Usage: pdfextract.py <source PDF> <target PDF> <page range(s)> [options]

<source PDF>    --      The source PDF file.
<target PDF>    --      The target PDF file. This is the file to which the extracted pages will be written to.
                        In case of multiple given page ranges, each page range is written to its own file unless
                        the user supplied the join parameter (-j, --join) to group them together into a single
                        target PDF.
<page range(s)> --      Comma-separated list of page ranges.

OPTIONS

-j, --join      --      Combines multiple target PDFs into a single target PDF (only admissible if multiple page
                        ranges were supplied).

EXAMPLES:

Extract pages 3 to 5 from file source.pdf to target.pdf:
    pdfextract.py source.pdf target.pdf 3-5

Extract pages 3-5 and 7-12 from source.pdf to target.pdf:
    pdfextract.py source.pdf target.pdf 3-5,7-12
    Yields both target PDF files target-3-5.pdf and target-7-12.pdf.

Extract pages 3-5 and 7-12 from source.pdf to target.pdf and join them:
    pdfextract.py source.pdf target.pdf 3-5,7-12 --join
    Yields the single target PDF file target.pdf.
'''.strip()

import os
import sys

from .parameter_parser import parse_options
from .parameter_parser import parse_range_list
from .pdftk_adapter import extract_pdf_pages
from .validation import is_program_installed


def main():

    if len(sys.argv[1:]) != 3 and len(sys.argv[1:]) != 4:
        fail("Wrong number of arguments.")

    if not is_program_installed("pdftk"):
        fail("This script requires PDFTK to run.")

    if not os.access(sys.argv[1], os.F_OK):
        fail("Source PDF is not accessible.")

    ranges = parse_range_list(sys.argv[3])

    if len(ranges) == 0:
        fail("No page range given.")

    source_pdf = sys.argv[1]
    target_pdf = sys.argv[2]

    extract_pdf_pages(source_pdf, target_pdf, ranges, parse_options())

def fail(message):
    '''Writes the given message to the stderr and the help to stdout.
    Terminates the script with exit code 1.
    '''
    print >>sys.stderr, "ERROR: %s" % message
    print >>sys.stdout, __help__
    sys.exit(1)