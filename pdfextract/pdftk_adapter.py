# -*- coding: utf-8 -*-

"""Provides the means to extract PDF pages (multiple ranges) from
a source PDF using PDFTK as an external tool."""

import os
import sys

PDFTK_EXTRACT_CMD = "pdftk A=%s cat A%s output %s"
PDFTK_JOIN_CMD = "pdftk %s cat output %s"


def extract_pdf_pages(source_pdf, target_pdf, page_ranges, options):
    """Extracts the pages identified by the given ranges from source PDf
    to target PDF.

    Arguments:
        source_pdf      --      Represents the source PDF file
        target_pdf      --      Represents the target PDF file
        page_ranges     --      List with pages to be extracted from the source PDF file
        options         --      Dictionary with optional parameters and their values

    Returns:
        None
    """
    tmp_pdf_name_pattern = build_output_file_pattern(sys.argv[2])
    temporary_files = []
    for page_range in page_ranges:
        temporary_pdf_name = tmp_pdf_name_pattern % page_range
        cmd = PDFTK_EXTRACT_CMD % (source_pdf, page_range, temporary_pdf_name)
        print >>sys.stdout, "Extracting pages %s from %s..." % (page_range, source_pdf)
        os.system(cmd)
        temporary_files.append(temporary_pdf_name)

    if options['join_pages'] or len(page_ranges) == 1:
        cmd = PDFTK_JOIN_CMD % (" ".join(temporary_files), target_pdf)
        print >>sys.stdout, "Joining temporary PDF files..."
        os.system(cmd)
        for temporary_file in temporary_files:
            os.remove(temporary_file)

    print >> sys.stdout, "Job finished."


def build_output_file_pattern(out_fn):
    """Builds the string pattern "{OUTFN}-{PAGE_RANGE}.pdf". This is necessary
       if one wants to extract multiple page ranges and does not join the single
       results.

       Arguments:
            out_fn    --    Output filename

       Returns:
            String value which represents the filename pattern.
    """
    if len(out_fn.split(".")) >= 2:
        tokens = out_fn.split(".")
        outfile = "".join(tokens[0:len(tokens) - 1])
        return outfile + "-%s.pdf"
    else:
        return out_fn + "-%s.pdf"
