from PIL import Image
from StringIO import StringIO
import requests
r = requests.get('http://img3.douban.com/view/movie_poster_cover/ipst/public/p1356576774.jpg')
i = Image.open(StringIO(r.content))
i.save('D:/new.jpg')