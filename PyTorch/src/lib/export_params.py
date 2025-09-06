from torch import nn

models_folder = "../models/"


def export_params(model: nn.Module, model_name: str):
    """Exports the parameters (weights and biases) of a PyTorch model to a text file."""
    with open(f"{models_folder}{model_name}_params.txt", "w") as file:
        state_dict = model.state_dict()
        for name, param in state_dict.items():
            weights = param.numpy()
            dims = weights.shape

            # Convert numpy array to a formatted string in C++ style without internal braces
            if weights.ndim == 1:  # 1D vector
                formatted_weights = "{" + ", ".join(f"{v:.6f}" for v in weights) + "};"
            elif weights.ndim == 2:  # 2D matrix
                # Flatten the matrix to a single dimension
                flattened_weights = weights.flatten()
                formatted_weights = (
                    "{" + ", ".join(f"{v:.6f}" for v in flattened_weights) + "};"
                )
            else:
                raise ValueError("This script only handles 1D or 2D tensors.")

            # Print tensor information
            file.write(f"Nome: {name}\n")
            file.write(f"Dimensões: {dims}\n")
            file.write(f"Valores:\n{formatted_weights}\n\n")
