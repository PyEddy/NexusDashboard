APP_THEME = "Blue"
FONT_STYLE = "Nunito"
MODE = "Dark"


def newTheme(theme):
    with open("static/scss/site.scss", 'r') as f:
        lines = f.readlines()
        newline = "        \"primary\": " + theme + "," + "\n"
    with open("static/scss/site.scss", 'w') as f:
        lines[2] = newline
        f.writelines(lines)
        f.close()


def newFont2(font_url, font):
    with open("static/scss/site.scss", 'r') as f:
        lines = f.readlines()
        importline = "@import url(" + font_url + ");" + "\n"
        bodyline = "body { font-family:'" + font + "', Helvetica, Arial, sans-serif; }" + "\n"
    with open("static/scss/site.scss", 'w') as f:
        lines[10] = importline
        lines[12] = bodyline
        f.writelines(lines)
        f.close()


def openFile(theme, hover_background, hover_color):
    with open("static/site.css", 'r') as f:
        lines = f.readlines()
        newline = "  background-color: " + theme + " !important; }" + "\n"
        borderline = "  border-color: " + theme + " !important; }" + "\n"
        buttonline = "  background-color: " + theme + ";" + "\n"
        border_color = "  border-color: " + theme + "; }" + "\n"
        hover_background_color = "    background-color: " + hover_background + ";" + "\n"
        hover_color1 = "    border-color: " + hover_color + "; }" + "\n"
    with open("static/site.css", 'w') as f:
        lines[4540] = newline
        lines[4648] = borderline
        lines[1715] = buttonline
        lines[1716] = border_color
        lines[1719] = hover_background_color
        lines[1720] = hover_color1
        f.writelines(lines)
        f.close()


def newFont(font_url, font):
    with open("static/site.css", 'r') as f:
        lines = f.readlines()
        importline = "@import url(" + font_url + ");" + "\n"
        bodyline = "  font-family: '" + font + "', Helvetica, Arial, sans-serif; }" + "\n"
    with open("static/site.css", 'w') as f:
        lines[6] = importline
        lines[7005] = bodyline
        f.writelines(lines)
        f.close()


def newMode(mode, text_color):
    with open("static/site.css", 'r') as f:
        lines = f.readlines()
        modeLine = "  background-color: " + mode + " !important; }" + "\n"
        textLine = "  color: " + text_color + " !important; }" + "\n"
    with open("static/site.css", 'w') as f:
        lines[4596] = modeLine
        lines[6910] = textLine
        f.writelines(lines)
        f.close()


if MODE == "Dark":
    dark_mode = "#343a40"
    text_color = "#FFFFFF"
    newMode(dark_mode, text_color)
if MODE == "Light":
    light_mode = "#FFFFFF"
    text_color = "#000000"
    newMode(light_mode, text_color)

if APP_THEME == "Blue":
    HEX_CODE = "#005ac2"
    HOVER_BACKGROUND = "#00489c"
    HOVER_COLOR = "#00428f"
    openFile(HEX_CODE, HOVER_BACKGROUND, HOVER_COLOR)
    newTheme(HEX_CODE)
if APP_THEME == "Red":
    HEX_CODE = "#FF0000"
    HOVER_BACKGROUND = "#d90000"
    HOVER_COLOR = "#cc0000"
    openFile(HEX_CODE, HOVER_BACKGROUND, HOVER_COLOR)
    newTheme(HEX_CODE)
if APP_THEME == "Green":
    HEX_CODE = "#006400"
    HOVER_BACKGROUND = "#003e00"
    HOVER_COLOR = "#003100"
    openFile(HEX_CODE, HOVER_BACKGROUND, HOVER_COLOR)
    newTheme(HEX_CODE)
if APP_THEME == "Yellow":
    HEX_CODE = "#FFCC00"
    HOVER_BACKGROUND = "#d9ad00"
    HOVER_COLOR = "#cca300"
    openFile(HEX_CODE, HOVER_BACKGROUND, HOVER_COLOR)
    newTheme(HEX_CODE)
if APP_THEME == "Black":
    HEX_CODE = "#000000"
    HOVER_BACKGROUND = "black"
    HOVER_COLOR = "black"
    openFile(HEX_CODE, HOVER_BACKGROUND, HOVER_COLOR)
    newTheme(HEX_CODE)
if APP_THEME == "Purple":
    HEX_CODE = "#A020F0"
    HOVER_BACKGROUND = "#8c0fdb"
    HOVER_COLOR = "#850ecf"
    openFile(HEX_CODE, HOVER_BACKGROUND, HOVER_COLOR)
    newTheme(HEX_CODE)

if FONT_STYLE == "Nunito":
    URL = "https://fonts.googleapis.com/css?family=Nunito:700"
    FONT_NAME = "Nunito"
    newFont(URL, FONT_NAME)
    newFont2(URL, FONT_NAME)
if FONT_STYLE == "Grape Nuts":
    URL = "https://fonts.googleapis.com/css2?family=Grape+Nuts&display=swap"
    FONT_NAME = "Grape Nuts"
    newFont(URL, FONT_NAME)
    newFont2(URL, FONT_NAME)
if FONT_STYLE == "Odibee Sans":
    URL = "https://fonts.googleapis.com/css2?family=Odibee+Sans&display=swap"
    FONT_NAME = "Odibee Sans"
    newFont(URL, FONT_NAME)
    newFont2(URL, FONT_NAME)
if FONT_STYLE == "Righteous":
    URL = "https://fonts.googleapis.com/css2?family=Righteous&display=swap"
    FONT_NAME = "Righteous"
    newFont(URL, FONT_NAME)
    newFont2(URL, FONT_NAME)

print("Updated Dashboard Theme")



