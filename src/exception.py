import sys
import logging # to check that everything is working fine or not

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error Occurred in Python script name [{0}] line number[{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message

  
    
    
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message) ## We are inheriting exception class here ## in this line innit merthod is overriden
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
        
    def __str__(self):
        return self.error_message ## this will common everywhere when you use try catch block
    
    
# main error i was doing that it was super().__init__ is was using super.__init__
# ,str(error) it is and i was using .str(error)