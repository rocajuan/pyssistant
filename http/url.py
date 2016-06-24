import requests
import urllib2

# Url class that breaks down the desired url.  
# It can verify the url is active and will return the response code.
class Url(object):
	def __init__(self, url, action=None):
		self.protocol = url.split("://")[0] if "http" in url[:4] else "http"
		self.levels = url.strip(self.protocol + "://").split("/")
		self.domain = self.levels[0]
		self.url = url if self.protocol in url else "://".join([self.protocol, url])
		self.status = self.verify()

	def __repr__(self):
		return "<Url (%s) protocol:%s domain:%s status:%s levels:%s>" % (self.url, self.protocol, self.domain, self.status, self.levels)

	def get(self):
		print self

	def verify(self):
		try:
			req = requests.get(self.url)
			self.status = req.status_code
		except:
			self.status = None
		return self.status

	def verify2(self):
		try:
			url = urllib2.urlopen(self.url)
			print url.getcode()
		except urllib2.HTTPError, e:
			print (e.code)
		except urllib2.URLError, e:
			print (e.args)

#TODO: class ImageUrl(Url)
