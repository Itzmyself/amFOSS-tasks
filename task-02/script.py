import pytesseract 
from PIL import Image

def evaluate_expression(image_path):
    # Load the image
    image = Image.open(image_path)

    # Use OCR to extract text
    extracted_text = pytesseract.image_to_string(image, config='--psm 7')

    # Clean the extracted text
    expression = extracted_text.strip()

    try:
        # Evaluate the expression
        result = eval(expression)
        return f"Expression: {expression}, Result: {result}"
    except Exception as e:
        return f"Error interpreting the expression: {e}"

# Example usage
image_path = "/home/itzmyself/amFOSS_tasks/task-02/arithmetic_expression.png"  # Replace with your image path
print(evaluate_expression(image_path))
