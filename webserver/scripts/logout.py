import html_builder
import cgitb; cgitb.enable()
import cgi; fields = cgi.FieldStorage()
from Session import Session

script = "logout"

html_builder.begin_output()
session = Session.get_session()

if session is not None:
	session.logout()
	status = "0"
	message = "Logout successful"
	print(open("login_result.html", "r").read()
		.replace("<?script>", script)
		.replace("<?status>", status)
		.replace("<?message>", message))
else: 
	status = "-1"
	message = "An error occurred while logging out"
	print(open("login_result.html", "r").read()
		.replace("<?script>", script)
		.replace("<?status>", status)
		.replace("<?message>", message))


