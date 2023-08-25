from pro_filer.actions.main_actions import show_details  # NOQA
from unittest.mock import Mock, patch

def test_show_details(capsys, tmp_path):
    file = tmp_path / "detailsFile"
    file.touch()
    context = {
        "base_path": str(file)
    }
    show_details(context)
    output = capsys.readouterr()

    expected_output = (
        "File name: detailsFile\n"
        "File size in bytes: 0\n"
        "File type: file\n"
        "File extension: [no extension]\n"
        "Last modified date: 2023-08-25\n"
        )


    assert output.out == expected_output

def test_no_existance_file(capsys):
    context = {
        "base_path": "/home/trybe/Downloads/????"
    }
    mock = Mock(return_value = False)
    with patch("os.path.exists", mock):
        show_details(context)
        output = capsys.readouterr()

        expected_out = (
            "File '????' does not exist\n"
        )

        assert output.out == expected_out