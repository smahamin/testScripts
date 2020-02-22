
original_string = open('original.txt').read()

maketrans = original_string.maketrans
new_string= original_string.translate(maketrans(',?','?,'))
open('translated.txt', 'w').write(new_string)