from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup


try:
    html = urlopen("http://www.pythonscrapingnoexit.com")
except HTTPError as e:
    print(e)
    # return null, break,あるいはプランBを実行
except URLError as e:
    print("The server coould not be found!")
else:
    print("IT worked!")
