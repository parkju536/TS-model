class Config(object):
    def __init__(self):
        self.lr = 1e-3
        self.attention_size = 128
        self.num_filters = 128
        self.kernel_sizes = [3, 4, 5]
        self.clip = 5
        self.nsteps = 8
        self.l2_lambda = 1e-3
        self.ar_lambda = 1e-1