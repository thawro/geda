from geda.get_data import DATA_PROVIDERS, get_data
from geda.utils.config import DATA_PATH

ROOTS = {
    "DUTS": DATA_PATH / "DUTS",
    "NYUDv2": DATA_PATH / "NYUDv2",
    "VOC": DATA_PATH / "voc_2012",
}


def _download(name: str):
    root_name, *_ = name.split("_")
    root = str(ROOTS[root_name])
    get_data(name, root=root)


def test_download():
    for name in DATA_PROVIDERS:
        _download(name)


if __name__ == "__main__":
    # test_download()
    _download("NYUDv2")
