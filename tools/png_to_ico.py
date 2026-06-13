from pathlib import Path

from PIL import Image


png_files = list(
    Path("assets").glob("*.png")
)

for png_file in png_files:

    ico_file = png_file.with_suffix(
        ".ico"
    )

    img = Image.open(
        png_file
    )

    img.save(
        ico_file,
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

    print(
        f"Created: {ico_file.name}"
    )

print("\nDone.")