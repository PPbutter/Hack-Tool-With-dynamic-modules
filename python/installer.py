def execute():
    pass

def install(package:str):
    import pip
    pip.main(["install",package])