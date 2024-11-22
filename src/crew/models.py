from flask                         import current_app
from flask_security.models         import fsqla_v3                                               as fsqla
from sqlalchemy.orm                import DeclarativeBase,MappedAsDataclass,Mapped,mapped_column
from sqlalchemy_imageattach.entity import Image,image_attachment

current_app.user_datastore = SQLAlchemyUserDatastore(current_app.database,User,Role)

class Role(current_app.database.Model, fsqla.FsRoleMixin):
    pass
class User(current_app.database.Model, fsqla.FsUserMixin):
    pass

class CrewMember(User):
    __tablename__ = "crew_members"
    nickname:   Mapped[str] = mapped_column(primary_key=True)
    rank:       Mapped[str]
    first_name: Mapped[str]
    last_name:  Mapped[str]

current_app.database.create_all()
