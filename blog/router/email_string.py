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