
import logging


def handler(data, context):
    """Handle an incoming HTTP request, it could be from reanbot-router or from any bot. """
    # readEvent
    logger.info("incoming data : " + str(data))
    # print("incoming data : " + str(data))

    if "challenge" in data:
        return data["challenge"]



    return "500 OK"
