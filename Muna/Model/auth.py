# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship
# import uuid

# Base = declarative_base()

# class Types(Base):
#     __tablename__ = 'types'

#     type_id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(255), nullable=False)
#     created_at = Column(Integer, nullable=False)
#     updated_at = Column(Integer, nullable=False)

#     connects = relationship("Connect", back_populates="type")

# class Connect(Base):
#     __tablename__ = 'connect'

#     connect_id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(255), nullable=False)
#     type_id = Column(Integer, ForeignKey('types.type_id'), nullable=False)
#     created_at = Column(Integer, nullable=False)
#     updated_at = Column(Integer, nullable=False)

#     type = relationship("Types", back_populates="connects")


# class Auth(Base):
#     __tablename__ = 'auth'

#     auth_id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
#     user_name = Column(String(255), nullable=False)
#     password = Column(String(255), nullable=False)
#     created_at = Column(Integer, nullable=False)
#     updated_at = Column(Integer, nullable=False)

#     user = relationship("User", back_populates="auth")
#     forgets = relationship("Forgets", back_populates="auth")


# class Forgets(Base):
#     __tablename__ = 'forgets'

#     forget_id = Column(Integer, primary_key=True, autoincrement=True)
#     freq_forget = Column(String(255), nullable=False)
#     auth_id = Column(Integer, ForeignKey('auth.auth_id'), nullable=False)
#     created_at = Column(Integer, nullable=False)
#     updated_at = Column(Integer, nullable=False)

#     auth = relationship("Auth", back_populates="forgets")


# class UserLevels(Base):
#     __tablename__ = 'user_levels'

#     usle_id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(100), nullable=False)


# class User(Base):
#     __tablename__ = 'users'

#     user_id = Column(Integer, primary_key=True, autoincrement=True)
#     user_uuid = Column(String, nullable=False, default=str(uuid.uuid4()))
#     full_name = Column(String(255), nullable=False)
#     nick_name = Column(String(50), nullable=False)
#     created_at = Column(Integer, nullable=False)
#     updated_at = Column(Integer, nullable=False)
    
#     auth = relationship("Auth", back_populates="user")
