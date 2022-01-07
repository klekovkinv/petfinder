import os


class AttributeInspect:

    @classmethod
    def get_class_attributes(cls):
        attributes = {}
        for attr in cls.__dict__.keys():
            if attr[:2] != '__':
                value = getattr(cls, attr)
                if not callable(value):
                    attributes[attr] = value

        return attributes


class Paths(AttributeInspect):
    inp = '../input'
    outp = '../output'
    data = os.path.join(inp, 'petfinder-pawpularity-score')
    train_csv = os.path.join(data, 'train.csv')
    test_csv = os.path.join(data, 'test.csv')
    sample_submission = os.path.join(data, 'sample_submission.csv')
    weights = os.path.join(inp, 'weights')


class Training(AttributeInspect):
    kernel_type = 'swin_large_patch4_window7_224'  # 'efficientnetv2_m', 'swin_large_patch4_window7_224'
    epochs = 5
    warm_up_epochs = 2
    n_folds = 5
    batch_size = 2
    patience = float('inf')
    num_workers = 4
    image_size = 224
    use_meta = True
    lr = 5e-6
    scheduler = 'LambdaLR'
    criterion = 'BCEWithLogitsLoss'
    # for efficientnet
    drop_rate = 0.3
    drop_path_rate = 0.2
    #
    if not use_meta:
        warm_up_epochs = 0
