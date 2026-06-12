from task_router import main


def run_task(task_text, output_box):

    result = main(task_text)

    output_box.delete(
        "1.0",
        "end"
    )

    output_box.insert(
        "1.0",
        str(result)
    )