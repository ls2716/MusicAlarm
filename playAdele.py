from webbot import Browser

from config import user, password

web = Browser()
web.go_to('google.com')
web.type('spotify web player')  # or web.press(web.Key.SHIFT + 'hello its me')
web.press(web.Key.ENTER)
web.click('Spotify - Web Player')
web.click('LOG IN')
web.click('LOG IN WITH FACEBOOK')
web.type(user, into='Email')
web.type(password, into='Password')
web.click('Log In')
web.click('Great Movie Theme Songs')
web.click('PLAY')