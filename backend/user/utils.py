import pyotp 


def create_OTP_token(user):
    token = pyotp.random_base32(chars=user.pk)
    return user, token
