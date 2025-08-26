import redis

r = redis.StrictRedis.from_url('redis://redis:6379')

def cache_user_credentials(email, password, passport_id, pnlf, time):
    key = f"user_credentials:{email}"

    r.hmset(key, {
        "email": email,
        "password": password,
        "passport_id": passport_id,
        "pnlf": pnlf,
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
        "pnlf": data.get(b'pnlf').decode() if data.get(b'pnlf') else None,
    }
    
