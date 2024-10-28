import enum
from sqlalchemy import DECIMAL, BigInteger, ForeignKey, create_engine
from sqlalchemy import String, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import Base
from db.utils import CreatedModel

class LanguageEnum(str, enum.Enum):
        uz = "O'zbek 🇺🇿"
        ru = "Русский 🇷🇺"

class MaleFemale(str, enum.Enum):
    male = '👨‍ Мужской'
    female = '👩‍ Женский'


class User(CreatedModel):
    __tablename__ = 'user'
    name: Mapped[str] = mapped_column(String(55), nullable=True)
    phone_number: Mapped[str] = mapped_column(String(13))
    language: Mapped[LanguageEnum] = mapped_column(
        Enum(LanguageEnum, name="language_enum"),
        default=LanguageEnum.ru,
        nullable=False
    )
    birthdate: Mapped[str] = mapped_column(String(20))
    jins : Mapped[MaleFemale] = mapped_column(
        Enum(MaleFemale, name="male_female_enum"),
        nullable=False
    )
    city: Mapped[str] = mapped_column(String(60))


engine = create_engine("postgresql+psycopg2://postgres:1@localhost:5432/module_5")

metadata = Base.metadata.create_all(engine)
