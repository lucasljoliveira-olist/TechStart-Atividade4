class Category:
    def __init__(self, name: str, marketplace : str):
        self.__name = name
        self.__marketplace = marketplace

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def get_marketplace(self) -> str:
        return self.__marketplace

    def __str__(self):
        return f"""
                Name: {self.get_name()}
                """
        
class SubCategory(Category):
    def __init__(self, name: str, parent: str, marketplace : str):
        self.__parent = parent
        super().__init__(name, marketplace)
    
    def get_parent(self) -> str:
        return self.__parent
    
    def set_parent(self, parent: str) -> None:
        self.__parent = parent
    
    def __str__(self):
        return f"""
                Name: {self.get_name()}
                Mother: {self.get_parent()}
                """