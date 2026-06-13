from PIL import Image

img = Image.open(
    "assets/local_ai_icon.png"
)

img.save(
    "assets/local_ai_icon.ico",
    format="ICO",
    sizes=[
        (16, 16),
        (32, 32),
        (48, 48),
        (64, 64),
        (128, 128),
        (256, 256)
    ]
)

print("ICO created.")