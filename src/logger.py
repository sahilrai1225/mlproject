import logging
## logger is for the purpose that any execution happen we shoukd be able to log all info,exection
## in some file so that we will be able to track if there are  any errors even the custom exception error we will try to log that into text file For that we need to implement logger

import os
from datetime import datetime

# how out log file should be created we are looking at that
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# so our file name will be created of whatever datetime in coming # it will be text file # in this naming convention it will be created
# this will be used every where format
## down here log file will definaely be used
# our file name should have logs in forward and this is naming conventions
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
# cwd=current working dir

## in the folder only log file will be created and everfile will start with log and this naming convention

os.makedirs(logs_path,exist_ok=True)
## this says even though their is a file keep appending file


LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

## whenever we want to create a log we really need to set it in basic config

# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format="[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s", # this is format used everywhere, timestmp line no ,name,level name, message this is how our entire meassage will be print
#     level=logging.INFO,
    
    
# )
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)

# That basically means now wherever I use logging.info import logging and logging.info.
# And uh probably I write out any print message.
# Then it is going to use this kind of basic config and it is going to create this file path.
# It is basically going to keep this particular format with respect to the message and all that we are
# going to get.
# Okay, uh, I'll show this. 
## wrt to logging we need to set up basic config

## These were generic thing we need to do- exception handling and logger
## util.py when we need the we will do 


# custom exception handling the new error message, whatever you want based on your requirement, you
# can basically get it.
# Now, what I will do is that whenever we get an exception, I will take that exception.
# Logging it with a logger file and use logging logging.info to put it inside the file.
# Right.
# So such way we will be able to get that particular folder also perfect.
# So this is perfect.
# Till now uh, we are able to get all these things.
# It's uh I think it will be working fine.
# Absolutely.


if __name__=="__main__":
    logging.info("Logging Has Started")
    
    
# this is for testing
# first it will not run beacuse logger.py is in src and we are runninng outside

## new log folder has been created in ml project big folder