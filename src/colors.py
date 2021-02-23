class Colors:
    titleBarColor = (27, 29, 34)
    sideBarColor = (27, 29, 35)
    infoBarColor = (39, 44, 54)
    statusBarColor = (33, 37, 43)
    contentFrameColor = (44, 49, 60)

    cardColor = (54, 57, 63)
    colorAccent = (0, 132, 255)

    menuButtonColor = sideBarColor
    menuButtonColorHover = (36, 38, 45)
    menuButtonBorderColorHover = (150, 150, 150)

    wordInputBackground = (38, 44, 56)
    dialogBackground = statusBarColor

    textColor = (210, 210, 210)

    @staticmethod
    def get_color(color):
        return f'rgb({color[0]},{color[1]},{color[2]})'
