from flask                    import current_app
from flask_security.models    import fsqla_v3                                               as fsqla
from sqlalchemy               import ForeignKey
from sqlalchemy.orm           import DeclarativeBase,MappedAsDataclass,Mapped,mapped_column,relationship
from flask_security           import SQLAlchemyUserDatastore
from flask_admin.contrib.sqla import ModelView

class CrewMember(current_app.database.Model):
    __tablename__ = "crew_members"
    user:     Mapped[str] = mapped_column(ForeignKey("user.username"))
    nickname: Mapped[str] = mapped_column(primary_key=True)
    rank:     Mapped[str] = mapped_column(nullable=False)

current_app.database.create_all()
