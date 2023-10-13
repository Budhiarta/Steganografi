from PIL import Image

# Buka gambar BMP
image_path = "cover.bmp"
img = Image.open(image_path)

# meminta input koordinat pixel
x = int(input("masukkan titik x: "))
y = int(input("masukkan titik y: "))

# Mendapatkan dimensi gambar
pixel = img.getpixel((x, y))

print(f"Nilai RGB di titik ({x}, {y}): {pixel}")

# meminta input nilai RGB baru
print("")
print("lanjut dengan menyisipkan nilai rbg")
red = int(input("masukkan nilai merah (0-255): "))
green = int(input("masukkan nilai hijau (0-255): "))
blue = int(input("masukkan nilai biru (0-255): "))

# validator RGB
red = max(0, min(255, red))
green = max(0, min(255, green))
blue = max(0, min(255, blue))

# menyimpan niliai rgb inputan user
rgb_val = (red, green, blue)

# menambahkan nilai rgb ke pixel tertentu

newX = int(input("masukkan titik x: "))
newY = int(input("masukkan titik y: "))
img.putpixel((newX, newY), rgb_val)

img.save("cover.bmp")
