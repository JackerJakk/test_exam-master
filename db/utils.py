from sqlalchemy import delete as sqlalchemy_delete, DateTime
from sqlalchemy import text
from sqlalchemy import update as sqlalchemy_update
from sqlalchemy.future import select
from sqlalchemy.orm import declared_attr, lazyload, Mapped
from sqlalchemy.testing.schema import mapped_column

from db import db, Base

db.init()  # create engine


# ----------------------------- ABSTRACTS ----------------------------------
class AbstractClass:
    @staticmethod
    async def commit():
        try:
            await db.commit()
        except Exception:
            await db.rollback()
            raise

    @classmethod
    async def create(cls, **kwargs):
        object_ = cls(**kwargs)
        db.add(object_)
        await cls.commit()
        return object_

    @classmethod
    async def update(cls, id_, **kwargs):
        query = (sqlalchemy_update(cls)
                 .where(cls.id == id_)
                 .values(**kwargs)
                 .execution_options(synchronize_session="fetch")
                 )

        await db.execute(query)
        await cls.commit()

    @classmethod
    async def get(cls, id_):
        query = select(cls).filter(cls.id == id_)
        objects = await db.execute(query)
        object_ = objects.first()
        if object_:
            return object_[0]
        else:
            return []

    @classmethod
    async def delete(cls, id_):
        query = sqlalchemy_delete(cls).where(cls.id == id_)
        await db.execute(query)
        await cls.commit()
        return True

    @classmethod
    async def get_all(cls, order_fields: list[str] = None, options=None):
        query = select(cls).options(lazyload(options))
        if order_fields:
            query = query.order_by(*order_fields)
        objects = await db.execute(query)
        result = []
        for i in objects.all():
            result.append(i[0])
        return result


tz = "TIMEZONE('Asia/Tashkent', NOW())"


class CreatedModel(Base, AbstractClass):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() + 's'

    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created_at: Mapped[str] = mapped_column(DateTime, server_default=text(tz))
    updated_at: Mapped[str] = mapped_column(DateTime, server_default=text(tz), onupdate=text(tz))