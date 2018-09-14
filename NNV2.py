from textgenrnn import textgenrnn
textgen = textgenrnn('./server_weights.hdf5')

def deep_train(epoch, mode):
    textgen.train_from_file('log.txt', num_epochs=epoch)
    if mode == 1:
        textgen.generate_to_file('halout.txt')

def train(epoch,mode):
    try:
        textgen.train_from_file('temp_log.txt', num_epochs=epoch)
    except AssertionError:
        return False
    if mode == 1:
        textgen.generate_to_file('halout.txt')
    return True

def generate(prefix):
    phrase = textgen.generate(1,temperature = 1.0,return_as_list=True, prefix = prefix)
    return phrase

if __name__ == "__main__":
    train(50,0)
    generate("I must interject by saying ")
