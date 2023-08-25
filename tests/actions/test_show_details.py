from pro_filer.actions.main_actions import show_details  # NOQA


def test_show_details(capsys):
    context = {
        "base_path": "/home/trybe/Downloads/Trybe_logo.png"
    }

    show_details(context)
    output = capsys.readoutter()

    expected_output = (
    "File name: Trybe_logo.png"
    "File size in bytes: 22438"
    "File type: file"
    "File extension: .png"
    "Last modified date: 2023-06-13"
    )

    assert output.out == expected_output



