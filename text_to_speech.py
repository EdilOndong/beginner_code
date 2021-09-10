# Simple calculator using text to speech module
import pyttsx3


def text_to_speech(voice):
    speaker = pyttsx3.init()
    speaker.say(voice)
    speaker.runAndWait()


def add_number(number_1, number_2):
    result = number_1 + number_2
    return result


def sub_number(number_1, number_2):
    result = number_1 - number_2
    return result


def mul_number(number_1, number_2):
    result = number_1 * number_2
    return result


def div_number(number_1, number_2):
    result = number_1 / number_2
    return result

# You change the operation


add_all_operations_together = add_number(2, 3) + sub_number(2, 3) + mul_number(2, 3) + div_number(2, 3)
text_to_speech(add_all_operations_together)
print(add_all_operations_together)

sub_all_operations_together = add_number(2, 3) - sub_number(2, 3) - mul_number(2, 3) - div_number(2, 3)
text_to_speech(sub_all_operations_together)
print(sub_all_operations_together)

mul_all_operations_together = add_number(2, 3) * sub_number(2, 3) * mul_number(2, 3) * div_number(2, 3)
text_to_speech(mul_all_operations_together)
print(mul_all_operations_together)

div_all_operations_together = add_number(2, 3) / sub_number(2, 3) / mul_number(2, 3) / div_number(2, 3)
text_to_speech(div_all_operations_together)
print(div_all_operations_together)