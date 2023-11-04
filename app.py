from flask import Flask

app=Flask(__name__)
import route
route.set_route(app)
app.secret_key=route.secret_key(58)
if __name__=="__main__":
    app.run(debug=True)
