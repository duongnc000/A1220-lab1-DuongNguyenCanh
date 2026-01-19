# gpt.py
import json
from openai import OpenAI

client = OpenAI()

CATEGORIES = [
    "Meals",
    "Transport",
    "Lodging",
    "Office Supplies",
    "Entertainment",
    "Other",
]


def sanity_check(json_response):
    """The language model output is not always perfect. Sometimes it parses
    the correct amount without any indication of the currency. Sometimes, it
    also includes the currency symbol, such as “$”, in the parsed value. Add
    a small function that processes the output of the language model, removes
    the “$” symbol if present, converts the parsed value to float, and replaces
    the one in the dictionary.

        Args:
            json_response (dict): The JSON response from the language model.

        Returns:
            dict: The processed JSON response with corrected values.
    """
    if "amount" in json_response:
        value = json_response["amount"]
        if isinstance(value, str):
            value = value.replace("$", "").strip()
            try:
                json_response["amount"] = float(value)
            except ValueError:
                json_response["amount"] = None
    return json_response


def extract_receipt_info(image_b64):
    """Extract information from a receipt image.

    Args:
        image_b64 (str): The base64-encoded image data of the receipt.

    Returns:
        dict: A dictionary containing the extracted receipt information.
    """
    prompt = f"""
You are an information extraction system.
Extract ONLY the following fields from the receipt image:

date: the receipt date as a string
amount: the total amount paid as it appears on the receipt
vendor: the merchant or vendor name
category: one of [{", ".join(CATEGORIES)}]

Return EXACTLY one JSON object with these four keys and NOTHING ELSE.
Do not include explanations, comments, or formatting.
Do not wrap the JSON in markdown.
If a field cannot be determined, use null.

The output must be valid JSON.
"""
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        seed=43,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{image_b64}"},
                    },
                ],
            }
        ],
    )

    response_json = json.loads(response.choices[0].message.content)
    return sanity_check(response_json)
