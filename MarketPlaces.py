class Marketplace:
    def __init__(self, name: str, categories: list):
        self.__name = name
        self.__categories = categories

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name
    
    def get_categories(self):
        return self.__categories

    def __str__(self):
        return f"""
                Name: {self.get_name()}
                """
        