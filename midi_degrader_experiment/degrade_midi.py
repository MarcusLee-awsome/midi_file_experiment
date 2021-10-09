import degrader
import fileio
import numpy as np
from glob import glob
import os


def main():
    midi_paths = glob('./data/train/*.midi')  # you need to revise it
    midi_path = '../midi_degrader/data/degrade_midi_data'  # 添加的路径为通过degrade之后的路径
    degrader1 = degrader.Degrader()
    for path in midi_paths:
        # 新加的data_augmentation
        path_name = os.path.split(path)[1]
        #shortname, extension = os.path.splitext(path_name)
        note_df = fileio.midi_to_df(path)
        new_note_df, length= degrader1.degrade(note_df)
        #print(type(new_note_df))
        midi_path_name = midi_path +'/'+path_name
        #print(midi_path_name)
        midi_file = fileio.df_to_midi(df=new_note_df, midi_path=midi_path_name, existing_midi_path=path)

if __name__ == '__main__':
    main()
