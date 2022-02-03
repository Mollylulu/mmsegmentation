import os
import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument('--data_dir', '-dd', help='the last level dir do not end with /')
parser.add_argument('--save_txt', '-st')
parser.add_argument('--image_suffix', '-suffix', default='.png')
parser.add_argument('--data_root', '-dr', 
                    help='data root in dateset param, which is going to be removed from txt, REMEMBER end with NO / ')
args = parser.parse_args()


if __name__ == '__main__':
    data_dir = args.data_dir
    save_txt = args.save_txt
    suffix = args.image_suffix
    data_root = args.data_root

    folder = os.path.basename(data_dir)
    files = [os.path.join(dp, f) for dp, dn, fn in os.walk(data_dir) for f in fn]
    files = [f.replace(data_dir, '')[1:] for f in files if os.path.isfile(f) and suffix in f]  
    # [1:] aims to drop out the '/'in front of the image 
    random.shuffle(files)
    train_lens = int(len(files)*0.8)
    train_files = files[:train_lens]
    val_files = files[train_lens:]
    with open(save_txt, 'w') as w:
        for line in train_files:
            print(line)
            root = data_dir.split(data_root)[1] if data_root else '' #[0] is '' from ['', 'data/hushi_0812/Segmentation/train']
            # import pdb;pdb.set_trace()
            w.write('{}'.format(os.path.join(root, line)))
            w.write('\n')
    with open(save_txt.replace('train', 'val'), 'w') as val_f:
        for line in val_files:
            print(line)
            root = data_dir.split(data_root)[1] if data_root else '' #[0] is '' from ['', 'data/hushi_0812/Segmentation/train']
            # import pdb;pdb.set_trace()
            val_f.write('{}'.format(os.path.join(root, line)))
            val_f.write('\n')