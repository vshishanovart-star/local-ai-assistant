import subprocess


def is_process_running(process_name):
    result = subprocess.run(
        ["tasklist"],
        capture_output=True,
        text=True
    )

    return process_name.lower() in result.stdout.lower()