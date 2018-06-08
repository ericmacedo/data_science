import numpy as np


class MLP:

    def __init__(self,
                dataset,
                n_input: int = 2,
                n_hidden: int = 2,
                n_output: int = 1,
                eta: float = 0.1,
                threshold = 1e-6):
        self.dataset = dataset
        self.threshold = threshold
        self.eta = eta

        self.n_input = n_input
        self.n_hidden = n_hidden
        self.n_output = n_output

        self.w_h = np.random.uniform(
            -0.5,
            0.5,
            (n_hidden, n_input + 1)
        )

        self.w_o = np.random.uniform(
            -0.5,
            0.5,
            (n_output, n_hidden + 1)
        )

    def f_(self, net):
        return 1/(1 + np.exp(-net))

    def df_net(self, f_net):
        return f_net * (1 - f_net)

    def matrix_prod(self, x, y):
        result = np.zeros(len(x))
        for row in y:
            for col in range(len(x)):
                result[col] += row[col] * x[col]
        return result

    def forward(self, Xp: list) -> dict:

        # HIDDEN LAYER
        net_h_p = self.matrix_prod(np.append(Xp, 1), self.w_h)
        f_net_h_p = self.f_(net_h_p)

        # OUTPUT LAYER
        net_o_p = self.w_o * f_net_h_p
        f_net_o_p = self.f_(net_o_p)

        return dict({
            "h": [net_h_p, f_net_h_p],
            "o": [net_o_p, f_net_o_p]
        })

    def backpropagation(self):

        E2 = self.threshold + 1

        for index, p in enumerate(self.dataset):
            Xp = p[:self.n_input]
            Yp = p[self.n_input:]

            result = self.forward(Xp)
            Y = result["o"][1]

            error = Yp - Y

            E2 += np.sum(error**2)  # absolute value

            # OUTPUT LAYER TRAINING
            delta_o_p = error * self.df_net(result["o"][1])

            # HIDDEN LAYER TRAINING
            w_o_ij = self.w_o[..., :self.n_hidden]  # exclui os theta
            delta_h_p = self.df_net(result["h"][1]) * (delta_o_pff * w_o_ij)

input_file = open("./xor.txt")

data = np.loadtxt(input_file)

mlp = MLP(data, 2, 2, 2)

mlp.forward([1,1])
mlp.backpropagation()

import pdb; pdb.set_trace()
