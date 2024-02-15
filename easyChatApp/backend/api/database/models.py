# where i store Database models
from datetime import datetime
from datetime import datetime as datetime_details
from enum import Enum, IntEnum, StrEnum

from .base import *
from .basetemplate import BaseTemplate

# utils when i want to test them on sqlite
UnsignedInt = Integer()
UnsignedInt = UnsignedInt.with_variant(INTEGER(unsigned=True), "mysql")
CustomBoolean = Integer()
CustomBoolean = CustomBoolean.with_variant(TINYINT, "mysql", "mariadb")


class User(Base, BaseTemplate):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(
        UnsignedInt, init=False, autoincrement=True, nullable=False, primary_key=True
    )
    nom: Mapped[str] = mapped_column(VARCHAR(50), init=True, nullable=False)
    number: Mapped[str] = mapped_column(VARCHAR(25), init=True, nullable=False)
    password: Mapped[str] = mapped_column(VARCHAR(255), init=True, nullable=False)


class Groupe(Base, BaseTemplate):
    __tablename__ = "groupe"
    id: Mapped[int] = mapped_column(
        UnsignedInt, init=False, autoincrement=True, nullable=False, primary_key=True
    )
    title: Mapped[str] = mapped_column(VARCHAR(50), init=True, nullable=False)
    description: Mapped[str] = mapped_column(VARCHAR(255), init=True, nullable=False)
    created_by: Mapped[int] = mapped_column(UnsignedInt, ForeignKey("user.id", onupdate="CASCADE", ondelete="SET NULL"), nullable=True)


class Message(Base, BaseTemplate):
    __tablename__ = "message"
    id: Mapped[int] = mapped_column(
        UnsignedInt, init=False, autoincrement=True, nullable=False, primary_key=True
    )
    content: Mapped[str] = mapped_column(VARCHAR(255), init=True, nullable=False)
    send_by: Mapped[int] = mapped_column(UnsignedInt, nullable=False)
    send_to_user: Mapped[int] = mapped_column(UnsignedInt, ForeignKey("user.id", ondelete="CASCADE"), nullable=True)
    send_to_groupe: Mapped[int] = mapped_column(UnsignedInt, ForeignKey("groupe.id", ondelete="CASCADE"), nullable=True)

class UserInGroupe(Base, BaseTemplate):
    __tablename__ = "user_in_groupe"
    id: Mapped[int] = mapped_column(
        UnsignedInt, init=False, autoincrement=True, nullable=False, primary_key=True
    )
    user_id: Mapped[int] = mapped_column(UnsignedInt, ForeignKey("user.id", ondelete="CASCADE"), init=True, primary_key=True,)
    groupe_id: Mapped[int] = mapped_column(UnsignedInt, ForeignKey("groupe.id", ondelete="CASCADE"), init=True, primary_key=True)