import praw
import threading

# Configuration start
username = 'Mkrah' # Your reddit username
password = '8996344' # Your reddit password
subredditName = 'MyTestPostSub' # Suberddit name (you must be a moderator)
stylesheetPath = './style.css' # Path to your stylesheet
clientID = 'ClientID' # Your app's ID
clientSecret = 'ClientSecret' # You app's secret
clientCallback = 'http://127.0.0.1:65010/authorize_callback'
# Configuration end

r = praw.Reddit('LiveStyle v0.1 by /u/Timbo_KZ')
r.set_oauth_app_info(client_id=clientID, client_secret=clientSecret, redirect_uri=clientCallback)
r.login(username, password)
def file_get_contents(filename):
    with open(filename) as f:
        return f.read()
def static_var(varname, value):
    def decorate(func):
        setattr(func, varname, value)
        return func
    return decorate
@static_var("oldStylesheet", "")
def update_stylesheet():
    threading.Timer(2.0, update_stylesheet).start()
    print("Checking CSS...")
    stylesheet = file_get_contents(stylesheetPath)
    if stylesheet != update_stylesheet.oldStylesheet:
        print("Updating CSS...")
        r.set_stylesheet(subredditName, stylesheet)
        update_stylesheet.oldStylesheet = stylesheet
    else:
        print("CSS is up to date.")
update_stylesheet()