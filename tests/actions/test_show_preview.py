from pro_filer.actions.main_actions import show_preview  # NOQA


def test_show_preview(capsys):
    context = {
         "all_files": ["src/__init__.py",
                       "src/app.py", "src/utils/__init__.py"],
         "all_dirs": ["src", "src/utils"]
    }

    show_preview(context)
    output = capsys.readouterr()

    expected_output = (
        "Found 3 files and 2 directories\n"
        "First 5 files: ['src/__init__.py', "
        "'src/app.py', 'src/utils/__init__.py']\n"
        "First 5 directories: ['src', 'src/utils']\n"
    )

    assert output.out == expected_output
