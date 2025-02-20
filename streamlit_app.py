from io import BytesIO
from barcode import Code128
from barcode.writer import ImageWriter

# Write to a file-like object:
rv = BytesIO()
Code128(str(100000902922), writer=ImageWriter()).write(rv)

data = "AbCd-123456"
fileName = data + ".jpeg"

# Or to an actual file:
with open(fileName, "wb") as f:
    Code128(data, writer=ImageWriter()).write(f)
