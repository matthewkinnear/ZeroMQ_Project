import json


def mogrify(topic, message):
    """ json encode the message and prepend the topic """
    return topic + ' ' + json.dumps(message)


def demogrify(message):
    """ Inverse of mogrify() """
    json0 = message.find('{')
    topic = message[0:json0].strip()
    msg = json.loads(message[json0:])
    return topic, msg
