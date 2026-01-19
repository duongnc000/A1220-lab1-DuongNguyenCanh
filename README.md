# Receipt Extraction Tool

This project is a command-line tool that processes a directory of receipt images and extracts structured information from each receipt using an OpenAI vision-enabled language model.

---

## Features

- Processes receipt images from a directory
- Extracts structured fields (date, amount, vendor, category)
- Outputs machine-readable JSON
- Simple CLI interface

---

## Project Structure

```text
.
├── file_io.py
├── gpt.py
├── main.py
└── README.md
```

---

## Requirements

- Python 3.9+
- OpenAI API key
- openai Python package

Install dependencies:

```bash
pip install openai
```

Set your API key:

```bash
export OPENAI_API_KEY="your-api-key"
```

---

## Usage

Run the tool from the project root:

```bash
python -m main path/to/receipt_images --print
```

### Arguments

- `dirpath` — directory containing receipt images
- `--print` — print extracted JSON to stdout

---

## Example Output

```json
{
  "receipt1.jpg": {
    "date": "2024-01-12",
    "amount": "$23.45",
    "vendor": "Starbucks",
    "category": "Meals"
  }
}
```

---

## Notes

- Only files in the given directory are processed
- If a field cannot be extracted, it is returned as `null`
- API errors will raise exceptions
