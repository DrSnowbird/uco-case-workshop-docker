#!pwsh

..\..\..\venv\Scripts\Activate.ps1
  # Do static type review before running code.
  # For those interested: Use --strict flag on mypy.
  mypy .

  # Build mapped file.
  python3 pdf_info_txt_to_case.py --unmapped-txt 000015.pdf.pdfinfo-isodates.txt.mapped_with_rdflib.unmapped.txt 000015.pdf.pdfinfo-isodates.txt.mapped_with_rdflib.json 000015.pdf.pdfinfo-isodates.txt

  # Validate mapped file.
  case_validate 000015.pdf.pdfinfo-isodates.txt.mapped_with_rdflib.json

deactivate
