## APPROACH
First I downloaded a image.png which has the arithmetic expression "2+2". Then to create a Python script to read the image, extract the text, and evaluate the expression, I downloaded the following librabries and packages:
1. **Install Tesseract OCR**
        <br>
        Command -> ``sudo apt install tesseract-ocr``
        <br>
        OCR (Optical Character Recognition) is used to read the text from the image.

2. **Install Python Libraries** (Pillow and pytesseract)
    <br>
    We will need the Python pytesseract library for OCR and Pillow for image handling.
    But for installing these two packages, virtual environment method is more better.
    <br>
    So the commands are:
    * Create a Virtual Environment ``python3 -m venv myenv``
    * Activate the Virtual Environment ``source myenv/bin/activate``
    * Install the Required Packages(inside the Environment) ``pip install pytesseract pillow``
    * Run the Script ``python3 <file name>``
    * When you're done, deactivate the virtual environment ``deactivate``


