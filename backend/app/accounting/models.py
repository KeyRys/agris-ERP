from sqlalchemy import Column, String, Boolean, Enum
from app.core.database import Base
import enum
import uuid
from sqlalchemy.dialects.postgresql import UUID

class AccountType(str, enum.Enum):
    asset = "asset"
    liability = "liability"
    equity = "equity"
    revenue = "revenue"
    expense = "expense"

class NormalBalance(str, enum.Enum):
    debit = "debit"
    credit = "credit"

class Account(Base):
    __tablename__ = "accounts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    code = Column(String(4), nullable=False, unique=True)
    name = Column(String(100), nullable=False)

    type = Column(Enum(AccountType), nullable=False)
    normal_balance = Column(Enum(NormalBalance), nullable=False)

    is_active = Column(Boolean, default=True, nullable=False)