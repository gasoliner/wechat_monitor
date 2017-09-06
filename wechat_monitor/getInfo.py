
def getPipeLineInfo():
    file = open('f:\\pipeLineInfo')
    result = file.read().decode('utf-8')
    file.close()
    return result

def getPageProcessorInfo():
        file = open('f:\\pageProcessorInfo')
        result = file.read().decode('utf-8')
        file.close()
        return result
