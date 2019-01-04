camera={"camera","camera-quality","camera quality","picture quality","picture-quality"}
battery={"battery life","battery","power","standby"}
processor={"processor","performance","speed","power"}
def getNoun(word):
    if word in camera:
        return "camera"
    elif word in battery:
        return "battery"
    elif word in processor:
        return "processor"
    else:
        return ""
