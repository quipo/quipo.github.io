import io
import segno
from PIL import Image, ImageDraw

numPanels = 14
for i in range(1, numPanels, 1):  # (start, stop, step)
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

    # Optional: Add rounded corners or a circular mask to the logo for a better look
    mask = Image.new('L', logo_img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + logo_img.size, fill=255)
    logo_img = Image.composite(logo_img, Image.new('RGBA', logo_img.size, (0, 0, 0, 0)), mask)

    # Resize the logo while preserving aspect ratio
    logo_img.thumbnail((logo_max_size, logo_max_size), Image.Resampling.LANCZOS)

    # 5. Calculate the exact center coordinates to paste the logo
    logo_width, logo_height = logo_img.size
    center_x = (qr_width - logo_width) // 2
    center_y = (qr_height - logo_height) // 2

    # 6. Paste the logo onto the QR code
    qr_img.paste(logo_img, (center_x, center_y), logo_img)

    # 7. Save the final image
    qr_img.save(f'pannello-{i}.png', scale=15)