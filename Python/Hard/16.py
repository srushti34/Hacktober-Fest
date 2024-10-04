def build_sentence(subject, **words):
 sentence = subject + ' ' + words['verb'] + ' ' + words['object']
 return sentence
print(build_sentence("The cat", verb="eats", adjective="big",
object="fish"))
