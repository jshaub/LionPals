import html
import cgitb; cgitb.enable()
import cgi; fields = cgi.FieldStorage()
from Session import Session

script = "login"
mail = fields.getvalue("mail")
pwd = fields.getvalue("pwd")

session = Session.login(mail, pwd)
html.begin_output()

if session is not None: 

	status = "0"
	message = "Login successful"
	print(open("login_result.html", "r").read()
		.replace("<?script>", script)
		.replace("<?status>", status)
		.replace("<?message>", message))

else: 
	status = "-1"
	message = "An error occurred while logging in"
	print(open("login_result.html", "r").read()
		.replace("<?script>", script)
		.replace("<?status>", status)
		.replace("<?message>", message))

