# _input = raw_input("link or text: ")

# imports
from bs4 import BeautifulSoup
import urllib2
import re

# *************************************************************************** #

def to_text(website): 
  """Rips visible elments __main__"""
  # texts = get_html(website)
  # visible_text = filter(visible, texts)
  # rip = "".join(visible_text)
  # return "".join(rip)
  text = urllib2.urlopen("http://boilerpipe-web.appspot.com/extract?url="+ website + "&output=text")
  return text.read()

   
# *************************************************************************** #

def get_html(website):
  """Rips the body text from the page"""
  page = urllib2.urlopen(website)
  soup = BeautifulSoup(page)
  body = soup.body
  texts = body.findAll(text=True)
  return texts

# *************************************************************************** #

def visible(element):
  """For analysis of HTML tags & returns True for text visible to the user"""
  tags = ['style', 'script', '[document]', 'head', 'title']
  if element.parent.name in tags:
    return False
  # elif re.match('<!--.*-->', str(element)):
  #   return False
  # elif re.match('/*.*/', str(element)):
  #   return False
  else:
    return True

# *************************************************************************** #

def link_or_nah(_input):
  """link or just text"""
  x = list(_input)
  for element in x:
    if element == " ":
      return False
  return True

# *************************************************************************** #

# # if _input is a link call mains
# if link_or_nah(_input):
#   text = to_text(_input)
# else:
#   print "text is already good to go."
  # passt "text is already good to go."
#   pass