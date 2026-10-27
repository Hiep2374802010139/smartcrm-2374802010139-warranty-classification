import logging, uuid
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

log = logging.getLogger('serve.errors')

class LoiNghiepVu(Exception):
    def __init__(self, ma: str, thong_diep: str, http_status: int = 409):
        super().__init__(thong_diep)
        self.ma, self.thong_diep, self.http_status = ma, thong_diep, http_status

def dang_ky_xu_ly_loi(app: FastAPI):
    @app.exception_handler(LoiNghiepVu)
    async def _nghiep_vu(req: Request, e: LoiNghiepVu):
        log.info('vi pham quy tac %s', e.ma)
        return JSONResponse(status_code=e.http_status, content={'error': e.ma, 'message': e.thong_diep})

    @app.exception_handler(Exception)
    async def he_thong(req: Request, e: Exception):
        ma_tra_cuu = req.headers.get('x-request-id') or uuid.uuid4().hex[:8]
        log.exception('loi he thong', extra={'request_id': ma_tra_cuu})
        return JSONResponse(status_code=500, content={
            'error': 'LOI_HE_THONG',
            'message': f'He thong dang gap su co. Ma tra cuu: {ma_tra_cuu}'
        })