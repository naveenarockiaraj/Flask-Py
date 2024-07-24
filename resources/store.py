import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import StoreSchema


blp = Blueprint("Stores", "stores", description="Operations on stores")

@blp.route("/store/<string:store_id>")
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError:
            return abort(404, message="store not found")

    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "store delete."}
        except KeyError:
            abort(404, message="store not found")
        
@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return stores.values()
    
    @blp.arguments(StoreSchema)
    @blp.response(200, StoreSchema)
    def post(self, store_data):
        for store in stores.values():
            if store_data["name"] == store["name"]:
                abort(400, message=f"Store is already exist")

        store_id = uuid.uuid4().hex
        store = {**store_data, "id": store_id}
        stores[store_id] = store

        return store