from flask import Flask

app = Flask(__name__)

store = [
    {
        "name":"New store",
        "item":[
            {
                "name":"sofa",
                "price":25.5
            }
        ]
    }
]

@app.get("/store")
def get_store():
    return {"stores":store}