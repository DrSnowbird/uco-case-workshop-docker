import argparse
import sys

import case_utils
from case_utils.namespace import NS_RDF, NS_UCO_CORE, NS_UCO_IDENTITY, NS_XSD
from rdflib import Graph, Literal, Namespace


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output_path")
    args = parser.parse_args()

    NS_KB = Namespace("http://example.org/kb/")

    g: Graph = Graph()
    g.bind("kb", NS_KB)
    g.bind("uco-core", NS_UCO_CORE)
    g.bind("uco-identity", NS_UCO_IDENTITY)

    g.add(
        (
            NS_KB["organization-e9e85a45-b618-4e1b-a726-4b6f08ba1d68"],
            NS_RDF.type,
            NS_UCO_IDENTITY.Organization,
        )
    )
    g.add(
        (
            NS_KB["organization-e9e85a45-b618-4e1b-a726-4b6f08ba1d68"],
            NS_UCO_CORE.name,
            Literal("Cyber Domain Ontology", datatype=NS_XSD.string),
        )
    )

    # Write the CASE graph to a file
    try:
        with open(args.output_path, "w") as case_file:
            case_file.write(g.serialize(format="json-ld", indent=4))
            print(f"CASE graph exported to: {args.output_path}")
    except IOError:
        print(f"Error writing to path: {args.output_path}")
        raise


if __name__ == "__main__":
    main()
