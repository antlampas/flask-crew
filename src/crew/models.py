from flask                    import current_app
from flask_security.models    import fsqla_v3                                               as fsqla
from sqlalchemy.orm           import DeclarativeBase,MappedAsDataclass,Mapped,mapped_column
from flask_security           import SQLAlchemyUserDatastore
from flask_admin.contrib.sqla import ModelView

class CrewMember(User):
    __tablename__ = "crew_members"
    nickname:   Mapped[str] = mapped_column(primary_key=True)
    rank:       Mapped[str]
    first_name: Mapped[str]
    last_name:  Mapped[str]

current_app.database.create_all()

current_app.admin.add_view(ModelView(CrewMember,current_app.database.session))
