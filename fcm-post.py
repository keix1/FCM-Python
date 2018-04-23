# coding: utf-8

from pyfcm import FCMNotification
import settings
API_KEY = settings.AP
DEVICE_REGISTRATION_ID = settings.DRI

push_service = FCMNotification(api_key=API_KEY)

registration_id = DEVICE_REGISTRATION_ID
data_message = {
    "title" : "News!!",
    "body" : "great match!",
    "data" : "PortugalVSDenmark",
}

# message_title = "Uber update"
# message_body = "Hi john, your customized news for today is ready"

result = push_service.single_device_data_message(registration_id=registration_id, data_message=data_message)

# result = push_service.notify_single_device(registration_id=registration_id, data_message=data_message, message_body=message_body)
print(result)