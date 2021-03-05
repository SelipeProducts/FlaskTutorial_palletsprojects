from markupsafe import Markup


def markup_safe():
  print()
  safe = Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>'

  #Markup(u'<strong>Hello &lt;blink&gt;hacker&lt;/blink&gt;!</strong>')
  print(safe)

def markup_escape():
  escape = Markup.escape('<blink>hacker</blink>')

  #Markup(u'&lt;blink&gt;hacker&lt;/blink&gt;')
  print(escape)

def markup_strip():
  strip = Markup('<em>Marked up</em> &raquo; HTML').striptags()
  
  #u'Marked up \xbb HTML'
  print(strip)


markup_safe()
print()
markup_escape()
print()
markup_strip()
