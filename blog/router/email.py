# from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
# from pydantic import EmailStr
# from fastapi import APIRouter
#
# router = APIRouter(
#     prefix= '/send_email',
#     tags= ['email']
# )
#
#
# conf = ConnectionConfig(
#     MAIL_USERNAME = "cozmosluna",
#     MAIL_PASSWORD = "owleenokwwbhhbwy",
#     MAIL_FROM = "cozmosluna@gmail.com",
#     MAIL_PORT = 587,
#     MAIL_SERVER="smtp.gmail.com",
#     MAIL_FROM_NAME="Cozmos Luna Mission",
#     MAIL_STARTTLS=True,
#     MAIL_SSL_TLS=False,
#     USE_CREDENTIALS=True,
#     VALIDATE_CERTS=True
# )
#
# @router.post("/send_mail")
# async def send_mail(email: str):
#     emails = [email]
#     template = 'Hi I am Cozmos'
#     message = MessageSchema(
#         subject="Verification",
#         recipients=emails,
#         body=template,
#         subtype="plain"
#     )
#
#     fm = FastMail(conf)
#     await fm.send_message(message)
#     print(message)
#
#
#     return {
#         'message' : 'done'
#     }
#
