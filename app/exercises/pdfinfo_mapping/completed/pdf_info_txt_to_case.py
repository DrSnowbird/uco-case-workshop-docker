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
from typing import Any, Dict, Optional, TextIO
from uuid import uuid4

from case_utils.namespace import NS_RDF, NS_UCO_CORE, NS_UCO_OBSERVABLE, NS_XSD
from rdflib import BNode, Graph, IdentifiedNode, Literal, Namespace, URIRef
from rdflib.util import guess_format


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--unmapped-txt", help="Optional secondary output, where unmapped data is written.")
    parser.add_argument("output_path", help="CASE format will be guessed based on file extension.")
    parser.add_argument("input_txt")
    args = parser.parse_args()

    # Guess output format before doing work.
    output_format = guess_format(args.output_path)
    assert output_format is not None

    unmapped_fh: Optional[TextIO] = None
    if args.unmapped_txt:
        unmapped_fh = open(args.unmapped_txt, "w")

    # Initialize CASE graph.
    graph = Graph()
    NS_KB = Namespace("http://example.org/kb/")
    graph.bind("kb", NS_KB)
    graph.bind("uco-core", NS_UCO_CORE)
    graph.bind("uco-observable", NS_UCO_OBSERVABLE)

    # Add 'drafting' namespace for concepts not found in UCO.
    NS_DRAFTING = Namespace("http://example.org/ontology/drafting/")
    graph.bind("drafting", NS_DRAFTING)

    # Initialize and type-designate the file node.
    n_pdf_file: IdentifiedNode = NS_KB["pdf-file-" + str(uuid4())]
    graph.add((n_pdf_file, NS_RDF.type, NS_UCO_OBSERVABLE.PDFFile))

    # Initialize and attach PDF file facet.
    n_pdf_file_facet: IdentifiedNode = BNode()
    graph.add((n_pdf_file_facet, NS_RDF.type, NS_UCO_OBSERVABLE.PDFFileFacet))
    graph.add((n_pdf_file, NS_UCO_CORE.hasFacet, n_pdf_file_facet))

    # Read input data.
    with open(args.input_txt, "r") as input_fh:
        for input_line in input_fh:
            # Parse input data.
            # Reassemble input_value in case right column contains colons (e.g. in timestamps).
            input_line_parts = input_line.split(":")
            input_key = input_line_parts[0]
            input_value = ":".join(input_line_parts[1:]).strip()

            # Assign these two values on encountering a key where a mapping is known.
            n_input_literal_datatype: Optional[URIRef] = None
            n_mapped_property: Optional[URIRef] = None

            if input_key == "Title":
                n_input_literal_datatype = NS_XSD.string
                n_mapped_property = NS_DRAFTING.pdfTitle
            elif input_key == "Author":
                n_input_literal_datatype = NS_XSD.string
                n_mapped_property = NS_DRAFTING.pdfAuthor
            elif input_key == "CreationDate":
                n_input_literal_datatype = NS_XSD.dateTime
                n_mapped_property = NS_DRAFTING.pdfCreationDate
            elif input_key == "ModDate":
                n_input_literal_datatype = NS_XSD.dateTime
                n_mapped_property = NS_DRAFTING.pdfModifiedDate
            elif input_key == "PDF version":
                n_input_literal_datatype = NS_XSD.string
                n_mapped_property = NS_UCO_OBSERVABLE.version

            if n_mapped_property is None:
                if unmapped_fh:
                    unmapped_fh.write(input_line)
            else:
                if n_input_literal_datatype is not None:
                    l_input_value = Literal(input_value, datatype=n_input_literal_datatype)
                    graph.add((n_pdf_file_facet, n_mapped_property, l_input_value))

    # Clean up secondary file handle, if initialized.
    if unmapped_fh is not None:
        unmapped_fh.close()

    # Write the CASE graph to a file.
    serialize_kwargs: Dict[str, Any] = {
        "format": output_format
    }
    if output_format == "json-ld":
        context_dictionary: Dict[str, Any] = {
            "drafting": NS_DRAFTING,
            "kb": NS_KB,
            "uco-core": NS_UCO_CORE,
            "uco-observable": NS_UCO_OBSERVABLE,
            "xsd": str(NS_XSD)
        }
        serialize_kwargs["context"] = context_dictionary
        
    graph.serialize(args.output_path, **serialize_kwargs)

if __name__ == "__main__":
    main()
