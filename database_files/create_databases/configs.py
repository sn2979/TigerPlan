import requests
import json
import base64

class Configs:
    def __init__(self):
        self.CONSUMER_KEY = "qV3vQDkDfg6OKYEqTp3LYJvUdN0a"
        self.CONSUMER_SECRET = "nX031MduByHplmGLWEia4MfNs7Aa"
        self.BASE_URL="https://api.princeton.edu:443/student-app"
        self.COURSE_COURSES="/courses/courses"
        self.COURSE_TERMS="/courses/terms"
        self.REFRESH_TOKEN_URL="https://api.princeton.edu:443/token"
        self._refreshToken(grant_type="client_credentials")
        self.DATABASE_URL="mongodb+srv://tigerplan333:TigerPlan123!@tig\
            erplandata.yyrhywn.mongodb.net/?retryWrites=true&w=majority\
            &appName=TigerPlanData"

    def _refreshToken(self, **kwargs):
        req = requests.post(
            self.REFRESH_TOKEN_URL, 
            data=kwargs, 
            headers={
                "Authorization": "Basic " + base64.b64encode(bytes(self.CONSUMER_KEY + ":" + self.CONSUMER_SECRET, "utf-8")).decode("utf-8")
            },
        )
        text = req.text
        response = json.loads(text)
        self.ACCESS_TOKEN = response["access_token"]
