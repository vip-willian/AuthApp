from typing import cast


def extract_remote_ip(request) -> str:
    if request.headers.get("CF-Connecting-IP"):
        return cast(str, request.headers.get("CF-Connecting-IP"))
    elif request.headers.get("X-Forwarded-For"):
        return cast(str, request.headers.get("X-Forwarded-For"))
    else:
        return cast(str, request.remote_addr)
