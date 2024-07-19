class CustomException(Exception):
    def __init__(self, message, code=0):
        Exception.__init__(self)
        self.message = message
        self.code = code

    def __str__(self):
        return str(self.code) + ":" +self.message

try:
    raise CustomException("딱히 이유 없음")
except Exception as e:
    print(e)

# 0:딱히 이유 없음
