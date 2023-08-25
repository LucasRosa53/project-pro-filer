from pro_filer.actions.main_actions import show_disk_usage  # NOQA

def test_show_disk_usage(capsys, tmp_path):
    file = tmp_path / "idontknow"
    file.touch()
    file.write_text("but now i know")

    file_two = tmp_path / "iknow"
    file_two.touch()
    file_two.write_text("but now i forget")

    context = {
    "all_files": [
        str(file), str(file_two)
    ]
}
    show_disk_usage(context)
    output = capsys.readouterr()
    slice_phrases = output.out.split("\n")
    assert "iknow" in slice_phrases[0]
    assert "idontknow" in slice_phrases[1]
    assert "Total size: 30" in slice_phrases[2]