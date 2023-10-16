import pathlib
import os
class Args():
    ROOT = pathlib.Path().absolute()

    # RSNA unzip directory
    RSNA_ROOT_DIR = ''

    # zip file download from kaggle
    ZIP_FILE = ''
    # e.g
    # ZIP_FILE = '/home/kcc/Downloads/rsna-intracranial-hemorrhage-detection.zip'



    # dicom file path
    TRAIN_DICOM_DIR = os.path.join(RSNA_ROOT_DIR, 'stage_2_train')
    TEST_DICOM_DIR = os.path.join(RSNA_ROOT_DIR, 'stage_2_test')

    # Output meta data path
    META_DATA_PATH = os.path.join(ROOT, 'datas', 'meta_data')

    # output image file path #edit
    ALL_PNG_IMAGE = os.path.join(ROOT, 'datas', 'proc')


    TRAIN_CSV_PATH = os.path.join(ROOT, 'datas', 'csv')

    # FL output file path
    FL_PATH = os.path.join(ROOT, 'FL')

    FL_META_DATA_PATH = os.path.join(ROOT, 'FL', "meta_data")

    FL_SITE_META_DATA_PATH = os.path.join(ROOT, 'FL', "site_meta_csv")


    FL_SITE_CSV_PATH = os.path.join(ROOT, 'FL', "site_csv")

    FL_SITE_IMAGE_PATH = os.path.join(ROOT, 'FL', "site_images")
    
    FL_TEST_CSV_PATH = os.path.join(ROOT, 'FL', "test_csv")


if __name__ == "__main__":
    import os
    os.makedirs(Args.META_DATA_PATH, exist_ok=True)
    os.makedirs(Args.ALL_PNG_IMAGE, exist_ok=True)
    os.makedirs(Args.TRAIN_CSV_PATH, exist_ok=True)
    os.makedirs(Args.FL_PATH, exist_ok=True)
    os.makedirs(Args.FL_META_DATA_PATH, exist_ok=True)
    os.makedirs(Args.FL_SITE_META_DATA_PATH, exist_ok=True)
    os.makedirs(Args.FL_SITE_CSV_PATH, exist_ok=True)
    os.makedirs(Args.FL_SITE_IMAGE_PATH, exist_ok=True)
    os.makedirs(Args.FL_TEST_CSV_PATH, exist_ok=True)