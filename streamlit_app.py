#import streamlit as st
#from io import BytesIO
#from barcode import Code128
#from barcode.writer import ImageWriter
#from PIL import Image,ImageDraw, ImageFont

## タイトル
#st.title("Streamlit でバーコードを生成")
#
## ユーザー入力
#barcode_text = st.text_input("バーコードの内容を入力してください")
#barcode_date = st.text_input("バーコード内のデータ")
#
## バーコード生成関数
#def generate_barcode(text):
#    buffer = BytesIO()
#    barcode = Code128(text, writer=ImageWriter())
#    barcode.write(buffer)
#    buffer.seek(0)
#    return buffer
#
## ボタンが押されたらバーコードを生成
#if st.button("バーコードを作成"):
#    barcode_image = generate_barcode(barcode_text)
#    
#    # PIL で画像を開いて Streamlit で表示
#    image = Image.open(barcode_image)
#    st.image(image, caption="生成されたバーコード", use_column_width=True)
#    
#    # ダウンロードボタン
#    st.download_button(
#        label="バーコードをダウンロード",
#        data=barcode_image,
#        file_name="barcode.png",
#        mime="image/png"
#    )

from barcode import Code128
from barcode.writer import ImageWriter
from PIL import Image

# バーコードに情報を埋め込む（"Hello123"）
barcode_data = "Hello123"
barcode = Code128(barcode_data, writer=ImageWriter())

# バーコードを保存（PNG形式）
filename = barcode.save("barcode_with_text")

# 画像を開いて表示
image = Image.open(f"{filename}.png")
image.show()

