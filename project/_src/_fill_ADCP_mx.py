import numpy as np

def fill_mx(DATA):
    header_keys = ['RDIFileName', 'RDISystem', 'RDIPingsPerEns', 'RDISecPerPing', 'RDIEnsDate', 'RDIEnsTime',
                   'RDIEnsInterval', 'RDIBin1Mid', 'RDIBinSize']
    fileheader = {k: v for k, v in DATA.items() if k in header_keys}

    no_ensembles = len(DATA['SerEnsembles'].flatten())
    no_bins = len(DATA['SerBins'].flatten())

    ensembles = DATA['SerEnsembles'].flatten().astype('int')
    bins = DATA['SerBins'].flatten().astype('int')

    first_bin = np.reshape(DATA['RDIBin1Mid'].astype('float'), 1)[0]
    bin_size = np.reshape(DATA['RDIBinSize'].astype('float'), 1)[0]

    levels = np.round(np.arange(first_bin, first_bin + bin_size * no_bins, bin_size), 2)

    timestamps = []
    for yr, mo, da, hh, mm, ss, hu in zip(DATA['SerYear'].flatten(), DATA['SerMon'].flatten(),
                                          DATA['SerDay'].flatten(), DATA['SerHour'].flatten(),
                                          DATA['SerMin'].flatten(), DATA['SerSec'].flatten(),
                                          DATA['SerHund'].flatten()):
        ts = (f'{str(int(da)).zfill(2)}/{str(int(mo)).zfill(2)}/{str(int(yr)).zfill(2)} '
              f'{str(int(hh)).zfill(2)}:{str(int(mm)).zfill(2)}:'
              f'{str(int(ss)).zfill(2)}.{str(int(hu)).zfill(2)}')
        timestamps.append(ts)

    latitudes = np.round(DATA['AnLLatDeg'].flatten(), 8)
    longitudes = np.round(DATA['AnLLonDeg'].flatten(), 8)
    bt1 = DATA['AnBTDepthcmB1'].flatten()
    bt2 = DATA['AnBTDepthcmB2'].flatten()
    bt3 = DATA['AnBTDepthcmB3'].flatten()
    bt4 = DATA['AnBTDepthcmB4'].flatten()


    # ADCP [single_magnitude, single_direction, bin_level, bin]
    # META [ensemble_no, timestamp, latitude, longitude]
    # BTRA [ensemble_no, timestamp, bottom_track]
    ADCP = np.zeros((no_ensembles, no_bins, 4), dtype=object)
    META = np.zeros((no_ensembles, 4), dtype=object)
    BTRA = np.zeros((no_ensembles, 3), dtype=object)

    ADCP[:, :, 0] = DATA['SerMagmmpersec'].T.astype('int')
    ADCP[:, :, 1] = DATA['SerDir10thDeg'].T.astype('int')
    ADCP[:, :, 2] = levels
    ADCP[:, :, 3] = bins
    ADCP[ADCP == -32768] = 0
    ADCP[:, :, 1] = ADCP[:, :, 1] / 10


    META[:, 0] = ensembles
    META[:, 1] = timestamps
    META[:, 2] = latitudes
    META[:, 3] = longitudes

    BTRA[:, 0] = ensembles
    BTRA[:, 1] = timestamps
    BTRA[:, 2] = np.mean([bt1, bt2, bt3, bt4], axis=0) / 100


    return fileheader, no_ensembles, no_bins, bin_size, ADCP, META, BTRA