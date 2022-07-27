import torch

if __name__ == '__main__':
    print(
        'CUDA Available: {}'.format(
            torch.cuda.is_available()
        )
    )
    x = torch.rand(5, 3)
    print(x)

