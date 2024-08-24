import argparse
import os 
import random

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', type=str, default="data/babylm_2024")
    args = parser.parse_args()
    return args

def main():
       
    SEED = 42
    random.seed(SEED)
    
    args = parse_args()
    input_dir = args.input_dir
    
    if "babylm" not in input_dir:
        raise ValueError("input_dir must contain 'babylm'")
    
    if not os.path.exists(os.path.join(input_dir, "en/raw")):
        os.makedirs(os.path.join(input_dir, "en/raw"))
        
    # train
    train_data = ""
    for file in os.listdir(os.path.join(input_dir, "train_100M")):
        with open(os.path.join(input_dir, "train_100M", file), "r") as f:
            train_data += f.read()
            train_data += "\n"
    

    with open(os.path.join(input_dir, "en/raw/train.txt"), "w") as f:
        f.write(train_data)
        
    # test
    test_data = ""
    for file in os.listdir(os.path.join(input_dir, "test")):
        with open(os.path.join(input_dir, "test", file), "r") as f:
            test_data += f.read()
            test_data += "\n"
            
    test_data = test_data.split("\n")
    random.shuffle(test_data)
    test_data = "\n".join(test_data)
            
    with open(os.path.join(input_dir, "en/raw/test.txt"), "w") as f:
        f.write(test_data)
    
    # validation    
    val_data = ""
    for file in os.listdir(os.path.join(input_dir, "dev")):
        with open(os.path.join(input_dir, "dev", file), "r") as f:
            val_data += f.read()
            val_data += "\n"
            
    val_data = val_data.split("\n")
    random.shuffle(val_data)
    val_data = "\n".join(val_data)
    
    with open(os.path.join(input_dir, "en/raw/validation.txt"), "w") as f:
        f.write(val_data)
        
    print("Done combining babylm data")
    

if __name__ == '__main__':
    main()