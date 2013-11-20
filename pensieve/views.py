from pensieve import pensieve

@pensieve.route('/')
@pensieve.route('/index')
def index():
    return "Hello, World!"