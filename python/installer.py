def execute():
    pass

def install(packages:list):
    import pip
    stat = "install"
    for i in packages:
        pip.main([stat,i])