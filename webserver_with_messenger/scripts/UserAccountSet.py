
import sqlite3

class UserAccount: 
	conn = sqlite3.connect("database.db")
	conn.executescript("""
create table if not exists UserAccountSet (
	ID Integer primary key autoincrement, 
	mail String unique, 
	pwd String
)
"""	)
	conn.commit()


	def __init__(self, ID): 
		self.conn = sqlite3.connect("database.db")
		self.ID = ID


	def __del__(self): 
		self.conn.close()


	@property
	def mail(self): 
		cursor = self.conn.cursor()
		res = cursor.execute("""\
select mail 
from UserAccountSet 
where ID == ? 
"""		, (self.ID, )).fetchone()[0]
		cursor.close()

		return str(res)


	@mail.setter
	def mail(self, value): 
		self.conn.execute("""\
update UserAccountSet 
set mail = ? 
where ID = ?
"""		, (value, self.ID, ))


	@property
	def pwd(self): 
		cursor = self.conn.cursor()
		res = cursor.execute("""\
select pwd 
from UserAccountSet 
where ID == ? 
"""		, (self.ID, )).fetchone()
		cursor.close()

		return str(res[0])


	@pwd.setter
	def pwd(self, value): 
		self.conn.execute("""\
update UserAccountSet 
set pwd = ? 
where ID = ?
"""		, (value, self.ID, ))


	@classmethod
	def get_account(cls, mail): 
		cursor = cls.conn.cursor()
		res = cursor.execute("""\
select ID 
from UserAccountSet 
where mail = ?
"""		, (mail, )).fetchone()
		
		cursor.close()

		if res is None: 
			return None

		return cls(res[0])


	@classmethod
	def get_account_by_id(cls, ID):
		return cls(ID)


	def __str__(self): 
		return "UserAccountSet.UserAccount(mail = \"" + str(self.mail) + "\", pwd = \"" + self.pwd + "\")"


	def commit(self): 
		self.conn.commit()


	@classmethod
	def create(cls, mail, pwd): 
		cursor = cls.conn.cursor()
		try: 
			cursor.execute("""\
insert into UserAccountSet 
(mail, pwd) 
values (?, ?)
"""			, (mail, pwd, ))
		except: 
			raise "AlreadyExists"
		
		
		ID = cursor.lastrowid
		cursor.close()
		
		return cls(ID)


	def remove(self): 
		self.conn.execute("""\
delete from UserAccountSet 
where ID = ?
"""		, (self.ID, ))




def print_table(): 
	conn = sqlite3.connect("accounts.db")

	for row in conn.execute("""\
select * 
from UserAccountSet
"""		): 
		print(row)
	
	conn.close()

