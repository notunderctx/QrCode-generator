import click
import qrcode

@click.command()
@click.option('--box-size', type=int, prompt='Enter the box size', help='Box size of the QR code')
@click.option('--border', type=int, prompt='Enter the border size', help='Border size of the QR code')
@click.option('--info', prompt='Enter the text to be encoded in the QR code', help='Text to be shown when scanned')
@click.option('--fill-color', prompt='Enter the line color', help='Color of the lines in the QR code')
@click.option('--background-color', prompt='Enter the background color', help='Background color of the QR code')
@click.option('--output', default='result.png', help='Output file name')
def generate_qrcode(box_size, border, info, fill_color, background_color, output):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )
    qr.add_data(info)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=background_color)
    img.save(output)
    click.echo('QR code generation complete. Saved to {}.'.format(output))

if __name__ == '__main__':
    generate_qrcode()

