import qrcode


class QRCODE:

    def __init__(self, size: int, padding: int):
        self.qr = qrcode.QRCode(box_size=size, border=padding)

    def gen_qr(self, file_name: str, fg: str, bg: str):
        user_input: str = input("Enter a text: ")

        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
            qr_image.save(file_name)

            print(f"Created QR Code Successfully: {file_name}")
        except Exception as e:
            print(f'Error: {e}')


def main():
    qr = QRCODE(size=30, padding=2)
    qr.gen_qr('sample_qr.png', fg='black', bg='white')


if __name__ == '__main__':
    main()
