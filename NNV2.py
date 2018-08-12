from textgenrnn import textgenrnn
textgen = textgenrnn('textgenrnn_weights.hdf5')
def train(epoch, mode):
    textgen.train_from_file('log.txt', num_epochs=epoch)
    if mode == 1:
        textgen.generate_to_file('halout.txt')

def generate(prefix):
    phrase = textgen.generate(1,temperature = 1.0,return_as_list=True, prefix = prefix)
    #print (phrase)
    return phrase

if __name__ == "__main__":
    #train(50)
    generate("I must interject by saying ")
