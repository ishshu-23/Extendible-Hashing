class Directory:
    __instance = None

    def __new__(cls, gd=1, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Directory, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self, gd=1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gd = gd
        self.l = [None for i in range(pow(2, self.gd))]


