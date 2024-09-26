from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey, CheckConstraint, select, func, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, column_property
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    description = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    transactions = relationship("Transaction", back_populates="user", cascade="all, delete-orphan")
    def __repr__(self):
        return f"<User (id={self.id}, username='{self.username}')>"
    
    def __str__(self):
        return self.username
    
class Transaction(Base):
    __tablename__ = 'transactions'
    __table_args__ = (
    CheckConstraint('amount > 0', name='check_positive_amount'),
    CheckConstraint("transaction_type IN ('income', 'expense')", name='check_transaction_type'),
    Index('ix_transactions_user_id', 'user_id'),
    Index('ix_transactions_category_id', 'category_id')
    )
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    date = Column(DateTime, nullable=False, default= datetime.utcnow)
    description = Column(String(255))
    category_id = Column(Integer, ForeignKey('categories.id'))
    transaction_type = Column(String(10), nullable=False, default='expense') # 'income' or 'expense'
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    user = relationship("User", back_populates="transactions")
    category = relationship("Category", back_populates="transactions")

    def __repr__(self):
        return f"<Transaction(id={self.id}, amount={self.amount}, date={self.date})>"

    def __str__(self):
        return f"Transaction: {self.amount} on {self.date.strftime('%Y-%m-%d')}"

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('categories.id'))
    parent = relationship("Category", remote_side=[id], backref="subcategories")
    name = Column(String(50), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    description = Column(String(255))
    color = Column(String(7))  # Hex color code
    
    transactions = relationship("Transaction", back_populates="category", cascade="all, delete-orphan")

    total_amount = column_property(
        select(func.sum(Transaction.amount))
        .where(Transaction.category_id == id)
        .correlate_except(Transaction)
        .scalar_subquery()
    )

    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}')>"

    def __str__(self):
        return self.name