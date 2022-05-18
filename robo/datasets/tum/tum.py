from robo.datasets.dataset import Dataset
import wget

# def bar_progress(current, total, width=80):
#   progress_message = "Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total)
#   # Don't use print() as it will print in new line every time.
#   sys.stdout.write("\r" + progress_message)
#   sys.stdout.flush()


class TumDataset(Dataset):
    def download(self):
        # url = "http://www.doc.ic.ac.uk/~ahanda/living_room_traj1_frei_png.tar.gz"
        # print(wget.download(url, out="test/"))
        pass

    def remove(self):
        pass
