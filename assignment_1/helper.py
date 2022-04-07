import numpy as np

def get_data(filepath, datatype=('U64', 'U64', 'U64', np.int64, 'U64', 'U64', 'U64', 'U64', 'U64', np.int64, 'U64', np.int64, np.int64, np.float64, 'U64', 'U64', 'U64')):
    with open(filepath) as file_name:
        array = np.genfromtxt(file_name, dtype=datatype, delimiter=";", invalid_raise=False, skip_header=True)
    return array