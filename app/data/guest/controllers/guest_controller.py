""" Routes for the endpoint 'guest'"""

from flask import Blueprint, request
from marshmallow import ValidationError

from data.guest.models import GuestModel
from data.guest.schemas import GuestSchema
from shared import db

NAME = 'guest'

guest_blueprint = Blueprint(f"{NAME}_guest_blueprint", __name__)


@guest_blueprint.post(f"/{NAME}/guest")
def post_guest():
    """POST route code goes here"""
    payload = request.get_json()
    
    # Ajoutez le traitement pour extraire le nom d'utilisateur et le mot de passe du payload
    username = payload.get("name")
    password = payload.get("password")
    
    # Créez une instance GuestModel avec les champs supplémentaires
    try:
        entity: GuestModel = GuestModel(username=username, password=password)
        # Vous pouvez également utiliser GuestSchema().load(payload) avec le schéma approprié
    except ValidationError as error:
        return jsonify({"message": f"The payload doesn't correspond to a valid GuestModel: {error}"}), 400
    
    db.session.add(entity)
    db.session.commit()
    
    # Retournez les informations de l'entité nouvellement créée avec un message de succès
    response_data = {
        "message": "Successfully created a new guest",
        "username": entity.username,
    }
    
    return jsonify(response_data), 200

@guest_blueprint.delete(f"/{NAME}/guest/<int:id>")
def delete_guest(id: int):
    """DELETE route code goes here"""
    # Recherchez l'entité à supprimer dans la base de données
    entity = GuestModel.query.get(id)

    # Vérifiez si l'entité existe
    if not entity:
        return jsonify({"message": f"Guest with ID {id} not found"}), 404

    # Supprimez l'entité de la base de données
    db.session.delete(entity)
    db.session.commit()

    # Retournez un message de succès
    return jsonify({"message": f"Successfully deleted guest with ID {id}"}), 200


@guest_blueprint.put(f"/{NAME}/guest/<int:id>")
def put_guest(id: int):
    """PUT route code goes here"""
    # Recherchez l'entité à mettre à jour dans la base de données
    entity = GuestModel.query.get(id)

    # Vérifiez si l'entité existe
    if not entity:
        return jsonify({"message": f"Guest with ID {id} not found"}), 404

    # Obtenez les données de mise à jour depuis la requête JSON
    update_data = request.get_json()

    # Mettez à jour les champs de l'entité avec les nouvelles données
    for key, value in update_data.items():
        setattr(entity, key, value)

    # Committez les changements à la base de données
    db.session.commit()

    # Retournez un message de succès avec les données mises à jour
    return jsonify({
        "message": f"Successfully updated guest with ID {id}",
        "updated_data": {"id": entity.id, "username": entity.username, "password": entity.password}
    }), 200


@guest_blueprint.patch(f"/{NAME}/guest/<int:id>")
def patch_guest(id: int):
    """PATCH route code goes here"""
    # Recherchez l'entité à mettre à jour dans la base de données
    entity = GuestModel.query.get(id)

    # Vérifiez si l'entité existe
    if not entity:
        return jsonify({"message": f"Guest with ID {id} not found"}), 404

    # Obtenez les données de mise à jour partielles depuis la requête JSON
    patch_data = request.get_json()

    # Mettez à jour les champs de l'entité avec les nouvelles données
    for key, value in patch_data.items():
        setattr(entity, key, value)

    # Committez les changements à la base de données
    db.session.commit()

    # Retournez un message de succès avec les données mises à jour
    return jsonify({
        "message": f"Successfully patched guest with ID {id}",
        "patched_data": {"id": entity.id, "username": entity.username, "password": entity.password}
    }), 200
