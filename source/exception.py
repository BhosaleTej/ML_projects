import sys 
# sys - It rpovides various functions and variables that are used to 
#       manipulate different parts of the python runtime environment.

from source.logger import loggging

def error_message_detail(error, error_detail: sys):
    _,_,exc_tb = error_detail.exc_info() 
# _,_,exc_tb = type, value, traceback. type and value are ignored(hence _) 
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))
    
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message


# customexception - captures detailed error information, including the filename
#                   and line number where error occured.

# error_message_detail - function is used to construct a detailed error message.

# custom exception can be used to raise exceptions with more context about where
#   and why they occured.