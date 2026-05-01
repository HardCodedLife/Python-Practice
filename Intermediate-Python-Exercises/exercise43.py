class Database:
    _instance = None
    def __new__(cls):
        if cls._instance == None:
            print("Loading Database (first time only)...")
            cls._instance = super(Database, cls).__new__(cls)
        return Database._instance
    def __init__(self):
        print("Initializing Database...")
if __name__ == "__main__":
    db1 = Database()
    db2 = Database()
    print(db1 is db2)
