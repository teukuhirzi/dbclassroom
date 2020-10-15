from app import db

class MyClassnya(db.Model):
    __tablename__ = 'view_myclass'

    # id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('murid.id_siswa'))
    class_id = db.Column(db.Integer, db.ForeignKey('kelas.id_kelas'), primary_key=True)
    full_name = db.Column(db.String())
    class_name = db.Column(db.String())

    def __init__(self, student_id, class_id, full_name, class_name ):
        self.student_id = student_id
        self.class_id = class_id
        self.full_name = full_name
        self.class_name = class_name

    def serialize(self):
        return {
            # 'id':self.id,
            'student_id':self.student_id,
            'class_id':self.class_id,
            'full_name':self.full_name,
            'class_name':self.class_name
        }