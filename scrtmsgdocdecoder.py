import requests
from bs4 import BeautifulSoup
import re

def decode_secret_message(doc_url):
    # Fetch the Google Doc
    response = requests.get(doc_url)
    response.raise_for_status()
    html = response.text

    # Parse HTML to extract plain text
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(separator="\n")

    # Flexible regex to capture x, character, y ignoring extra spaces
    pattern = re.compile(r'(\d+)\s*\n\s*(.)\s*\n\s*(\d+)')
    matches = pattern.findall(text)

    if not matches:
        print("No matches found. Check your Google Doc format or link.")
        return

    # Convert matches to (char, x, y) tuples
    data = [(char, int(x), int(y)) for x, char, y in matches]

    # Determine grid size
    max_x = max(x for _, x, _ in data)
    max_y = max(y for _, _, y in data)

    # Initialize grid
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Fill the grid
    for char, x, y in data:
        grid[y][x] = char

    # Print the grid
    for row in grid:
        print(''.join(row))

# Example usage
google_doc_link = "https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub"
decode_secret_message(google_doc_link)
