def user_serializer(user)->dict:
    return{
        "id":str(user["_id"]),
        "first_name":user["first_name"],
        "last_name":user["last_name"],
        "email":user["email"],
        "telephone":user["telephone"],
        "city":user["city"],
        "created_at":user["created_at"],
        "updatated_at":user["updated_at"],
    }

def user_list_serializer(users)->list:
    return[
        user_serializer(user) for user in users
    ]