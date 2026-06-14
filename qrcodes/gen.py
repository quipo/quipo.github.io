import segno

numPanels = 14
for i in range(1, numPanels, 1):  # (start, stop, step)
    qrcode = segno.make(f'https://quipo.github.io/#pannello-{i}')
    qrcode.save(f'pannello-{i}.svg')
    qrcode.save(f'pannello-{i}.png', scale=15)