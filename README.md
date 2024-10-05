# Assignments Generator

## Description
This package reads in a `.txt` file of combined operations with fractions, chooses 10 lines, and generates a LaTeX formatted output with the expression on the left and the solution on the right.

## Installation

To install and run this package, it is recommended to use a virtual environment. Here are the steps to set it up:

1. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install the required packages**:
   Ensure that you have a `requirements.txt` file in the same directory as this README. Run the following command to install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the script, use the following command:

```bash
python script.py -i <inputfile.txt> -o <outputfile.tex>
```

### Arguments:
- `-i, --input`: Input file (mandatory, must have `.txt` extension).
- `-o, --output`: Output file (mandatory, must have `.tex` extension).
- `-h, --help`: Prints this help message (optional).

### Example:
```bash
python script.py -i input.txt -o output.tex
```

### Help Dialog:
If you run the script with the `-h` or `--help` option, it will display the following usage instructions:

```
Usage: script.py -i <inputfile.txt> -o <outputfile.tex>

Arguments:
  -i, --input   Input file (mandatory, must have .txt extension)
  -o, --output  Output file (mandatory, must have .tex extension)
  -h, --help    Prints this help message (optional)
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

