


''' Structure

     word -  translation    ([transcription])
      ^          ^                 ^
      |          |                 |
    'key'  ['translation', '[transcription]' ]
'''

class Storage:
    def __init__(self, data=None):
        if not data or type(data) is not dict:
            self.data = dict()
        else:
            self.data = data

    def add_word(self, new_word: str):
        if new_word is not None:
            new_word_pair = new_word.split('-')

            '''check right construction'''
            if len(new_word_pair) == 2:

                word = new_word_pair[0]

                ''' checking for repetitions of keys'''
                if word not in self.data:
                    self.data[word] = []

                if



        return "Bad line, use construction:\n" \
               "word - translation ([transcription])"

