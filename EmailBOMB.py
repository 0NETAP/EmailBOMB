from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import random
n = random.random()

#FROM GMAIL ACCOUNT ONLY

host = "smtp.gmail.com"
port = 587
#type email
username = ""
#type email password
password = ""
from_email = username
#enter target adress
to_list = ["miltondv6@gmail.com",""] 

email_conn = smtplib.SMTP(host, port)
email_conn.starttls()
email_conn.login(username, password)

the_msg = MIMEMultipart("alternative")
#subject of the email
the_msg['Subject'] = ""
the_msg["From"] = from_email


plain_txt = "Testing the message"
#insert html code here (use https://html-online.com/editor/)
html_txt = """\
<h1 style="text-align: center;">𝒮𝐸𝐿𝐸𝒞𝒯 𝒴𝒪𝒰𝑅<br />𝒫𝒪𝑅𝒩𝐻𝒰𝐵 𝐸𝒳𝒫𝐸𝑅𝐼𝐸𝒩𝒞𝐸</h1>
<p style="text-align: center;">Ｔｈａｎｋ ｙｏｕ ｆｏｒ ｓｉｇｎｉｎｇ ｕｐ ｆｏｒ ｐｏｒｎｈｕｂ<br />&nbsp; &nbsp; &nbsp;ｌｅｖｅｌ ｕｐ ａｎｄ ｊｏｉｎ Ｐｏｒｎｈｕｂ Ｐｒｅｍｉｕｍ ｆｏｒ ｔｈｅ ｕｌｔｉｍａｔｅ ｐｏｒｎ ｅｘｐｅｒｉｅｎｃｅ!</p>
<div class="buttons" style="text-align: center;"><a class="btnOrange removeAdLink" href="https://www.pornhub.com/create_account_select#" rel="nofollow" data-segment="straight" data-entrycode="SignUp-Modal">𝓖𝓮𝓽 𝓟𝓸𝓻𝓷𝓱𝓾𝓫 𝓟𝓻𝓮𝓶𝓲𝓾𝓶</a></div>
<div class="buttons" style="text-align: center;">&nbsp;</div>
<div class="buttons"><br /><br /></div>
"""

part_1 = MIMEText(plain_txt, 'plain')
part_2 = MIMEText(html_txt, "html")

the_msg.attach(part_1)
the_msg.attach(part_2)


i=0
print("Sending...")
#change the less than value to however many times you want the email to be sent
#example: i<80 sends 80 emails, i<10 sends 10 emails
while i<200:
    email_conn.sendmail(from_email, to_list, the_msg.as_string())
    print("Bot has sent " + str(i+1) + " so far") 
    i=i+1

print("All " + str(i) + " emails have been sent!")    
email_conn.quit()
