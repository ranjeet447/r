import logging
import time
import requests

LOGGER = logging.getLogger('__name__')


def request_retry_sync(retries=3, cooloff=1):
    retry_on_exceptions = {
        requests.exceptions.ConnectionError,
        requests.exceptions.Timeout,
        requests.exceptions.HTTPError,
    }


def wrap(func):
    @wraps(func)
    def innner(*args, **kwargs):
        for retry_count in range(retries+1):
            response = func(*args, **kwargs)
            try:
                response.raise_for_status()
            except Exception as err:
                if not any([err == exc for exc in retry_on_exceptions]):
                    raise
                if retry_count == retries:
                    raise
                time.sleep(cooloff)
                cooloff *= 2
                LOGGER.warning('{} during {} execution {} of "{}} retries attempted'.format(
                    err.__class__.__name__,
                    func.__name__,
                    retry_count + 1,
                )
                )
        else:
            return response
        return innner
    return wrap
