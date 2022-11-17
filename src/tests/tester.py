import pathlib 


class Tester():
    def __init__(self, repository:str):
        self.repository = repository

    def check_a_directory(self):
        assert pathlib.Path(self.repository).is_dir(), "Sequence repository is not found !"
    
    def check_if_a_directory_is_empty(self):
        assert any(pathlib.Path(self.repository).iterdir()), "Sequence repository is empty !"
    
    def check_if_a_directory_contains_images(self):
        existed_extensions_list = list(map( lambda x: x.suffix ,pathlib.Path(self.repository).rglob("*")))
        extensions_not_images = [element for element in existed_extensions_list if element.lower() not in [".jpg", ".jpeg", ".png"]]

        assert len(extensions_not_images) == 0, "There are files that are not images in the repository! Please consider removing them before generating star trails"

