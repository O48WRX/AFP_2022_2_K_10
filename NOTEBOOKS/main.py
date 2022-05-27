import Network
import mnist_loader
import time

# Kezelt MNIST adatméret ÉS  OUTPUT LAYER
# NE ÉRJ HOZZÁ

__MNISTMAXSIZE = 784
__OUTPUTLAYER = 10

# Futási paraméterek

_hidden_layer1 = 10
_hidden_layer2 = 10

_epoch = 10
_mini_batch_size = 10
_eta = 4.0

# Felhasználói input

inputIsDigitAndNotNull = False
_nr_of_hidden_layers = 1
__neural_network_size = []
tempNumber = None

if __name__ == '__main__':
    training_data, validation_data, test_data = mnist_loader.load_data_together(__MNISTMAXSIZE)

    while not inputIsDigitAndNotNull:
        tempNumber = input("Mennyi rejtett réteget szeretnél? ")
        if (tempNumber.isnumeric() and tempNumber != None and tempNumber != 0):
            inputIsDigitAndNotNull = True
    _nr_of_hidden_layers = int(tempNumber)


    __neural_network_size.append(__MNISTMAXSIZE)
    for i in range(_nr_of_hidden_layers):
        inputIsDigitAndNotNull = False
        while not inputIsDigitAndNotNull:
            tempNumber = input(f"Mérete a {i + 1}. rejtett rétegnek: ")
            if  tempNumber.isnumeric() and tempNumber != None and tempNumber != 0:
                inputIsDigitAndNotNull = True
        __neural_network_size.append(int(tempNumber))

    __neural_network_size.append(__OUTPUTLAYER)

    [print(f"A neurális háló {i}. rétegének nagysága: {__neural_network_size[i]}")
     for i in range(len(__neural_network_size))]

    # [__MNISTMAXSIZE, _hidden_layer1, _hidden_layer2, __OUTPUTLAYER]
    net = Network.Network(__neural_network_size)

    _Start_Time = time.time()
    net.stochastic_gradient_descent(training_data, _epoch, _mini_batch_size, _eta, test_data=test_data)
    _End_Time = time.time()
    print("\n\nFutási idő: ", round(_End_Time - _Start_Time),"másodperc")



