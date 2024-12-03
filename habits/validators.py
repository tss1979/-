from rest_framework.serializers import ValidationError


class TimeToActionValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, data):
        if data.get("time_to_action_in_sec ") and data.get("time_to_action_in_sec ") > 120:
            raise ValidationError("Время выполнения должно быть не больше 120 секунд")
