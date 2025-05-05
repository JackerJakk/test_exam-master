from sqlalchemy import select, Text, ForeignKey, DATE
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base, db
from db.utils import CreatedModel


class User(CreatedModel):
    id : Mapped[int] = mapped_column(BIGINT , primary_key=True)
    first_name : Mapped[str]
    last_name : Mapped[str] = mapped_column(nullable=True)
    username : Mapped[str] = mapped_column(nullable=True)



class Category(CreatedModel):
    __tablename__ = "categories"
    name: Mapped[str]
    foods : Mapped[list['Food']] = relationship(back_populates="category",lazy= 'joined')

    @classmethod
    async def get_by_name(cls, name):
        query = select(cls).where(cls.name.contains(name))
        objects = await db.execute(query)
        objects = objects.all()
        return objects


class Food(CreatedModel):
    deadline : Mapped[str] = mapped_column(DATE)
    title : Mapped[str]
    description : Mapped[str]
    category_id : Mapped[int] = mapped_column(ForeignKey('categories.id', ondelete='cascade'))
    category : Mapped['Category'] = relationship(back_populates="foods",lazy= 'joined')


metadata = Base.metadata