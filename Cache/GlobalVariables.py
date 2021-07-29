import datetime
class MetaCache(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaCache, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
class GlobalVariables(metaclass=MetaCache):
    __refreshToken: str
    __dormitoryId: str
    __pullCloudStatus: int
    __numberOfPullApiSuccess: int

    def __init__(self):
        self.__dormitoryId = ""
        self.__refreshToken = ""
        self.__pullCloudStatus = 0
        self.__numberOfPullApiSuccess = 0

    @property
    def NumberOfPullApiSuccess(self):
        return self.__numberOfPullApiSuccess

    @NumberOfPullApiSuccess.setter
    def NumberOfPullApiSuccess(self, numberOfPullApiSuccess: int):
        self.__numberOfPullApiSuccess = numberOfPullApiSuccess

    @property
    def RefreshToken(self):
        return self.__refreshToken

    @RefreshToken.setter
    def RefreshToken(self, refreshToken: str):
        self.__refreshToken = refreshToken

    @property
    def DormitoryId(self):
        return self.__dormitoryId
    
    @DormitoryId.setter
    def DormitoryId(self, DormitoryId: str):
        self.__dormitoryId = DormitoryId
     
    @property
    def PullCloudErrorState(self):
        return self.__pullCloudStatus
        
    @PullCloudErrorState.setter
    def PullCloudErrorState(self, pullCloudStatus: int):
        self.__pullCloudStatus = pullCloudStatus
