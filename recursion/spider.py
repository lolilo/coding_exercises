# keys are pseudo-urls, values are pseudo-HTML
site = {
	'a': ['b', 'c', 'f'],
	'b': ['a', 'd', 'e', 'f'],
	'c': ['g'],
	'd': [],
	'e': [],
	'f': [],
	'g': ['c']
}

class Spider(object):
	def __init__(self):
		self.seen = {}

	def find_links(self, html):
		return html

	def get_html(self, url):
		return site[url]

	# prints out all url, html pairs that can be reached from the start url
	def crawl(self, start):
		html = self.get_html(start)
		self.seen[start] = True

		url_list = self.find_links(html)
		print start, html

		for url in url_list:
			if url not in self.seen:
				self.crawl(url)

if __name__ == "__main__":
	spider = Spider()
	spider.crawl('a')