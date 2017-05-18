from flask import Flask, render_template
import requests
from xml.etree import ElementTree as ET
from itertools import zip_longest
app = Flask(__name__)

@app.route('/')
def cat():
	url = 'http://thecatapi.com/api/images/get?format=xml&results_per_page=9&type=gif'
	xml = requests.get(url)
	root = ET.fromstring(xml.content)
	urls = [ele.text for ele in root.findall('./data/images/image/url')]
	urls_grouped = grouper(urls, 3) # devide 9 usls into 3 groups
	return render_template('cat.html', urls=urls_grouped)

def grouper(iterable, n, fillvalue=None):
	args = [iter(iterable)] * n
	return zip_longest(*args, fillvalue=fillvalue)

if __name__ == "__main__":
	app.run()