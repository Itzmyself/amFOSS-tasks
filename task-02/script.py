import pytesseract 
from PIL import Image

def evaluate_expression(image_path):
    image = Image.open(image_path)

    extracted_text = pytesseract.image_to_string(image, config='--psm 7')

    expression = extracted_text.strip()

    try:
        result = eval(expression)
        return f"Expression: {expression}, Result: {result}"
    except Exception as e:
        return f"Error interpreting the expression: {e}"

image_path = "/home/itzmyself/amFOSS_tasks/task-02/arithmetic_expression.png"  # Replace with your image path
print(evaluate_expression(image_path))
