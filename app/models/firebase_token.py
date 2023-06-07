from ..extensions import db
from datetime import datetime
from .user import User

class FirebaseToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(80), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    def get_user(self):
        return User.query.get(self.user_id)
    
    @classmethod
    def register_token(model, current_user, token):
        ft = model.query.filter(model.token == token).first()
        if not ft:
            ft = model(user_id=current_user.id, token=token)
            db.session.add(ft)
        else:
            ft.user_id = current_user.id

        db.session.commit()

    @classmethod
    def unregister_token(model, current_user, token):
        ft = model.query.filter(model.token == token).first()

        # Preventing someone deleting randomly tokens
        if ft and ft.user_id == current_user.id:
            db.session.delete(ft)

        db.session.commit()
