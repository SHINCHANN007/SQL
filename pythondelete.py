from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client.TYCS
def delete():
    try:
        id = input('Enter the ID: ')
        db.pyrmp.delete_one(
            {"_id:": id}
            )
        print('\nData Deleted Successfully')
    except Exception:
        print(str(Exception))
    finally:
        client.close()
delete()
