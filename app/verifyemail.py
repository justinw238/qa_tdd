import re


class VerifyEmail:

    def verifyEmail(self, email):
        regex = r"^.+?@.+?\..{2,3}$"
        match = re.search(regex, email)
        if(match):
            return True
        else:
            return False


