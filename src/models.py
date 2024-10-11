from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

    
class Personajes(db.Model):
    Id_Personajes = db.Column(db.Integer, primary_key=True)

    Birthline = db.Column(db.Integer, nullable=False)
    Gender = db.Column(db.String(250), nullable=False)
    Height= db.Column(db.Integer, nullable=False)
    Skin_color = db.Column(db.String(250), nullable=False)
    Eye_color = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Personajes %r>' % self.Id_Personajes

    def serialize(self):
        return {
            "id": self.Id_Personajes,
            "Birthline": self.Birthline,
            "Gender": self.Gender,
            "Height": self.Height,
            "Skin_color": self.Skin_color,
            "Eye_color": self.Eye_color,

            

            # do not serialize the password, its a security breach
        }
    
class Planetas(db.Model):
    ID_Planeta = db.Column(db.Integer, primary_key=True)
    Rotation_Period = db.Column(db.Integer, nullable=False)
    Orbital_Period = db.Column(db.Integer, nullable=False)
    Gravity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Planeta %r>' % self.Rotation_Period

    def serialize(self):
        return {
            "id": self.ID_Planeta,
            "Rotation_Period": self.Rotation_Period,
            "Orbital_Period": self.Orbital_Period,
            "Gravity": self.Gravity,
    
            # do not serialize the password, its a security breach
        }
    
class Usuario(db.Model):
    ID_Usuario = db.Column (db.Integer, primary_key=True)
    Nombre = db.Column(db.String(250), nullable=False)
    Apellido = db.Column(db.String(250), nullable=False)
    Correo = db.Column(db.String(250), nullable=False)
    Password = db.Column(db.String(250), nullable=False)
    # planetas_favoritos = db.relationship('Datos_Favoritos', backref='usuario_planeta', lazy=True)
    # personajes_favoritos = db.relationship('Datos_Favoritos', backref='usuario_personaje', lazy=True)


    def __repr__(self):
        return '<Usuario %r>' % self.Nombre

    def serialize(self):
        return {
        "ID_Usuario": self.ID_Usuario,
        "Nombre": self.Nombre,
        "Apellido": self.Apellido,
        "Correo": self.Correo,
        # do not serialize the password, its a security breach
    }
   #codigo comentando 
class Datos_Favoritos(db.Model):
    id_Favoritos = db.Column(db.Integer, primary_key=True)
    user_Id = db.Column(db.Integer, db.ForeignKey('usuario.ID_Usuario'))
    user= db.relationship('Usuario', backref='datos_favoritos')
    Planeta_ID = db.Column(db.Integer, db.ForeignKey('planetas.ID_Planeta'))
    Personajes_Id = db.Column(db.Integer, db.ForeignKey('personajes.Id_Personajes'))
    planeta = db.relationship('Planetas', backref='datos_favoritos')
    personajes = db.relationship('Personajes', backref='datos_favoritos')


    def __repr__(self):
        return '<Datos_Favoritos %r>' % self.id_Favoritos
    
def serialize(self):
    return {
        "id_Favoritos": self.id_Favoritos,
        "user_Id": self.user_Id,
        "Planeta_ID": self.Planeta_ID,
        "Personajes_Id": self.Personajes_Id,
    }