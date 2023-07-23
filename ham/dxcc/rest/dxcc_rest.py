from flask import Flask
from flask_classful import FlaskView
from ham.dxcc import DxccAll

dx = DxccAll()
print("Dx initialized")
# we'll make a list to hold some quotes for our app
quotes = [
    "A noble spirit embiggens the smallest man! ~ Jebediah Springfield",
    "If there is a way to do it better... find it. ~ Thomas Edison",
    "No one knows what he can do till he tries. ~ Publilius Syrus",
]

app = Flask(__name__)


class QuotesView(FlaskView):
    # http://localhost:5000/quotes/
    def index(self):
        return "<br>".join(quotes)


class CallView(FlaskView):
    def index(self):
     # http://localhost:5000/call
        return {"call": "callsign"}

    def get(self, call):
     # http://localhost:5000/call/M0FGC/
        if call is not None:
            print(f"call is {call}")
            dxo = dx.find(call)
            return dxo.todict()
        else:
            return "Not Found", 404


QuotesView.register(app)
CallView.register(app)

if __name__ == "__main__":
    app.run()
