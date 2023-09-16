APP_MAJOR = 1
APP_MINOR = 0
APP_PATCH = 0

DB_MAJOR = 1
DB_MINOR = 0
DB_PATCH = 0

def getAppVersion():
    return str(APP_MAJOR) + '.' + str(APP_MINOR) + '.' + str(APP_PATCH)


def getDBVersion():
    return str(DB_MAJOR) + '.' + str(DB_MINOR) + '.' + str(DB_PATCH)