# middleware.py
import time
import logging
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

# uvicorn.access 가 아닌 app 전용 로거 생성
logger = logging.getLogger("app.middleware")
logger.setLevel(logging.INFO)
# (필요하면 핸들러·포매터 직접 설정)

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # 요청 시작 로그
        logger.info(f"➡️ [Start] {request.method} {request.url.path}")
        
        start = time.time()
        response = await call_next(request)
        elapsed = time.time() - start
        
        # 요청 완료 로그
        logger.info(
            f"✅ [End]   {request.method} {request.url.path} "
            f"status={response.status_code} time={elapsed:.3f}s"
        )
        return response
