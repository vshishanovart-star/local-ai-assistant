from pathlib import Path

from PIL import Image
from PIL import ImageTk

from task_router import main
import os


def run_task(
    task_text,
    output_box,
    image_label
):

    result = main(task_text)

    file_name = Path(result).name

    output_box.delete(
        "1.0",
        "end"
    )

    output_box.insert(
        "1.0",
        f"Task completed\n\nGenerated image:\n{file_name}"
    )

    try:

        image_path = Path(result)

        image = Image.open(
            image_path
        )

        image.thumbnail(
            (700, 500)
        )

        photo = ImageTk.PhotoImage(
            image
        )

        image_label.config(
            image=photo
        )

        image_label.image = photo

        image_label.image_path = str(image_path)

        image_label.bind(
            "<Button-1>",
            lambda e: os.startfile(
                image_label.image_path
            )
        )

    except Exception as e:

        print(
            "Image preview error:",
            e
        )