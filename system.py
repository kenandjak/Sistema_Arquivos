import array

# usar mapa de bits para gerenciar os blocos livres

class Block:
    def __init__(self,data:str):
        self.data = data
        self.pointer = None

class List:
    def __init__(self):
        self.start = None

    def showList(self):
        present = self.start
        while present != None:
            print(present.data)
            present = present.pointer
    
    def addStart(self,text:str):
        block = Block(text)
        block.pointer = self.start
        self.start = block

class Directory_Table:
    def __init__(self):
        self.files = {}

    def add_file(self, file_name: str, file_content: str):
        if file_name in self.files:
            return f"Error: File '{file_name}' already exists!"
        self.files[file_name] = file_content
    
    
    def list_files(self):
        return list(self.files.keys())
class Available_Blocks:
    def __init__(self):
        pass

class System:
    def __init__(self):
        self.directory_table = Directory_Table()
        self.available_blocks = Available_Blocks()

    def create_file(self, name:str, content:str):
        content_size = len(content)
        if content_size > len(self.available_blocks):
            return ("Error: Not enough memory to store the file!")
        return self.directory_table.add_file(name, content)
    def read_file(self, name:str):
        return
    def delete_file(self, name:str):
        return
    

