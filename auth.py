
import pyotp

key = 'coPyPasteKey'

totp = pyotp.TOTP(key)

while True:
	print(totp.verify(input('Enter code: ')))