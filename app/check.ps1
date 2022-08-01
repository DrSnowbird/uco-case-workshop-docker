#!pwsh

# Guarantee submodules are initialized.
git submodule update --init

# Create virtual environment, if not yet created.
if (-Not (Test-Path -Path 'venv')) {
    python3 -m venv venv
    #.\venv\Scripts\Activate.ps1
        #pip install --upgrade pip setuptools wheel
        pip install --requirement requirements.txt
    #deactivate
}

# Run tests within tests/ directory.
Push-Location tests
    .\check.ps1
Pop-Location
