import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from PIL import Image

def generate_barcode(product_name: str, price: str, identifier: str):
    """商品情報を埋め込んだバーコードを生成"""
    data = f"{product_name}:{price}:{identifier}"  # カスタムデータ形式
    CODE128 = barcode.get_barcode_class('code128')
    barcode_instance = CODE128(data, writer=ImageWriter())

    buffer = BytesIO()
    barcode_instance.write(buffer)
    buffer.seek(0)
    return Image.open(buffer), data  # 画像と埋め込んだデータを返す

# 例
barcode_image, barcode_data = generate_barcode("Apple", "150", "123456789012")
barcode_image.show()
print("埋め込まれたデータ:", barcode_data)
