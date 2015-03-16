# -*- coding: utf-8 -*-

"""Provides functions that parse CLI options into suitable internal data structures."""

import re
import sys


def parse_options():
    """Tries to parse admissible options.

    Returns:
        Dictionary with parsed values for all admissible optional CLI parameters
    """
    options_dict = {'join_pages': False}

    if len(sys.argv[1:]) == 4:
        for arg in sys.argv[1:]:
            if arg == "-j" or arg == "--join":
                options_dict['join_pages'] = True

    return options_dict


def parse_range_list(range_list):
    """Parses a given string that represents a list of ranges. The format of the list
       adheres to the following format:

               range_list := {FROM_PAGE}-{TO_PAGE}[,{FROM_PAGE}-{TO_PAGE}]*

       Arguments:
           range_list    --    String value representing the range list

       Returns:
           List of single page ranges, e.g. "7-9"
    """
    pattern = "([0-9]+-[0-9]+)"
    matcher = re.compile(pattern)
    result = matcher.findall(range_list)
    if result is None:
        result = []
    return result