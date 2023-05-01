from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models
from typing import List
from ..database import get_db
from ..repository import seller
import math, random
from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
import hashlib

conf = ConnectionConfig(
    MAIL_USERNAME="no-reply@cozmos-space.com",
    MAIL_PASSWORD="Ov1fIA4T#R)F",
    MAIL_FROM="no-reply@cozmos-space.com",
    MAIL_PORT = 465,
    MAIL_SERVER="mail.cozmos-space.com",
    MAIL_FROM_NAME="no-reply",
    MAIL_STARTTLS = False,
    MAIL_SSL_TLS = True,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)

def get_email(first_name, code)->str:
    return f'''
            <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" style="font-family:arial, 'helvetica neue', helvetica, sans-serif">
 <head>
  <meta charset="UTF-8">
  <meta content="width=device-width, initial-scale=1" name="viewport">
  <meta name="x-apple-disable-message-reformatting">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta content="telephone=no" name="format-detection">
  <title>New message</title>
  <style type="text/css">
#outlook a {{
	padding:0;
}}
.es-button {{
	mso-style-priority:100!important;
	text-decoration:none!important;
}}
a[x-apple-data-detectors] {{
	color:inherit!important;
	text-decoration:none!important;
	font-size:inherit!important;
	font-family:inherit!important;
	font-weight:inherit!important;
	line-height:inherit!important;
}}
.es-desk-hidden {{
	display:none;
	float:left;
	overflow:hidden;
	width:0;
	max-height:0;
	line-height:0;
	mso-hide:all;
}}
.es-button-border:hover a.es-button, .es-button-border:hover button.es-button {{
	background:#56d66b!important;
}}
.es-button-border:hover {{
	border-color:#42d159 #42d159 #42d159 #42d159!important;
	background:#56d66b!important;
}}
@media only screen and (max-width:600px) {{p, ul li, ol li, a {{ line-height:150%!important }} h1, h2, h3, h1 a, h2 a, h3 a {{ line-height:120% }} h1 {{ font-size:30px!important; text-align:left }} h2 {{ font-size:24px!important; text-align:left }} h3 {{ font-size:20px!important; text-align:left }} .es-header-body h1 a, .es-content-body h1 a, .es-footer-body h1 a {{ font-size:30px!important; text-align:left }} .es-header-body h2 a, .es-content-body h2 a, .es-footer-body h2 a {{ font-size:24px!important; text-align:left }} .es-header-body h3 a, .es-content-body h3 a, .es-footer-body h3 a {{ font-size:20px!important; text-align:left }} .es-menu td a {{ font-size:14px!important }} .es-header-body p, .es-header-body ul li, .es-header-body ol li, .es-header-body a {{ font-size:14px!important }} .es-content-body p, .es-content-body ul li, .es-content-body ol li, .es-content-body a {{ font-size:14px!important }} .es-footer-body p, .es-footer-body ul li, .es-footer-body ol li, .es-footer-body a {{ font-size:14px!important }} .es-infoblock p, .es-infoblock ul li, .es-infoblock ol li, .es-infoblock a {{ font-size:12px!important }} *[class="gmail-fix"] {{ display:none!important }} .es-m-txt-c, .es-m-txt-c h1, .es-m-txt-c h2, .es-m-txt-c h3 {{ text-align:center!important }} .es-m-txt-r, .es-m-txt-r h1, .es-m-txt-r h2, .es-m-txt-r h3 {{ text-align:right!important }} .es-m-txt-l, .es-m-txt-l h1, .es-m-txt-l h2, .es-m-txt-l h3 {{ text-align:left!important }} .es-m-txt-r img, .es-m-txt-c img, .es-m-txt-l img {{ display:inline!important }} .es-button-border {{ display:inline-block!important }} a.es-button, button.es-button {{ font-size:18px!important; display:inline-block!important }} .es-adaptive table, .es-left, .es-right {{ width:100%!important }} .es-content table, .es-header table, .es-footer table, .es-content, .es-footer, .es-header {{ width:100%!important; max-width:600px!important }} .es-adapt-td {{ display:block!important; width:100%!important }} .adapt-img {{ width:100%!important; height:auto!important }} .es-m-p0 {{ padding:0px!important }} .es-m-p0r {{ padding-right:0px!important }} .es-m-p0l {{ padding-left:0px!important }} .es-m-p0t {{ padding-top:0px!important }} .es-m-p0b {{ padding-bottom:0!important }} .es-m-p20b {{ padding-bottom:20px!important }} .es-mobile-hidden, .es-hidden {{ display:none!important }} tr.es-desk-hidden, td.es-desk-hidden, table.es-desk-hidden {{ width:auto!important; overflow:visible!important; float:none!important; max-height:inherit!important; line-height:inherit!important }} tr.es-desk-hidden {{ display:table-row!important }} table.es-desk-hidden {{ display:table!important }} td.es-desk-menu-hidden {{ display:table-cell!important }} .es-menu td {{ width:1%!important }} table.es-table-not-adapt, .esd-block-html table {{ width:auto!important }} table.es-social {{ display:inline-block!important }} table.es-social td {{ display:inline-block!important }} .es-desk-hidden {{ display:table-row!important; width:auto!important; overflow:visible!important; max-height:inherit!important }} }}
</style>
 </head>
 <body style="width:100%;font-family:arial, 'helvetica neue', helvetica, sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0">
  <div class="es-wrapper-color" style="background-color:#F6F6F6"><!--[if gte mso 9]>
			<v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t">
				<v:fill type="tile" color="#f6f6f6"></v:fill>
			</v:background>
		<![endif]-->
   <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;padding:0;Margin:0;width:100%;height:100%;background-repeat:repeat;background-position:center top;background-color:#F6F6F6">
     <tr>
      <td valign="top" style="padding:0;Margin:0">
       <table cellpadding="0" cellspacing="0" class="es-content" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%">
         <tr>
          <td align="center" style="padding:0;Margin:0">
           <table class="es-content-body" align="center" cellpadding="0" cellspacing="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:transparent;width:600px">
             <tr>
              <td align="left" background="https://mlcogb.stripocdn.email/content/guids/CABINET_3be0ebf236f28d929f129c4c162361f41000377be4eb921aa1d369284c5b3290/images/group_11228.png" style="padding:0;Margin:0;padding-top:20px;padding-right:20px;padding-left:25px;background-image:url(https://mlcogb.stripocdn.email/content/guids/CABINET_3be0ebf236f28d929f129c4c162361f41000377be4eb921aa1d369284c5b3290/images/group_11228.png);background-position:center top;background-repeat:no-repeat no-repeat">
               <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                 <tr>
                  <td align="center" valign="top" style="padding:0;Margin:0;width:555px">
                   <table cellpadding="0" cellspacing="0" width="100%" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                     <tr>
                      <td align="left" style="Margin:0;padding-right:15px;padding-left:25px;padding-top:30px;padding-bottom:40px;font-size:0px"><img class="adapt-img" src="https://raw.githubusercontent.com/philipnakhleh/Repo/main/logo.png" alt style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic" width="175"></td>
                     </tr>
                     <tr>
                      <td align="center" style="Margin:0;padding-bottom:25px;padding-top:40px;padding-left:40px;padding-right:40px;font-size:0px"><img class="adapt-img" src="https://raw.githubusercontent.com/philipnakhleh/Repo/main/coza.png" alt style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic" width="475"></td>
                     </tr>
                     <tr>
                      <td align="center" style="padding:0;Margin:0;padding-top:40px;padding-bottom:40px"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:26px;color:#f1f1f1;font-size:17px">Regards from spaceman, Here is you <strong>Verification code</strong></p></td>
                     </tr>
                     <tr>
                      <td align="center" style="padding:40px;Margin:0"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:50px;color:#f1f1f1;font-size:33px"><strong>{code}</strong></p></td>
                     </tr>
                   </table></td>
                 </tr>
               </table></td>
             </tr>
           </table></td>
         </tr>
       </table></td>
     </tr>
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
    prefix= '/seller',
    tags= ['seller']
)


@router.get('/', response_model=List[schemas.Seller])
def all(db: Session = Depends(get_db)):
    return seller.get_all(db)



@router.post('/', status_code=status.HTTP_201_CREATED)
async def create(request: schemas.Seller, db: Session = Depends(get_db)):
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

    return seller.create(db, request, hashed)




@router.delete('/{id}', status_code=status.HTTP_202_ACCEPTED)
def destroy(id, db: Session = Depends(get_db)):
    return seller.delete(db, id)



@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_seller(id, request: schemas.Seller, db: Session = Depends(get_db)):
    return seller.update_seller(db, request, id)


@router.get('/{id}', status_code=200, response_model=schemas.Seller)
def show(id, db: Session = Depends(get_db)):
    return seller.get_id(db, id)

@router.post('/verify/{id}', status_code=200)
def verify(id, code: str, db: Session = Depends(get_db)):
    hashed = hashlib.sha256(code.encode()).hexdigest()
    return seller.verify_code(db, id, hashed)