from selenium.common.exceptions import NoSuchWindowException, \
    NoSuchFrameException, NoSuchElementException, NoAlertPresentException, \
    InvalidSelectorException, TimeoutException, ElementNotVisibleException, \
    ElementNotSelectableException, StaleElementReferenceException
from functools import wraps
import logging


def exc_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            logging.error(f"Exception was found.")
            res = func(*args, **kwargs)

        except NoSuchWindowException:
            logging.error(f"In function {func.__name__} the current list of "
                          f"windows is not updated. The previous window"
                          f"does not exist.")
            raise

        except NoSuchFrameException:
            logging.error(f"In function {func.__name__} switching between "
                          f"multiple frames is not possible.")
            raise

        except NoSuchElementException:
            logging.error(f"In function {func.__name__} the locators are "
                          f"unable to find or access elements on the"
                          f"web page or application.")
            raise

        except NoAlertPresentException:
            logging.error(
                f"In function {func.__name__} the user is trying to switch "
                f"to an alert which is not present. The browser"
                f"did not yet open an alert.")
            raise

        except InvalidSelectorException:
            logging.error(
                f"In function {func.__name__} the selector is incorrect. "
                f"Possibly the problem in selector syntax.")
            raise

        except TimeoutException:
            logging.error(
                f"In function {func.__name__} the command did not execute "
                f"or complete within wait time. The page components fail"
                f"to load within wait time.")
            raise

        except ElementNotVisibleException:
            logging.error(
                f"In function {func.__name__} the WebDriver tries to find "
                f"an element that is hidden or invisible. To handle this "
                f"exception, it is essential that the exact reason is "
                f"identified, which can be due to nested web elements or "
                f"overlapping web elements.")
            raise

        except ElementNotSelectableException:
            logging.error(
                f"In function {func.__name__} the element is present on the"
                f"web page, but the element cannot be selected. Wait"
                f"command should be implemented.")
            raise

        except StaleElementReferenceException:
            logging.error(
                f"In function {func.__name__} the web element is no longer"
                f"part of the web page. The element may have been part of the"
                f"source code, but it is no longer part of the window."
                f"There can be multiple reasons for this exception."
                f"It can occur either from a switch to a different page,"
                f"the element is no longer part of DOM or due"
                f"to frame/window switch. Use Dynamic Xpath for handling "
                f"DOM operations or use the Page Factory Model access the"
                f"element in loops before throwing the exception.")
            raise

        except Exception:
            logging.error(f"In function {func.__name__} there is an Error. "
                          f"Check code.")
            raise

        else:
            return res

    return wrapper


# Configure root logger
logging.basicConfig(level=logging.error)

# Configure file handler
file_handler = logging.FileHandler('exceptions.log')
file_handler.setLevel(logging.ERROR)

# Create formatter and add it to the handler
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the handler to the root logger
logging.getLogger('').addHandler(file_handler)

# logging.basicConfig(filename='exceptions.log',
#                     level=logging.error,
#                     filemode="w")


if __name__ == '__main__':
    pass
