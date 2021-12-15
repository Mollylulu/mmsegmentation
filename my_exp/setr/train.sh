source .bashrc_debug
conda activate smore
cd /home/lunaluo/git/mmsegmentation
./tools/dist_train.sh configs/setr/setr_pup_512x512_160k_b16_ade20k.py 4 --work-dir my_exp/setr/output
