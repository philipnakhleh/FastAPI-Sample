from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models
from typing import List
from ..database import get_db
from ..repository import investor
import math, random
from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
import hashlib

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

conf= None
def get_email(first_name, code)->str:
    return f'''
            <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">

    <head>
        <meta charset="UTF-8">
        <meta content="width=device-width, initial-scale=1" name="viewport">
        <meta name="x-apple-disable-message-reformatting">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta content="telephone=no" name="format-detection">
        <title></title>
        <!--[if (mso 16)]>
        <style type="text/css">
        a {{text-decoration: none;}}
        </style>
        <![endif]-->
        <!--[if gte mso 9]><style>sup {{ font-size: 100% !important; }}</style><![endif]-->
        <!--[if gte mso 9]>
    <xml>
        <o:OfficeDocumentSettings>
        <o:AllowPNG></o:AllowPNG>
        <o:PixelsPerInch>96</o:PixelsPerInch>
        </o:OfficeDocumentSettings>
    </xml>
    <![endif]-->
    </head>

    <body>
        <div class="es-wrapper-color">
            <!--[if gte mso 9]>
    			<v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t">
    				<v:fill type="tile" color="#eeeeee"></v:fill>
    			</v:background>
    		<![endif]-->
            <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0">
                <tbody>
                    <tr>
                        <td class="esd-email-paddings" valign="top">
                            <table class="es-content esd-footer-popover" cellspacing="0" cellpadding="0" align="center">
                                <tbody>
                                    <tr>
                                        <td class="esd-stripe" align="center">
                                            <table class="es-content-body" width="600" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center">
                                                <tbody>
                                                    <tr>
                                                        <td class="esd-structure es-p40t es-p35b es-p35r es-p35l" esd-custom-block-id="7685" style="background-color: #09090a; background-image: url(https://media.istockphoto.com/id/501655522/photo/star-field-at-night.jpg?b=1&s=170667a&w=0&k=20&c=nOIdRNElZtKxCxADiYoMXcATBMOYRtQy7P3V_txHjss=); background-position: left top; background-repeat: no-repeat no-repeat;" bgcolor="#09090a" align="left" background="https://media.istockphoto.com/id/501655522/photo/star-field-at-night.jpg?b=1&s=170667a&w=0&k=20&c=nOIdRNElZtKxCxADiYoMXcATBMOYRtQy7P3V_txHjss=">
                                                            <table width="100%" cellspacing="0" cellpadding="0">
                                                                <tbody>
                                                                    <tr>
                                                                        <td class="esd-container-frame" width="530" valign="top" align="center">
                                                                            <table width="100%" cellspacing="0" cellpadding="0">
                                                                                <tbody>
                                                                                    <tr>
                                                                                        <td class="esd-block-text es-p15b" align="center">
                                                                                            <h2 style="color: #f2f1e1; font-family: 'open sans', 'helvetica neue', helvetica, arial, sans-serif;">Welcom to COZMOS</h2>
                                                                                        </td>
                                                                                    </tr>
                                                                                    <tr>
                                                                                        <td class="esd-block-text es-m-txt-l es-p20t" align="center">
                                                                                            <h3 style="font-size: 18px; color: #f2f1e1;">Hello {first_name},</h3>
                                                                                        </td>
                                                                                    </tr>
                                                                                    <tr>
                                                                                        <td class="esd-block-text es-p15t es-p10b" align="center">
                                                                                            <p style="font-size: 16px; color: #f2f1e1;">Your Verification Code is</p>
                                                                                        </td>
                                                                                    </tr>
                                                                                    <tr>
                                                                                        <td align="center" class="esd-block-text">
                                                                                            <p style="color: #f9f22c; font-size: 46px;">{code}</p>
                                                                                        </td>
                                                                                    </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </body>

    </html>
            '''

def generate_verification_code():
    digits = "0123456789"
    code = ""

    for i in range(6):
        code += digits[math.floor(random.random() * 10)]

    return code



router = APIRouter(
    prefix= '/investor',
    tags= ['investor']
)


@router.get('/')
def all(db: Session = Depends(get_db)):
    return investor.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create(request: schemas.Investor, db: Session = Depends(get_db)):
    code = generate_verification_code()
    emails = [request.email]
    template = get_email(request.first_name, code)
    message = MessageSchema(
        subject="Verification Code",
        recipients=emails,
        body=template,
        subtype="html"
    )

    fm = FastMail(conf)
    await fm.send_message(message)
    hashed = hashlib.sha256(code.encode()).hexdigest()

    return investor.create(db, request, hashed)


@router.delete('/{id}', status_code=status.HTTP_202_ACCEPTED)
def destroy(id, db: Session = Depends(get_db)):
    return investor.delete(db, id)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_buyer(id, request: schemas.Investor, db: Session = Depends(get_db)):
    return investor.update(db, request, id)

@router.get('/{id}', status_code=200)
def show(id, db: Session = Depends(get_db)):
    return investor.get_id(db, id)

@router.post('/verify/{id}', status_code=200)
def verify(id, code: str, db: Session = Depends(get_db)):
    hashed = hashlib.sha256(code.encode()).hexdigest()
    return investor.verify_code(db, id, hashed)

