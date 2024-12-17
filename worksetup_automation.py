import webbrowser as wb

def workauto():
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    URLS = ("https://github.com/Ammarsaqib-programmer",
            "youtube.com")
    for url in URLS:
        wb.get(chrome_path).open(url)

workauto()
