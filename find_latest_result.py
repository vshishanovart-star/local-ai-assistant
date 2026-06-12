from pathlib import Path

from tool_result_paths import TOOL_RESULTS


def find_latest_result(tool_name):
    tool_info = TOOL_RESULTS.get(tool_name)

    if not tool_info:
        return None

    output_dir = Path(
        tool_info["output_dir"]
    )

    if not output_dir.exists():
        return None

    files = []

    for ext in tool_info["extensions"]:
        files.extend(
            output_dir.rglob(f"*{ext}")
        )

    if not files:
        return None

    latest = max(
        files,
        key=lambda item: item.stat().st_mtime
    )

    return latest


if __name__ == "__main__":
    result = find_latest_result(
        "image_generation"
    )

    print(result)