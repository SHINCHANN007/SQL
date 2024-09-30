from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client.TYCS
def display():
    try:
        id = input("Enter the ID to display record: ")
        for i in db.pyrmp.find({"empId":id}):
            print(i)
        print("\nRecord displayed")
    except Exception:
        print(str(Exception))
    finally:
        client.close()
display()
