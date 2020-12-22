class Marketplace:
    def __init__(self, id: int, name: str, categories: list):
        self.__id = id
        self.__name = name
        self.__categories = categories

    def set_id(self, id: int) -> None:
        self.__id = int(id)

    def get_id(self) -> int:
        return self.__id

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name
    
    def get_categories(self):
        return self.__categories

    def __str__(self):
        return f"""
                Id: {self.get_id()}
                Name: {self.get_name()}
                """
        