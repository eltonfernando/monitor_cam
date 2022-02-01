from .client import FileConfig

def test_criate_file_config():
    data = FileConfig("Elton")
    data_input = "0908"
    data.set_id_user(data_input)
    del data
    data =FileConfig("Elton")
    out_data = data.get_id_user()
    print(out_data)
    assert out_data == data_input