import io
import segno
from PIL import Image, ImageDraw

numPanels = 16
for i in range(1, numPanels + 1, 1):  # (start, stop, step)

    # 1. Generate the QR code with 'H' (High) error correction
    qr = segno.make(f'https://quipo.github.io/#pannello-{i}', error='h')

    # 2. Save the QR code as PNG to a memory buffer
    buffer = io.BytesIO()
    qr.save(buffer, scale=15, kind='png')
    buffer.seek(0)

    # 3. Load the QR code with Pillow and convert to RGBA
    qr_img = Image.open(buffer).convert('RGBA')
    qr_width, qr_height = qr_img.size

    # 4. Open and resize your logo (e.g., to 1/3 of the QR code width)
    logo_max_size = qr_width // 3
    logo_img = Image.open('./logo-sanfrancescogrande.png').convert('RGBA')
    logo_img.thumbnail((logo_max_size, logo_max_size), Image.Resampling.LANCZOS)
    logo_width, logo_height = logo_img.size

    # 5. Calculate the center coordinates
    center_x = (qr_width - logo_width) // 2
    center_y = (qr_height - logo_height) // 2

    # 6. Draw a solid white background card behind the logo
    # This clears out the QR modules so they don't bleed through
    draw = ImageDraw.Draw(qr_img)

    # Optional padding around the logo (e.g., 4 pixels)
    padding = 4 
    background_box = [
        center_x - padding, 
        center_y - padding, 
        center_x + logo_width + padding, 
        center_y + logo_height + padding
    ]

    # For a solid square background:
    #draw.rectangle(background_box, fill="white")

    # ALTERNATIVE: For a solid circular background, uncomment the line below:
    draw.ellipse(background_box, fill="white")

    # 7. Paste your opaque logo over the white background card
    qr_img.paste(logo_img, (center_x, center_y), logo_img)

    # 8. Save the final image
    qr_img.save(f'pannello-{i}.png', scale=15)
