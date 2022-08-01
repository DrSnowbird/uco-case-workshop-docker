#!pwsh

..\..\..\venv\Scripts\Activate.ps1
  # Do static type review before running code.
  # For those interested: Use --strict flag on mypy.
  mypy .

  # Build mapped file - JSON output.
  python3 pdf_info_txt_to_case.py --unmapped-txt 000015.pdf.pdfinfo-isodates.txt.mapped_with_rdflib.unmapped.txt 000015.pdf.pdfinfo-isodates.txt.mapped_with_rdflib.json 000015.pdf.pdfinfo-isodates.txt

  # Validate mapped JSON file.
  case_validate 000015.pdf.pdfinfo-isodates.txt.mapped_with_rdflib.json

  # Build mapped file - Turtle output.
  python3 pdf_info_txt_to_case.py --unmapped-txt 000015.pdf.pdfinfo-isodates.txt.mapped_with_rdflib.unmapped.txt  000015.pdf.pdfinfo-isodates.txt.mapped_with_rdflib.ttl 000015.pdf.pdfinfo-isodates.txt

  # Validate mapped Turtle file.
  case_validate 000015.pdf.pdfinfo-isodates.txt.mapped_with_rdflib.ttl

deactivate
