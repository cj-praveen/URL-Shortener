import sqlite3, random, string

class DataBase:
    def __init__(self) -> None:
        self.db: sqlite3.Connection = sqlite3.connect("url.db", check_same_thread=False)
        self.db.execute("CREATE TABLE IF NOT EXISTS URLS(URL TEXT, UID TEXT)")
        self.db.commit()

    def check_database(self, url: str) -> tuple:
        if result := self.db.execute("SELECT UID FROM URLS WHERE URL=?", (url,)).fetchone():
            return True, result[0]
        return False, None

    def new_record(self, url: str) -> str:
        generate_uid = lambda length: ''.join(random.choice(string.ascii_letters) for _ in range(length))
        uid: str = generate_uid(10)
        self.db.execute("INSERT INTO URLS VALUES(?,?)", (url,uid))
        self.db.commit()
        return uid

