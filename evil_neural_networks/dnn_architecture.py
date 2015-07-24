import lasagne

def build_model(input_dim, output_dim, batch_size):
    """Create a symbolic representation of a neural network for facial expression classification.

    @param input_dim: 3-tuple describing image size (channels, height, width), use (1, 48, 48)
    @param output_dim: number of classes
    @param batch_size: use 256 for training on GPU, 1 for evaluation on CPU

    @return tuple of (output_layer, input_layer), where each layer is a lasagne layer.
    """
    cur_layer = l_in = lasagne.layers.InputLayer(
        shape=(batch_size,)+ input_dim,
    )
    
    cur_layer = lasagne.layers.Conv2DLayer(
        cur_layer,
        num_filters=48,
        filter_size=(3, 3),
        nonlinearity=lasagne.nonlinearities.rectify,
        W=lasagne.init.HeUniform(gain='relu'),
        )
    cur_layer = lasagne.layers.Conv2DLayer(
        cur_layer,
        num_filters=48,
        filter_size=(3, 3),
        nonlinearity=lasagne.nonlinearities.rectify,
        W=lasagne.init.HeUniform(gain='relu'),
        )
    cur_layer = lasagne.layers.MaxPool2DLayer(cur_layer, pool_size=(2, 2))
    
    
    cur_layer = lasagne.layers.Conv2DLayer(
        cur_layer,
        num_filters=96,
        filter_size=(3, 3),
        nonlinearity=lasagne.nonlinearities.rectify,
        W=lasagne.init.HeUniform(gain='relu'),
        )
    cur_layer = lasagne.layers.Conv2DLayer(
        cur_layer,
        num_filters=96,
        filter_size=(3, 3),
        nonlinearity=lasagne.nonlinearities.rectify,
        W=lasagne.init.HeUniform(gain='relu'),
        )
    cur_layer = lasagne.layers.Conv2DLayer(
        cur_layer,
        num_filters=96,
        filter_size=(3, 3),
        nonlinearity=lasagne.nonlinearities.rectify,
        W=lasagne.init.HeUniform(gain='relu'),
        )
    cur_layer = lasagne.layers.MaxPool2DLayer(cur_layer, pool_size=(2, 2))
    
    
    cur_layer = lasagne.layers.Conv2DLayer(
        cur_layer,
        num_filters=192,
        filter_size=(3, 3),
        nonlinearity=lasagne.nonlinearities.rectify,
        W=lasagne.init.HeUniform(gain='relu'),
        )
    cur_layer = lasagne.layers.Conv2DLayer(
        cur_layer,
        num_filters=192,
        filter_size=(3, 3),
        nonlinearity=lasagne.nonlinearities.rectify,
        W=lasagne.init.HeUniform(gain='relu'),
        )
    cur_layer = lasagne.layers.MaxPool2DLayer(cur_layer, pool_size=(2, 2))
    
    
    cur_layer = lasagne.layers.DropoutLayer(
        cur_layer,
        p=0.4,
    )
    
    cur_layer = lasagne.layers.DenseLayer(
        cur_layer,
        num_units=256,
        nonlinearity=lasagne.nonlinearities.rectify,
        W=lasagne.init.HeUniform(gain='relu'),
    )

    cur_layer = lasagne.layers.DropoutLayer(
        cur_layer,
        p=0.4,
    )
    
    l_out = lasagne.layers.DenseLayer(
        cur_layer,
        num_units=output_dim,
        nonlinearity=lasagne.nonlinearities.softmax,
    )
    return l_out, l_in