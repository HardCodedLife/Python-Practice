class My_Database:
    def __enter__(self):
        print("Database connected!")
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print("Database disconnected!")
if __name__ == "__main__":
    with My_Database() as db:
        raise Exception("Something went wrong")
