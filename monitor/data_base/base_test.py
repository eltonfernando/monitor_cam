from .base import DataBase

def test_criate_file_config():
    data = DataBase("cam_test")
    data_input = "rstp data"
    data.set_rstp_link(data_input)
    del data
    data =DataBase("cam_test")
    out_data = data.get_rstp_link()
    print(out_data)
    assert out_data == data_input

