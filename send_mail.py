#!/Users/kawasakitaku/Documents/python-PVM/ln-python2.7/bin/python2.7

import sys

from email.mime.text import MIMEText

from twisted.internet import reactor
from twisted.mail.smtp import sendmail
from twisted.python import log



log.startLogging(sys.stdout)

host = "localhost"
sender = "@localhost"
recipients = ["@localhost"]

msg = MIMEText("""hello !!!""")
msg["Subject"] = "hello"
msg["from"] = "admiter '<%s>'" % (sender,)
msg["To"] = ", ".join(recipients)

deffered = sendmail(host,sender,recipients,msg.as_string(),port=2500)
deffered.addBoth(lambda result: reactor.stop())

reactor.run()


