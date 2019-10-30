"""
PyXLL Examples: Async function

Starting with Excel 2010 worksheet functions can
be registered as asynchronous.

This can be used for querying results from a server
asynchronously to improve the worksheet calculation
performance.
"""

from pyxll import xl_func, xl_version
import logging

_log = logging.getLogger(__name__)

try:
    import json
except ImportError:
    _log.warning("json could not be imported. Async example will not work", exc_info=True)
    json = None

try:
    import aiohttp
except ImportError:
    _log.warning("aiohttp could not be imported. Async example will not work", exc_info=True)
    aiohttp = None

#
# Async functions are only supported from Excel 2010
#
if xl_version() >= 14 and json is not None and aiohttp is not None:

    @xl_func
    async def pyxll_stock_price(endpoint, api_token, symbol):
        """Return the latest price for a symbol from iextrading.com"""
        url = "{endpoint}/stock/{symbol}/quote?token={api_token}".format(endpoint=endpoint,
                                                                         symbol=symbol,
                                                                         api_token=api_token)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                assert response.status == 200
                data = await response.read()

        data = json.loads(data.decode("utf-8"))
        return data.get("latestPrice", "#NoLatestPrice")

else:

    @xl_func
    def pyxll_stock_price(endpoint, api_token, symbol):
        """not supported in this version of Excel"""
        if aiohttp is None:
            return "aiohttp module could not be imported"
        if json is None:
            return "json module could not be imported"
        return "async functions are not supported in Excel %s" % xl_version()