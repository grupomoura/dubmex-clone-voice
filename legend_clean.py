import re

def time_to_milliseconds(time):
    hours, minutes, seconds, milliseconds = map(int, re.findall(r'\d+', time))
    total_milliseconds = (hours * 60 * 60 * 1000) + (minutes * 60 * 1000) + (seconds * 1000) + milliseconds
    return total_milliseconds

def parse_subtitle(subtitle):
    lines = subtitle.strip().split('\n')
    subtitle_objects = []

    for i in range(0, len(lines), 4):
        index = lines[i].strip()
        time = lines[i+1].strip()
        text = lines[i+2].strip()

        # Extrai os tempos inicial e final em milissegundos
        start_time, end_time = re.findall(r'\d+:\d+:\d+,\d+', time)
        start_time = time_to_milliseconds(start_time)
        end_time = time_to_milliseconds(end_time)

        # Cria o objeto de legenda
        subtitle_obj = {'time': f'{start_time}-{end_time}', 'text': text}
        subtitle_objects.append(subtitle_obj)

    return subtitle_objects


if __name__ == "__main__":
    # Exemplo de uso
    subtitle = '''
    1
    00:00:00,000 --> 00:00:06,000
    When it comes to protection, the helmet is one of the most important items for you to ride your motorcycle.

    2
    00:00:06,000 --> 00:00:09,000
    It has to be fully adjusted on the head.

    3
    00:00:09,000 --> 00:00:15,000
    You can't feel uncomfortable because nothing can distract you from the road.

    4
    00:00:15,000 --> 00:00:19,000
    You can't keep taking your hand off the handlebars and trying to move it there,

    5
    00:00:19,000 --> 00:00:22,000
    so that you might cause a distraction.

    6
    00:00:22,000 --> 00:00:26,000
    This can lead to a fall and you can suffer a serious accident.

    7
    00:00:26,000 --> 00:00:30,000
    I see many people using the helmet in the wrong way.

    8
    00:00:30,000 --> 00:00:36,000
    They use it as a seat belt, they don't put on the seat belt.

    9
    00:00:36,000 --> 00:00:38,000
    The seat belt is very important.

    10
    00:00:38,000 --> 00:00:41,000
    It's the same thing as riding a car without a seat belt.

    11
    00:00:41,000 --> 00:00:46,000
    The seat belt is what holds the helmet on your head.

    12
    00:00:46,000 --> 00:00:52,000
    In a collision, a possible collision, if you don't have the seat belt,

    13
    00:00:52,000 --> 00:00:55,000
    the helmet is thrown away and you can suffer an accident.

    14
    00:00:55,000 --> 00:00:59,000
    So take good care of your CPU, which is your head.

    '''
    subtitles = parse_subtitle(subtitle)

    # for subtitle_obj in subtitles:
    #     print(subtitle_obj)
