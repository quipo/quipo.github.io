import os

ext = 'png'

# 1. Define your QR codes and their corresponding labels
# Replace these with your actual filenames and desired text labels
qr_data = [
    {"file": f"pannello-1.{ext}", "label": "Battesimo"},
    {"file": f"pannello-2.{ext}", "label": "Beato Bernardino<br />da Feltre"},
    {"file": f"pannello-3.{ext}", "label": "San Lorenzo Martire"},
    {"file": f"pannello-4.{ext}", "label": "Crocifisso e <br />Sant'Antonio morente"},
    {"file": f"pannello-5.{ext}", "label": "Madonna<br />della Salute"},
    {"file": f"pannello-6.{ext}", "label": "Battesimo di<br />Santa Giustina<br />(Cappella Vitaliani)"},
    {"file": f"pannello-7.{ext}", "label": "Ecce Homo<br />(edicola sinistra)"},
    {"file": f"pannello-8.{ext}", "label": "Altare maggiore"},
    {"file": f"pannello-9.{ext}", "label": "Madonna con<br />Bambino e Santi<br />(edicola destra)"},
    {"file": f"pannello-10.{ext}", "label": "Santissimo Sacramento"},
    {"file": f"pannello-11.{ext}", "label": "San Francesco Stigmatizzato"},
    {"file": f"pannello-12.{ext}", "label": "Genealogia di Gesù · <br />Storie della Vergine"},
    {"file": f"pannello-13.{ext}", "label": "Ascensione di Cristo"},
]

ROMAN_NUMERALS = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV"]

# Alternative: If you just want to auto-load all files from a folder 
# and use the filename as the label, uncomment the lines below:
# qr_extensions = ('.png', '.{ext}')
# qr_data = [{"file": f, "label": os.path.splitext(f)[0].replace('_', ' ').title()} 
#            for f in os.listdir('.') if f.lower().endswith(qr_extensions)]


def generate_html(data, output_filename="qrcode_grid.html"):
    # Generate the HTML items for the grid
    grid_items_html = ""
    for i, item in enumerate(data):
        # Simple safety check to ensure the file exists
        if not os.path.exists(item["file"]):
            print(f"Warning: File '{item['file']}' not found. It will still be added to HTML.")
            
        roman = ROMAN_NUMERALS[i] if i < len(ROMAN_NUMERALS) else str(i + 1)

        grid_items_html += f"""
        <div class="qr-item">
            <div class="roman-number">{roman}</div>
            <img src="{item['file']}" alt="{item['label']}">
            <div class="label">{item['label']}</div>
        </div>
        """

    # Full HTML/CSS Template
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QR Code Print Grid</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@700&display=swap" rel="stylesheet">
    <style>
        /* Base Styles for Screen */
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: #f4f4f9;
            margin: 0;
            padding: 40px 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }}
        
        .print-btn {{
            background-color: #007bff;
            color: white;
            border: none;
            padding: 12px 24px;
            font-size: 16px;
            border-radius: 6px;
            cursor: pointer;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: background 0.2s;
        }}
        .print-btn:hover {{
            background-color: #0056b3;
        }}

        /* Grid Layout (3 columns looks great on standard A4/Letter paper) */
        .grid-container {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 30px;
            max-width: 900px;
            width: 100%;
            background: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        }}.qr-item {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: space-between;
            border: 1px solid #e0e0e0;
            padding: 25px 20px;
            border-radius: 8px;
            background: #fff;
            page-break-inside: avoid; 
            break-inside: avoid;
        }}

        .roman-number {{
            font-size: 32px;          /* Significantly larger than the label text */
            font-weight: 800;         /* Extra bold weight */
            color: #000000;           /* Pure black for high contrast */
            margin-bottom: 15px;      /* Space between numeral and QR code */
            letter-spacing: 0.5px;
        }}

        .qr-item img {{
            max-width: 100%;
            height: auto;
            aspect-ratio: 1 / 1;
            object-fit: contain;
        }}

        .label {{
            margin-top: 18px;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, Arial, sans-serif;
            font-size: 16px;         /* Bumped up slightly */
            font-weight: 700;        /* Bold */
            text-transform: uppercase; /* Uppercase is easier to read word-by-word from afar */
            letter-spacing: 1.5px;   /* Prevents letters from blurring together at a distance */
            color: #000000;          /* Pure black for maximum contrast against white paper */
            text-align: center;
            word-wrap: break-word;
            width: 100%;
            line-height: 1.5;
        }}

        /* Print Optimization Styles */
        @media print {{
            body {{
                background: white;
                padding: 0;
                margin: 0;
            }}
            .print-btn {{
                display: none; /* Hide the button when printing */
            }}
            .grid-container {{
                box-shadow: none;
                padding: 0;
                max-width: 100%;
            }}
            .qr-item {{
                border: 1px solid #ddd; /* Subtle border for clean cut lines if needed */
            }}
        }}
    </style>
</head>
<body>

    <!-- button class="print-btn" onclick="window.print()">🖨️ Print QR Codes</button -->

    <div class="grid-container">
        {grid_items_html}
    </div>

</body>
</html>
"""

    # Write the file
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"Success! '{output_filename}' has been created.")

if __name__ == "__main__":
    generate_html(qr_data)