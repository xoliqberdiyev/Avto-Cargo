import redis

r = redis.StrictRedis.from_url('redis://redis:6379')

def cache_user_credentials(email, password, passport_id, pnfl, time):
    key = f"user_credentials:{email}"

    r.hset(key, mapping={
        "email": email,
        "password": password,
        "passport_id": passport_id,
        "pnfl": pnfl,
    })

    r.expire(key, time)


def get_user_credentials(email):
    key = f"user_credentials:{email}"
    data = r.hgetall(key)
    if not data:
        return None
    
    return {
        "email": data.get(b'email').decode() if data.get(b'email') else None,
        "password": data.get(b'password').decode() if data.get(b'password') else None,
        "passport_id": data.get(b'passport_id').decode() if data.get(b'passport_id') else None,
        "pnfl": data.get(b'pnfl').decode() if data.get(b'pnfl') else None,
    }


def cache_user_confirmation_code(code, email, time):
    key = f"user_confirmation:{email}_{code}"

    r.hset(key, mapping={
        'email': email,
        'code': code
    })

    r.expire(key, time)


def get_user_confirmation_code(email, code):
    key = f'user_confirmation:{email}_{code}'

    data = r.hgetall(key)
    if not data:
        return None
    
    return {
        "email": data.get(b'email').decode() if data.get(b'email') else None,
        "code": data.get(b'code').decode() if data.get(b'code') else None
    }
