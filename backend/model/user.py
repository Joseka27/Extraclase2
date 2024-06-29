class User:
    def __init__(self, user_id,tema, nombre, comentario):
        self.user_id = user_id
        self.tema = tema
        self.nombre = nombre
        self.comentario = comentario

    def serialize(self):
        return {
            'user_id': self.user_id,
            'tema' : self.tema,
            'nombre': self.nombre,
            'comentario': self.comentario
        }
