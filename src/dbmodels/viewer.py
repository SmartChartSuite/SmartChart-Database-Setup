from typing import Optional

from sqlalchemy import DateTime, Index, Integer, JSON, PrimaryKeyConstraint, String, Text, UniqueConstraint, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import datetime

'''
Models match Viewer 1.1.1 scripts.
'''

class Base(DeclarativeBase):
    pass


class Annotation(Base):
    __tablename__ = 'annotation'
    __table_args__ = (
        PrimaryKeyConstraint('annotation_id', name='annotation_pk'),
        Index('annotation_annotation_id_uindex', 'annotation_id', unique=True),
        {'schema': 'viewer'}
    )

    annotation_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    content_id: Mapped[int] = mapped_column(Integer)
    case_id: Mapped[int] = mapped_column(Integer)
    created: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    user_id: Mapped[Optional[int]] = mapped_column(Integer)
    text_: Mapped[Optional[str]] = mapped_column('text', Text)


class Category(Base):
    __tablename__ = 'category'
    __table_args__ = (
        PrimaryKeyConstraint('concept_id', name='category_pk'),
        Index('category_concept_code_uindex', 'concept_id', unique=True),
        {'schema': 'viewer'}
    )

    concept_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    section: Mapped[Optional[str]] = mapped_column(String(30))
    category: Mapped[Optional[str]] = mapped_column(String(255))
    question: Mapped[Optional[str]] = mapped_column(String(255))


class Flag(Base):
    __tablename__ = 'flag'
    __table_args__ = (
        PrimaryKeyConstraint('content_id', name='viewer_data_pk'),
        Index('viewer_data_observation_id_uindex', 'content_id', unique=True),
        {'schema': 'viewer'}
    )

    content_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    case_id: Mapped[int] = mapped_column(Integer)
    created: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    flag: Mapped[Optional[str]] = mapped_column(String(20))


class Metadata(Base):
    __tablename__ = 'metadata'
    __table_args__ = (
        PrimaryKeyConstraint('metadata_id', name='metadata_pk'),
        UniqueConstraint('tag', name='metadata_un'),
        {'schema': 'viewer'}
    )

    metadata_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    tag: Mapped[str] = mapped_column(String)
    description: Mapped[Optional[str]] = mapped_column(String)
    viewer_config: Mapped[Optional[dict]] = mapped_column(JSON)


class User(Base):
    __tablename__ = 'user'
    __table_args__ = (
        PrimaryKeyConstraint('user_id', name='user_pk'),
        Index('user_user_id_uindex', 'user_id', unique=True),
        {'schema': 'viewer'}
    )

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True)
