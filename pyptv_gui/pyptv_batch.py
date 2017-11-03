""" PyPTV_BATCH is the script for the 3D-PTV (http://ptv.origo.ethz.ch) written in 
Python/Enthought Traits GUI/Numpy/Chaco

Example:
>> python pyptv_batch.py experiments/exp1 10001 10022

where 10001 is the first file in sequence and 10022 is the last one
the present "active" parameters are kept intact except the sequence


"""
from __future__ import print_function
from __future__ import absolute_import


# from scipy.misc import imread
import os
import sys
import numpy as np

# project specific inputs
from . import parameters as par
from . import general

import time


# directory from which we run the software
cwd = os.getcwd()


# import pdb; pdb.set_trace()



def sequence_tracking(n_img):
    # get following variables from the parameters:
    # n_camera, seq_first, seq_last, base_name
    import ptv1 as ptv
    
    sequenceParams = par.SequenceParams(n_img, path=par.temp_path)
    sequenceParams.read()
    (base_name, seq_first, seq_last) = (
        sequenceParams.base_name, sequenceParams.first, sequenceParams.last)

    print ("Starting sequence action")

    ptv.py_sequence_init(0)
    stepshake = ptv.py_get_from_sequence_init()
    if not stepshake:
        stepshake = 1
    print(stepshake)
    temp_img = np.array([], dtype=np.ubyte)
    for i in range(seq_first, seq_last + 1, stepshake):
        if i < 10:
            seq_ch = "%01d" % i
        elif i < 100:
            seq_ch = "%02d" % i
        else:
            seq_ch = "%03d" % i
        for j in range(n_img):
            img_name = base_name[j] + seq_ch
            print(("Setting image: ", img_name))
            try:
                temp_img = imread(img_name).astype(np.ubyte)
            except:
                raise ValueError("Error reading file")

            ptv.py_set_img(temp_img, j)

        ptv.py_sequence_loop(0, i)


#	forward tracking
    run_info = ptv.py_trackcorr_init()
    print(run_info.get_sequence_range())
    for step in range(*run_info.get_sequence_range()):
        print(step)
        ptv.py_trackcorr_loop(run_info, step, display=0)

    ptv.py_trackcorr_finish(run_info, step + 1)
    print("tracking without display finished")
    # RON - cancled back tracking due to bug 
    ptv.py_trackback_c()
    print("tracking backwards is finished")


def sequence(n_img):
    # get following variables from the parameters:
    # n_camera, seq_first, seq_last, base_name
    import ptv1 as ptv
    
    sequenceParams = par.SequenceParams(n_img, path=par.temp_path)
    sequenceParams.read()
    (base_name, seq_first, seq_last) = (
        sequenceParams.base_name, sequenceParams.first, sequenceParams.last)

    print ("Starting sequence action")

    ptv.py_sequence_init(0)
    stepshake = ptv.py_get_from_sequence_init()
    if not stepshake:
        stepshake = 1
    print(stepshake)
    temp_img = np.array([], dtype=np.ubyte)
    for i in range(seq_first, seq_last + 1, stepshake):
        if i < 10:
            seq_ch = "%01d" % i
        elif i < 100:
            seq_ch = "%02d" % i
        else:
            seq_ch = "%03d" % i
        for j in range(n_img):
            img_name = base_name[j] + seq_ch
            print(("Setting image: ", img_name))
            try:
                temp_img = imread(img_name).astype(np.ubyte)
            except:
                print ("Error reading file")

            ptv.py_set_img(temp_img, j)

        ptv.py_sequence_loop(0, i)


def run_batch(new_seq_first, new_seq_last):
    #  	import pdb; pdb.set_trace()
    import ptv1 as ptv
    
    ptv.py_init_proc_c()
    ptv.py_start_proc_c()  # or ptv.py_init_proc_c()?
    ptvParams = par.PtvParams(path=par.temp_path)
    ptvParams.read()
    (n_img, img_name, img_cal, hp_flag, allCam_flag, tiff_flag, imx, imy, pix_x, pix_y, chfield, mmp_n1, mmp_n2, mmp_n3, mmp_d) = \
        (ptvParams.n_img, ptvParams.img_name, ptvParams.img_cal, ptvParams.hp_flag, ptvParams.allCam_flag, ptvParams.tiff_flag,
         ptvParams.imx, ptvParams.imy, ptvParams.pix_x, ptvParams.pix_y, ptvParams.chfield, ptvParams.mmp_n1, ptvParams.mmp_n2, ptvParams.mmp_n3, ptvParams.mmp_d)
# read the sequence parameters
    sequenceParams = par.SequenceParams(n_img, path=par.temp_path)
    sequenceParams.read()
    (base_name, seq_first, seq_last) = (
        sequenceParams.base_name, sequenceParams.first, sequenceParams.last)
# write the new sequence parameters
    par.SequenceParams(n_img, base_name,
                       new_seq_first, new_seq_last, path=par.temp_path).write()
    # if you need sequence and tracking:
    sequence_tracking(n_img)

    # if you need sequence only:
    # sequence(n_img)
    
def main(sys_argv, repetitions=1):
    """ runs the batch 
    Usage: 
        main([software_path, exp_dir, first, last], [repetitions])
        
    Parameters:
        list of 4 parameters in this order:
        software_path : directory of pyptv_batch.py    
        exp_dir : directory with the experiment data
        first, last : integer, number of a first and last frame
        repetitions : int, default = 1, optional
    """
    software_path = os.path.split(os.path.abspath(sys_argv[0]))[0]
    print(('software_path='), software_path)
    
    try:
        os.chdir(software_path)
    except:
        raise ValueError("Error in instalation or software path")
    
    import string
    src_path = string.replace(software_path,'pyptv_gui','src_c')
    print('Source path for ptv1.so is %s' % src_path)
    sys.path.append(src_path)
    import ptv1 as ptv
    
    start = time.time()
    
    try:
        exp_path = os.path.abspath(sys_argv[1])
        print('exp_path= %s' % exp_path)
        os.chdir(exp_path)
        print(os.getcwd())
    except:
        raise ValueError('Wrong experimental directory %s' % exp_path)
        

# RON - make a res dir if it not found

    if 'res' not in os.listdir(sys_argv[1]):
        print (" 'res' folder not found. creating one")
        os.makedirs(os.path.join(sys_argv[1],'res'))
    
    
    for i in range(repetitions):
        try: # strings       
            seq_first = eval(sys_argv[2])
            seq_last = eval(sys_argv[3])
        except: # integers
            seq_first = sys_argv[2]
            seq_last = sys_argv[3]
       
        try:
            run_batch(seq_first, seq_last)
        except:
            print("something wrong with the software or folder")
            general.printException()

    end = time.time()
    print ('time lapsed %f sec' % (end - start))
    


if __name__ == '__main__':
    """ pyptv_batch.py enables to run a sequence without GUI
    It can run from a command shell: 
        python pyptv_batch.py ~/test_cavity 10000 10004
    
    or from Python:
        
        import sys, os
        sys.path.append(os.path.abspath('openptv/openptv-python/pyptv_gui'))
        from pyptv_batch import main
        batch_command = '/openptv/openptv-python/pyptv_gui/pyptv_batch.py'
        PyPTV_working_directory = '/openptv/Working_folder/'
        mi,mx = 65119, 66217
        main([batch_command,PyPTV_working_directory, mi, mx])
        """
    if len(sys.argv) < 4:
        print("Wrong number of inputs, usage: python pyptv_batch.py \
        experiments/exp1 seq_first seq_last")
        raise ValueError('wrong number of inputs')
        

    main(sys.argv)
    
    

