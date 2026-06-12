from pathlib import Path


COMFY_OUTPUT = Path(
    r"C:\AI\ComfyUI\ComfyUI_windows_portable\ComfyUI\output"
)


def extract_image_path(history):

    outputs = history.get(
        "outputs",
        {}
    )

    for node in outputs.values():

        images = node.get(
            "images",
            []
        )

        if images:

            filename = images[0]["filename"]

            return COMFY_OUTPUT / filename

    files = sorted(
        COMFY_OUTPUT.glob("*.png"),
        key=lambda p: p.stat().st_mtime,
        reverse=True
    )

    if files:
        return files[0]

    return None