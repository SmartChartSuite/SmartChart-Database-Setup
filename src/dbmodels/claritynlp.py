from typing import Optional

from sqlalchemy import BigInteger, Column, DateTime, Index, PrimaryKeyConstraint, String, Table, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import datetime

from utils.database import create_connection
from sqlalchemy.schema import CreateSchema

    
class Base(DeclarativeBase):
    pass


class NlpJob(Base):
    __tablename__ = 'nlp_job'
    __table_args__ = (
        PrimaryKeyConstraint('nlp_job_id', name='nlp_job_pkey'),
        Index('nlp_job_nlp_job_id_uindex', 'nlp_job_id', unique=True),
        {'schema': 'nlp'}
    )

    nlp_job_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    job_type: Mapped[Optional[str]] = mapped_column(String(100))
    name: Mapped[Optional[str]] = mapped_column(String(512))
    description: Mapped[Optional[str]] = mapped_column(Text)
    owner: Mapped[Optional[str]] = mapped_column(String(100))
    pipeline_id: Mapped[Optional[int]] = mapped_column(BigInteger)
    phenotype_id: Mapped[Optional[int]] = mapped_column(BigInteger)
    status: Mapped[Optional[str]] = mapped_column(String(256))
    date_started: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    date_ended: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


class NlpJobStatus(Base):
    __tablename__ = 'nlp_job_status'
    __table_args__ = (
        PrimaryKeyConstraint('nlp_job_status_id', name='nlp_job_status_pkey'),
        Index('nlp_job_status_nlp_job_status_id_uindex', 'nlp_job_status_id', unique=True),
        {'schema': 'nlp'}
    )

    nlp_job_status_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    status: Mapped[str] = mapped_column(String(256))
    date_updated: Mapped[datetime.datetime] = mapped_column(DateTime)
    description: Mapped[Optional[str]] = mapped_column(Text)
    nlp_job_id: Mapped[Optional[int]] = mapped_column(BigInteger)


class NlpqlLibrary(Base):
    __tablename__ = 'nlpql_library'
    __table_args__ = (
        PrimaryKeyConstraint('nlpql_id', name='nlpql_library_pkey'),
        Index('nlpql_library_nlpql_id_uindex', 'nlpql_id', unique=True),
        Index('nlpql_library_nlpql_name_nlpql_version_uindex', 'nlpql_name', 'nlpql_version', unique=True),
        {'schema': 'nlp'}
    )

    nlpql_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    nlpql_name: Mapped[str] = mapped_column(String(100))
    nlpql_version: Mapped[str] = mapped_column(String(25))
    nlpql_raw: Mapped[Optional[str]] = mapped_column(Text)
    nlpql_json: Mapped[Optional[str]] = mapped_column(Text)
    date_added: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


class Phenotype(Base):
    __tablename__ = 'phenotype'
    __table_args__ = (
        PrimaryKeyConstraint('phenotype_id', name='phenotype_pkey'),
        Index('phenotype_name_index', 'name'),
        Index('phenotype_phenotype_id_uindex', 'phenotype_id', unique=True),
        {'schema': 'nlp'}
    )

    phenotype_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    config: Mapped[str] = mapped_column(Text)
    date_created: Mapped[datetime.datetime] = mapped_column(DateTime)
    owner: Mapped[Optional[str]] = mapped_column(String(30))
    name: Mapped[Optional[str]] = mapped_column(String(250))
    description: Mapped[Optional[str]] = mapped_column(Text)
    nlpql: Mapped[Optional[str]] = mapped_column(Text)
    date_updated: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


t_phenotype_mapping = Table(
    'phenotype_mapping', Base.metadata,
    Column('phenotype_id', BigInteger, nullable=False),
    Column('pipeline_id', BigInteger, nullable=False),
    Index('phenotype_mapping_phenotype_id_index', 'phenotype_id'),
    schema='nlp'
)


class PipelineConfig(Base):
    __tablename__ = 'pipeline_config'
    __table_args__ = (
        PrimaryKeyConstraint('pipeline_id', name='pipeline_config_pkey'),
        Index('nlp_pipeline_config_pipeline_id_uindex', 'pipeline_id', unique=True),
        {'schema': 'nlp'}
    )

    pipeline_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    owner: Mapped[Optional[str]] = mapped_column(String(100))
    config: Mapped[Optional[str]] = mapped_column(Text)
    pipeline_type: Mapped[Optional[str]] = mapped_column(String(100))
    name: Mapped[Optional[str]] = mapped_column(String(256))
    description: Mapped[Optional[str]] = mapped_column(Text)
    date_created: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    date_updated: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
