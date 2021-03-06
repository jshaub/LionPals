import html_builder
import cgitb; cgitb.enable()
import cgi; fields = cgi.FieldStorage()
import UserAccountSet
from UserAccountPropertySet import UserAccount
from getAccountInfo import getAccountInfo
import logs

html_builder.begin_output()

script = "signup"

mail = fields.getvalue("mail")
pwd = fields.getvalue("pwd")

if mail is None or pwd is None: 
	print(open("signup.html", "r").read().replace("<?mail>", mail or "").replace("<?pwd>", pwd or ""))
else: 
	try: 
		user = UserAccount.create(mail, pwd)
		user.send_verify_email()
		accountInfo = getAccountInfo(user)

		if accountInfo: 
			if len(accountInfo) > 0: 
				user.name = accountInfo[0]
			
			if len(accountInfo) > 1: 
				user.academic_program = accountInfo[3]
				user.campus = accountInfo[2]

		user.commit()
		logs.print_line("user signup complete: " + str(user) + ".")
	except UserAccountSet.ACCOUNT_ALREADY_EXISTS: 
		status = "-1"
		message = "<?mail> has already been registered"
		print(open("signup_verify_result.html", "r").read()
			.replace("<?script>", script)
			.replace("<?status>", status)
			.replace("<?message>", message)
			.replace("<?mail>", mail))
	else: 
		status = "0"
		message = "To finish the sign-up process, please click the verification link sent to <?mail>"
		print(open("signup_verify_result.html", "r").read()
			.replace("<?script>", script)
			.replace("<?status>", status)
			.replace("<?message>", message)
			.replace("<?mail>", mail))


