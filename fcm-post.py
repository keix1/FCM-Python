# coding: utf-8

from pyfcm import FCMNotification
import settings
API_KEY = settings.AP
DEVICE_REGISTRATION_ID = settings.DRI

push_service = FCMNotification(api_key=API_KEY)

registration_id = DEVICE_REGISTRATION_ID
message_title = "News!"
message_body = "OKKKKKKKKKKKKKKKKKK!!!!!!!!"
result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)

print(result)