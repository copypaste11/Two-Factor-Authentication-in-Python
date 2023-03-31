import pyotp
import qrcode

key = 'coPyPasteKey'

uri = pyotp.totp.TOTP(key).provisioning_uri(name='coPyPaste', issuer_name='coPyPaste_App')

print(uri)