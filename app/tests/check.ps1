#!pwsh

..\venv\Scripts\Activate.ps1
    # Perform static type analysis.
    mypy --strict ..\exercises\pdfinfo_mapping\completed ..\templates

    # Run unit tests.
    pytest --log-level=DEBUG
deactivate
