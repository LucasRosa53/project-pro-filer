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


def test_show_preview_empty(capsys):
    context = {
        "all_files": [],
        "all_dirs": []
    }

    show_preview(context)
    output = capsys.readouterr()

    expected_output = "Found 0 files and 0 directories\n"


    assert output.out == expected_output


def test_a_lot_of_files_dirs(capsys):
    context = {
        "all_files": [
            "file1.py",
            "file2.py",
            "file3.py",
            "file4.py",
            "file5.py",
            "file6.py",
        ],
        "all_dirs": [
            "dirs1",
            "dirs2",
            "dirs3",
            "dirs4",
            "dirs5",
            "dirs6",
        ]
    }
    show_preview(context)
    output = capsys.readouterr()

    expected_output = (
        "Found 6 files and 6 directories\n"
        "First 5 files: ['file1.py', 'file2.py', 'file3.py', 'file4.py', 'file5.py']\n"
        "First 5 directories: ['dirs1', 'dirs2', 'dirs3', 'dirs4', 'dirs5']\n"
    )

    assert output.out == expected_output