import array

# usar mapa de bits para gerenciar os blocos livres

DISK_SIZE = 32
NULL_POINTER = None

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
    def __init__(self, name:str, address:int):
        self.name = name
        self.address = address

class System:
    def __init__(self):
        directory_table = Directory_Table()

    def create_file(self, name:str, content:str):
        content_size = len(content)
        if name in directory_table:
            return (f"Error: File '{name}' already exists!")
        available_blocks = "something" ###
        if content_size > len(available_blocks):
            return ("Error: Not enough memory to store the file!")
    
        
        for file in directory_table:
            1
        return
    def read_file(self, name:str):
        return
    def delete_file(self, name:str):
        return
    
