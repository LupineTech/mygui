@echo off
REM Check if we are in the correct directory
if not exist setup.py (
    echo setup.py not found. Please run this batch file from the project root.
    exit /b 1
)

REM Create a source distribution
python setup.py sdist

REM Create a wheel distribution
python setup.py bdist_wheel

echo Package built successfully.

twine upload dist/* --verbose
pause