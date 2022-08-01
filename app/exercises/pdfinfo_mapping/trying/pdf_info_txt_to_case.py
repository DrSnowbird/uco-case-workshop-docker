#!/usr/bin/env python3

"""
This program converts the output of pdfinfo, using the -isodates flag, to CASE.

pdfinfo's output is known to follow a pattern of a two-column text file, with a colon delineating the columns.  E.g.:

    Title:          Document
    Subject:        Extracted Pages
    Author:         U.S. Government Printing Office
    (...)

This program emits a CASE graph to the provided output file.
"""

import argparse
from typing import Optional, TextIO


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--unmapped-txt",
        help="Optional secondary output, where unmapped data is written.",
    )
    parser.add_argument(
        "output_path", help="Expecting to end with extension .json or .jsonld."
    )
    parser.add_argument("input_txt")
    args = parser.parse_args()

    unmapped_fh: Optional[TextIO] = None
    if args.unmapped_txt:
        unmapped_fh = open(args.unmapped_txt, "w")

    # Use 'drafting' namespace for concepts not found in UCO.
    PREFIX_DRAFTING = "http://example.org/ontology/drafting/"

    raise NotImplementedError("TODO - set up dictionary.")

    # Read input data.
    with open(args.input_txt, "r") as input_fh:
        for input_line in input_fh:
            # Parse input data.
            # Reassemble input_value in case right column contains colons (e.g. in timestamps).
            input_line_parts = input_line.split(":")
            input_key = input_line_parts[0]
            input_value = ":".join(input_line_parts[1:]).strip()

        raise NotImplementedError("TODO - map keys and values into CASE.")

    # Clean up secondary file handle, if initialized.
    if unmapped_fh is not None:
        unmapped_fh.close()

    # Write the CASE graph to a file.


if __name__ == "__main__":
    main()
