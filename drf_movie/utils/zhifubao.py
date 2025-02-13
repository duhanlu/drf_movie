import logging
import traceback

from alipay.aop.api.AlipayClientConfig import AlipayClientConfig
from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient
from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.domain.AlipayTradeAppPayModel import AlipayTradeAppPayModel
from alipay.aop.api.domain.AlipayTradePagePayModel import AlipayTradePagePayModel
from alipay.aop.api.domain.AlipayTradePayModel import AlipayTradePayModel
from alipay.aop.api.domain.GoodsDetail import GoodsDetail
from alipay.aop.api.domain.SettleDetailInfo import SettleDetailInfo
from alipay.aop.api.domain.SettleInfo import SettleInfo
from alipay.aop.api.domain.SubMerchant import SubMerchant
from alipay.aop.api.request.AlipayOfflineMaterialImageUploadRequest import AlipayOfflineMaterialImageUploadRequest
from alipay.aop.api.request.AlipayTradeAppPayRequest import AlipayTradeAppPayRequest
from alipay.aop.api.request.AlipayTradePagePayRequest import AlipayTradePagePayRequest
from alipay.aop.api.request.AlipayTradePayRequest import AlipayTradePayRequest
from alipay.aop.api.response.AlipayOfflineMaterialImageUploadResponse import AlipayOfflineMaterialImageUploadResponse
from alipay.aop.api.response.AlipayTradePayResponse import AlipayTradePayResponse
from alipay.aop.api.util.SignatureUtils import verify_with_rsa

from django.conf import settings 

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    filemode='a',)
logger = logging.getLogger('')

class Alipay():
    
    # 实例化客户端
    alipay_client_config = AlipayClientConfig()
    alipay_client_config.server_url = settings.ALIPAY_SERVER_URL
    alipay_client_config.app_id = settings.ALIPAY_APP_ID
    alipay_client_config.app_private_key = settings.ALIPAY_APP_PRIVATE_KEY
    alipay_client_config.alipay_public_key = settings.ALIPAY_PUBLIC_KEY
    
    def __init__(self):
        
        self.client = DefaultAlipayClient(alipay_client_config=self.alipay_client_config, logger=logger)
    
    def trade_page(self, out_trade_no, total_amount, subject, body, product_code):
        # 构造请求参数对象
        model = AlipayTradePagePayModel()
        model.out_trade_no = out_trade_no
        model.total_amount = total_amount
        model.subject = subject
        model.body = body
        model.product_code = product_code
        

        request = AlipayTradePagePayRequest(biz_model=model)
        # 得到构造的请求，如果http_method是GET，则是一个带完成请求参数的url，如果http_method是POST，则是一段HTML表单片段
        response = self.client.page_execute(request, http_method="GET")

        return response
    
    def verify_sign(self, unsigned_string, sign):
        
       return  verify_with_rsa(settings.ALIPAY_PUBLIC_KEY, bytes(unsigned_string, encoding='utf-8'), sign)
