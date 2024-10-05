import re
import random
import sys
import getopt
from sympy import sympify, latex

# ANSI escape codes for bold text
BOLD = "\033[1m"
RESET = "\033[0m"


def replace_fractions_to_latex(expression):
  # Regular expression to match fractions of the form a/b
  fraction_pattern = r'(-?\d+)\s*/\s*(-?\d+)'

  # Function to convert the matched fractions to LaTeX format
  def convert_to_latex(match):
    numerator = match.group(1).strip()  # Get the numerator
    denominator = match.group(2).strip()  # Get the denominator
    return f'\\frac{{{numerator}}}{{{denominator}}}'  # Return the LaTeX formatted fraction

  # Correctly replace parentheses with \left( and \right) around fractions
  latex_expression = re.sub(r'\(\s*([^()]*)\s*\)', r'\\left(\1\\right)', expression)

  # Substitute all fractions in the expression
  latex_expression = re.sub(fraction_pattern, convert_to_latex, latex_expression)

  # Regex to substitute '(' with '\left\lbrack', excluding '\left('
  latex_expression = re.sub(r'(?<!\\left)\(', r'\\left\\lbrack', latex_expression)

  # Regex to substitute ')' with '\right\rbrack', excluding '\right)'
  latex_expression = re.sub(r'(?<!\\right)\)', r'\\right\\rbrack', latex_expression)

  # Replace '*' with '\cdot'
  latex_expression = re.sub(r'\s*\*\s*', r' \\cdot ', latex_expression)  # Use '\cdot' directly

  # Calculate the numerical result using sympy
  result = sympify(expression.replace(':', '/'))  # Replace ':' with '/' for calculation

  result_fraction = latex(result.simplify())  # Get the LaTeX representation of the result

  return latex_expression, result_fraction


def select_n_expressions(n, inputfile):
  ret_expressions = []
  with open(inputfile) as fr:
    size = len([0 for _ in fr])
  lines_to_read = random.sample(range(1, size + 1), n)
  nl = 1
  with open(inputfile, 'r') as fr:
    for line in fr:
      if nl in lines_to_read:
        ret_expressions.append(line)
      nl += 1
  return ret_expressions


def detailed_output(_input_expressions):
  for input_expression in _input_expressions:
    _latex_output, _result_latex = replace_fractions_to_latex(input_expression)

    # Prepare output with bold label "Solution: " on the right
    latex_output = f"\\[ {_latex_output} \\hspace{{6cm}} \\mbox{{\\textbf{{Solution:}}}} \\hspace{{0.5cm}}" + \
                   f"{_result_latex} \\] "
    print("Original Expression:", input_expression)
    print()
    print("LaTeX Expression:", latex_output)
    print()


def generate_latex_output(_input_expressions, output_filename):
  full_latex_output = f"\\begin{{flalign*}}"
  for input_expression in _input_expressions:
    latex_output, result_latex = replace_fractions_to_latex(input_expression)

    # Prepare output with bold label "Solution: " on the right
    full_latex_output = full_latex_output + f" &\\hspace{{0.8cm}} {latex_output} && \\mbox{{\\textbf{{Solución:}}}}" + \
                        f" \\hspace{{0.5cm}} {result_latex} \\\\ & \\\\"
  full_latex_output = full_latex_output + f" \\end{{flalign*}}"
  with open(output_filename, "w") as f:
    print(full_latex_output, file=f)


def print_usage():
  print()
  print(f"{BOLD}Usage{RESET}: script.py -i <inputfile.txt> -o <outputfile.tex>")
  print(f"\n{BOLD}Arguments:{RESET}")
  print(f"  {BOLD}-i, --input{RESET}   Input file (mandatory, must have .txt extension)")
  print(f"  {BOLD}-o, --output{RESET}  Output file (mandatory, must have .tex extension)")
  print(f"  {BOLD}-h, --help{RESET}    Prints this help message (optional)")
  print()


def parse_arguments(argv):
  input_file = ""
  output_file = ""

  try:
    # Parsing command-line arguments
    opts, args = getopt.getopt(argv, "hi:o:", ["help", "input=", "output="])
  except getopt.GetoptError as err:
    print(err)
    print_usage()
    sys.exit(2)

  for opt, arg in opts:
    if opt in ("-h", "--help"):
      print_usage()
      sys.exit()
    elif opt in ("-i", "--input"):
      input_file = arg
    elif opt in ("-o", "--output"):
      output_file = arg

  # Check if mandatory options are provided
  if not input_file or not output_file:
    print("Error: Both input and output files are mandatory.")
    print_usage()
    sys.exit(2)

  # Check file extensions
  if not input_file.endswith('.txt'):
    print("Error: Input file must have a .txt extension.")
    sys.exit(2)

  if not output_file.endswith('.tex'):
    print("Error: Output file must have a .tex extension.")
    sys.exit(2)

  return input_file, output_file


def main(argv):
  input_filename, output_filename = parse_arguments(argv)
  # Generate a list of input expressions
  input_expressions = select_n_expressions(10, input_filename)

  # Output in debugging format (stdout)
  detailed_output(input_expressions)
  # Latex output
  generate_latex_output(input_expressions, output_filename)


if __name__ == "__main__":
  main(sys.argv[1:])
