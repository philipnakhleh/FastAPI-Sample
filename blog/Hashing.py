from passlib.context import CryptContext


pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')

class Hash():
    def bcrypt(self, password: str):
        return pwd_cxt.hash(password)

    def verify(self, hashed, plain):
        return pwd_cxt.verify(plain, hashed)