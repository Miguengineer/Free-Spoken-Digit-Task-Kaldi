#%%

def make_utt_dict(path):
    import os
    system_path = '/home/miguel/FSDD_Project'
    utt_dict = {}
    files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    for utt_idx in range(len(files)):
        utt_dict[utt_idx] = os.path.join(system_path, path, files[utt_idx])
    return utt_dict


def make_spk2utt(utt_dict, dummy=True):
    if not dummy:
        print("Not dummy model not yet implemented!")
        return
    # Utt idxs are 1-based indexing
    file = open("spk2utt", "w")
    for utt_idx in range(1, len(utt_dict) + 1):
        file.write("%04d %04d \n" % (utt_idx, utt_idx))
    file.close()


def make_utt2speak(utt_dict, dummy=True):
    if not dummy:
        print("Not dummy model not yet implemented!")
        return
    # Utt idxs are 1-based indexing
    file = open("utt2spk", "w")
    for utt_idx in range(1, len(utt_dict) + 1):
        file.write("%04d %04d \n" % (utt_idx, utt_idx))
    file.close()


def make_spk2gender(utt_dict, dummy=True):
    if not dummy:
        print("Not dummy model not yet implemented!")
        return
    # Utt idxs are 1-based indexing
    file = open("spk2gender", "w")
    for utt_idx in range(1, len(utt_dict) + 1):
        file.write("%04d m \n" % utt_idx)
    file.close()


def make_wav(utt_dict):
    file = open("wav.scp", "w")
    for utt_idx in range(1, len(utt_dict) + 1):
        file.write("%04d " % utt_idx + utt_dict[utt_idx - 1] + "\n")
    file.close()


def make_text(utt_dict):
    file = open("text", "w")
    digits_dict = {"0": "Zero", "1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six",
                   "7": "Seven", "8": "Eight", "9": "Nine"}
    for utt_idx in range(1, len(utt_dict) + 1):
        filename = utt_dict[utt_idx - 1]
        # First digit before _ is the actual pronounced digit
        spoken_digit = filename.split("/")[-1].split("_")[0]
        file.write("%04d " % utt_idx + digits_dict[spoken_digit] + "\n")
    file.close()

utt_dict_train = make_utt_dict('exp_data/train')