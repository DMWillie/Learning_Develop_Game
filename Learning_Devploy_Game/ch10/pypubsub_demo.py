"""
    作者:北辰
    日期:15/06/2019
    功能:使用PyPubSub包来进行发布
"""

from pubsub import pub

# A Subscriber function
def model_change_handler(data):
    print("In model_change handler function, data=", data)

# Register the subscriber
pub.subscribe(model_change_handler, "WINNER ANNOUNCEMENT")

# 'Publish' a message. the data is any optional argument
pub.sendMessage("WINNER ANNOUNCEMENT", data="Player Won!")