# import json
# from sqlalchemy import create_engine, and_
# from sqlalchemy.orm import sessionmaker
# from django.conf import settings
# from Muna.Model.auth import User, Auth
# from datetime import datetime
# from django.http import JsonResponse

# engine = create_engine(settings.DATABASE_URL['AUTH'])
# Session = sessionmaker(bind=engine)


# def register(data):
#     session = Session()
#     user = User(
#         full_name=data.get('full_name'),
#         nick_name=data.get('nick_name'),
#         created_at=int(datetime.now().timestamp()),
#         updated_at=int(datetime.now().timestamp())
#     )
#     auth = Auth(
#         user_name=data.get('user_name'),
#         password=data.get('password'),
#         created_at=int(datetime.now().timestamp()),
#         updated_at=int(datetime.now().timestamp())
#     )
#     try:
#         session.add(user)
#         session.commit()
#         auth.user_id = user.user_id
#         session.add(auth)
#         session.commit()
#         response = {"message": "success"}
#     except Exception as e:
#         session.rollback()
#         response = {"message": "error", "details": str(e)}
#     finally:
#         session.close()
#     return JsonResponse(response)

# def login(data):
#     session = Session()
#     try:
#         user_auth = session.query(User, Auth).join(Auth).filter(and_(Auth.user_name == data.get('user_name'), Auth.password == data.get('password'))).first()
#         if user_auth:
#             response = {
#                 "message": "berhasil login",
#                 "data": {
#                     'user_id': user_auth.User.user_id,
#                     'full_name': user_auth.User.full_name,
#                     'nick_name': user_auth.User.nick_name,
#                     'user_name': user_auth.Auth.user_name,
#                     'password': user_auth.Auth.password
#                 }
#             }
#         else:
#             response = {
#                 "message": "gagal login",
#             }
#     except Exception as e:
#         response = {"message": "error", "details": str(e)}
#     finally:
#         session.close()
#     return JsonResponse(response)
    