"""
Qr Code Generator

Simple qr code generator with customization and Optional logo insertion
"""

import os
from typing import List, Optional
import qrcode
from qrcode.constants import ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_H, ERROR_CORRECT_Q
from PIL import Image

ERROR_MAP = {"L": ERROR_CORRECT_L, "M": ERROR_CORRECT_M, "Q": ERROR_CORRECT_Q, "H": ERROR_CORRECT_H}

def generate_qr(
        data: str,
        filename: str = "qr.png",
        out_dir: str = ".",
        scale: int = 10,
        border: int = 4,
        error_correction: str = "M",
        fill_color: str = "black",
        back_color: str = "white",
        logo_path: Optional[str] = None,
        logo_scale: int = 4,
        image_format: str = "PNG"
) -> str:
    """
    Generate a QR code image and save it.

    :param data: string to encode
    :param filename: output filename (e.g, 'qr.png')
    :param out_dir: directory to save file
    :param scale: box size (pixel size per QR box)
    :param border: border sizes (boxes)
    :param error_correction: one of 'L', 'M', 'Q', 'H'
    :param fill_color: foreground color (hex or name)
    :param back_color: background color
    :param logo_path: optional path to a logo image to paste at center
    :param logo_scale: logo size will be 1/logo_scale og QR width
    :param image_format: file format (PNG, JPEG, etc.)
    :return: path to saved file
    """

    ec = ERROR_MAP.get(error_correction.upper(), ERROR_CORRECT_M)
    qr = qrcode.QRCode(error_correction=ec, border=border, box_size=scale)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color).convert("RGBA")

    if logo_path and os.path.exists(logo_path):
        try:
            logo = Image.open(logo_path).convert("RGBA")
            img_w, img_h = img.size
            logo_size = int(min(img_w, img_h) / logo_scale)
            logo.thumbnail((logo_size, logo_size), Image.ANTIALIAS)
            pos = ((img_w - logo.width) // 2, (img_h - logo.height) // 2)
            img.paste(logo, pos, mask=logo)
        except Exception as e:
            print("Warning: could not add logo:", e)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, filename)
    img.save(out_path, format=image_format)
    return out_path


def generate_qr_from_list(items: List[str], out_dir: str = "qrs",
                          prefix: str = "qr", **kwargs) -> List[str]:
    """Generate multiple QR images from a list of strings."""
    os.makedirs(out_dir, exist_ok=True)
    paths = []
    for i, item in enumerate(items, start=1):
        name = f"{prefix}_{i}.png"
        path = generate_qr(item, filename=name, out_dir=out_dir, **kwargs)
        paths.append(path)
    return  paths


def wifi_qr_string(ssid: str, password: str, auth_type: str = "WPA", hidden: bool = False) -> str:
    """
    Build a WiFi QR string compatible with many scanners:
    WIFI:T:WPA;S:SSIS;P:password;H:true;;
    """
    hidden_flag = "true" if hidden else "false"
    return f"WIFI:T:{auth_type};S:{ssid};P:{password};H:{hidden_flag};;"


if __name__ == "__main__":
    sample = "https://example.com"
    print("Generating sample QR...")
    p = generate_qr(sample, filename="qr_sample.png", out_dir="output",
                    scale=8, error_correction="H")
    print("Saved:", p)

    print("Generating WiFi QR example...")
    wifi = wifi_qr_string("MyNetwork", "SecretPass", "WPA")
    p2 = generate_qr(wifi, filename="qr_wifi.png", out_dir="output",
                     back_color="black", fill_color="white")
    print("Saved:", p2)
























