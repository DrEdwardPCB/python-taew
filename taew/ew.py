import copy
# numpy
import numpy as np
# pandas
import pandas as pd


def wave2_fibonacci_check(wave2_end, wave1_start, wave1_end):
    # Wave 2 is typically 50%, 61.8%, 76.4%, or 85.4% of wave 1
    wave2_endabs = abs(wave2_end)
    wave1_startabs = abs(wave1_start)
    wave1_endabs = abs(wave1_end)
    fibonacci_ratio = [0.146, 0.236, 0.382, 0.5, 0.618, 0.764, 0.854]
    for ratio in fibonacci_ratio:
        if wave2_endabs <= (wave1_endabs - (wave1_endabs - wave1_startabs) * ratio) * 1.001 and wave2_endabs >= (
                wave1_endabs - (wave1_endabs - wave1_startabs) * ratio) * 0.995:
            return True
        # endif
    # endfor
    return False


def wave3_fibonacci_check(wave3_end, wave2_start, wave2_end):
    # Wave 3 is typically 161.8% of wave 1
    wave3_endabs = abs(wave3_end)
    wave2_startabs = abs(wave2_start)
    wave2_endabs = abs(wave2_end)
    fibonacci_ratio = [1.236, 1.618, 2.00, 2.618, 3.236, 4.236]
    for ratio in fibonacci_ratio:
        if wave3_endabs <= (wave2_endabs - (wave2_endabs - wave2_startabs) * ratio) * 1.001 and wave3_endabs >= (
                wave2_endabs - (wave2_endabs - wave2_startabs) * ratio) * 0.995:
            return True
        # endif
    # endfor
    return False


def wave4_fibonacci_check(wave4_end, wave3_start, wave3_end):
    # Wave 3 is typically 161.8% of wave 1
    wave4_endabs = abs(wave4_end)
    wave3_startabs = abs(wave3_start)
    wave3_endabs = abs(wave3_end)
    fibonacci_ratio = [0.146, 0.236, 0.382, 0.5, 0.618, 0.764, 0.854]
    for ratio in fibonacci_ratio:
        if wave4_endabs <= (wave3_endabs - (wave3_endabs - wave3_startabs) * ratio) * 1.001 and wave3_endabs >= (
                wave3_endabs - (wave3_endabs - wave3_startabs) * ratio) * 0.995:
            return True
        # endif
    # endfor
    return False


def wave5_fibonacci_check(wave5_end, wave1_start, wave1_end, wave3_start, wave3_end, wave4_end):
    wave5_endabs = abs(wave5_end)
    wave1_startabs = abs(wave1_start)
    wave1_endabs = abs(wave1_end)
    wave3_startabs = abs(wave3_start)
    wave3_endabs = abs(wave3_end)
    wave4_endabs = abs(wave4_end)

    wave5_y = wave5_endabs - wave4_endabs
    wave1_y = wave1_endabs - wave1_startabs
    wave4_y = abs(wave4_endabs - wave3_endabs)
    wave1plus3_y = wave1_y + (wave3_endabs - wave3_startabs)
    if wave5_y >= wave4_y and wave5_y <= (wave4_y * 2):
        return True
    if wave5_y >= wave1_y * 0.95 and wave5_y <= wave1_y * 1.05:
        return True
    fibonacci_ratio = [0.382, 0.618, 0.764]
    for ratio in fibonacci_ratio:
        if wave5_y <= wave1plus3_y * ratio * 1.05 and wave5_y >= wave1plus3_y * ratio * 0.95:
            return True
        # end
    # end
    return False


def diff(data):
    # accept list of any number
    output_diff = []
    for i in range(1, len(data)):
        output_diff.append((data[i - 1] - data[i]))
    # return list of number
    return output_diff


def otherThan(data, otherthan=0):
    # accept list and a anytype option
    output_otherthan = []
    for i in range(len(data)):
        if data[i] != otherthan:
            output_otherthan.append(True)
        else:
            output_otherthan.append(False)
    # return list of boolean
    return output_otherthan


def trimming(data, determineArray):
    # accept list of any type and list of boolean
    if len(data) != len(determineArray):
        raise Exception('array/list size not equal')
    filtered_data = []
    for i in range(len(data)):
        if determineArray[i]:
            filtered_data.append(data[i])
    return filtered_data


##############################################
def Alternative_ElliottWave_label_upward(data):
    v = data
    j = range(len(data))
    x = []
    z = []
    b = []
    # finding the high point and low point
    for i in range(1, len(v) - 1):
        if (v[i] <= v[i + 1] and v[i - 1] >= v[i]) or (v[i] >= v[i + 1] and v[i - 1] <= v[i]):
            # finding peaks and valleys and then place in a new matrix
            x.append(v[i])
            z.append(j[i])

            diff4x = diff(x)
            diff4x.insert(0, 1)

            diff4z = diff(x)
            diff4z.insert(0, 1)

            x = trimming(x, otherThan(diff4x, otherthan=0))
            z = trimming(z, otherThan(diff4z, otherthan=0))

            b = [x, z]
        # end
    # end
    # for each point find the first wave
    listofCandidateWave = []
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i] < x[j]:
                wave = {
                    'x': [x[i], x[j]],
                    'z': [z[i], z[j]],
                    'searchIndex': j,
                }
                listofCandidateWave.append(wave)
            # end
        # end
    # end

    print(len(listofCandidateWave))
    print('successfully filter out candidate wave')

    listofCandidateWave12 = []

    for i in range(len(listofCandidateWave)):
        startSearchIndex = listofCandidateWave[i]['searchIndex']
        # third point should be within 0.382+-5%? we take 0.382+*1.05=0.4011
        timeInterval = (listofCandidateWave[i]['z'][1] - listofCandidateWave[i]['z'][0]) * 0.4011
        for j in range(startSearchIndex, len(x)):
            # wave 2 is a drop and point should at around 0.382 and wave 2 drop destination is higher than start of wave 1
            if x[j] < listofCandidateWave[i]['x'][1] and z[j] - listofCandidateWave[i]['z'][1] <= timeInterval and x[
                j] > listofCandidateWave[i]['x'][0] and wave2_fibonacci_check(x[j], listofCandidateWave[i]['x'][0],
                                                                              listofCandidateWave[i]['x'][1]):
                currWave = copy.deepcopy(listofCandidateWave[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave12.append(currWave)

            # end
        # end
    # end
    print(len(listofCandidateWave12))
    print('successfully filter out candidate wave 12')
    listofCandidateWave123 = []
    for i in range(len(listofCandidateWave12)):
        startSearchIndex = listofCandidateWave12[i]['searchIndex']
        # forth point should be within 1.618+-5%? we take 1.618+*1.05=1.6989
        timeInterval = (listofCandidateWave12[i]['z'][1] - listofCandidateWave12[i]['z'][0]) * 1.6989
        for j in range(startSearchIndex, len(x)):
            # wave 3 is a rise and point should at around 1.618 and wave 3 must be the longest wave
            if x[j] > listofCandidateWave12[i]['x'][2] and z[j] - listofCandidateWave12[i]['z'][2] <= timeInterval and \
                    z[j] - listofCandidateWave12[i]['z'][2] >= listofCandidateWave12[i]['z'][1] - \
                    listofCandidateWave12[i]['z'][0] and z[j] - listofCandidateWave12[i]['z'][2] >= \
                    listofCandidateWave12[i]['z'][2] - listofCandidateWave12[i]['z'][1] and wave3_fibonacci_check(x[j],
                                                                                                                  listofCandidateWave12[
                                                                                                                      i][
                                                                                                                      'x'][
                                                                                                                      1],
                                                                                                                  listofCandidateWave12[
                                                                                                                      i][
                                                                                                                      'x'][
                                                                                                                      2]):
                currWave = copy.deepcopy(listofCandidateWave12[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave123.append(currWave)

            # end
        # end
    # end
    print(len(listofCandidateWave123))
    print('successfully filter out candidate wave123')

    listofCandidateWave1234 = []
    for i in range(len(listofCandidateWave123)):
        startSearchIndex = listofCandidateWave123[i]['searchIndex']
        # forth point should be within 0.382+-5%? we take 0.382+*1.05=0.4011
        timeInterval = (listofCandidateWave123[i]['z'][1] - listofCandidateWave123[i]['z'][0]) * 0.4011
        wave3length = listofCandidateWave123[i]['z'][3] - listofCandidateWave123[i]['z'][2]
        for j in range(startSearchIndex, len(x)):
            # wave 4 is a fall and point should at around 1.618 and wave 4 must not fall below the end of wave 1
            if x[j] < listofCandidateWave123[i]['x'][3] and z[j] - listofCandidateWave123[i]['z'][3] <= timeInterval and \
                    x[j] > listofCandidateWave123[i]['x'][1] and z[j] - listofCandidateWave123[i]['z'][
                3] <= wave3length and wave4_fibonacci_check(x[j], listofCandidateWave123[i]['x'][2],
                                                            listofCandidateWave123[i]['x'][3]):
                currWave = copy.deepcopy(listofCandidateWave123[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave1234.append(currWave)

            # end
        # end
    # end

    print(len(listofCandidateWave1234))
    print('successfully filter out candidate wave1234')

    listofCandidateWave12345 = []
    for i in range(len(listofCandidateWave1234)):
        startSearchIndex = listofCandidateWave1234[i]['searchIndex']
        # forth point should be within 01.618+-5%? we take 1.618+*1.05=0.4011
        timeInterval = (listofCandidateWave1234[i]['z'][1] - listofCandidateWave1234[i]['z'][0]) * 1.6989
        wave3length = listofCandidateWave1234[i]['z'][3] - listofCandidateWave1234[i]['z'][2]
        for j in range(startSearchIndex, len(x)):
            # wave 4 is a fall and point should at around 1.618 and wave 4 must not fall below the end of wave 1
            if x[j] > listofCandidateWave1234[i]['x'][4] and z[j] - listofCandidateWave1234[i]['z'][
                4] <= timeInterval and z[j] - listofCandidateWave1234[i]['z'][
                4] <= wave3length and wave5_fibonacci_check(x[j], listofCandidateWave1234[i]['x'][0],
                                                            listofCandidateWave1234[i]['x'][1],
                                                            listofCandidateWave1234[i]['x'][2],
                                                            listofCandidateWave1234[i]['x'][3],
                                                            listofCandidateWave1234[i]['x'][4]):
                currWave = copy.deepcopy(listofCandidateWave1234[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave12345.append(currWave)

            # end
        # end
    # end
    print(len(listofCandidateWave12345))
    print('successfully filter out candidate wave12345')
    return listofCandidateWave12345


########################################
##############################################
def Alternative_ElliottWave_label_downward(data):
    v = data
    j = range(len(data))
    x = []
    z = []
    b = []
    # finding the high point and low point
    for i in range(1, len(v) - 1):
        if (v[i] <= v[i + 1] and v[i - 1] >= v[i]) or (v[i] >= v[i + 1] and v[i - 1] <= v[i]):
            # finding peaks and valleys and then place in a new matrix
            x.append(v[i])
            z.append(j[i])

            diff4x = diff(x)
            diff4x.insert(0, 1)

            diff4z = diff(x)
            diff4z.insert(0, 1)

            x = trimming(x, otherThan(diff4x, otherthan=0))
            z = trimming(z, otherThan(diff4z, otherthan=0))

            b = [x, z]
        # end
    # end
    # for each point find the first wave
    listofCandidateWave = []
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i] > x[j]:
                wave = {
                    'x': [x[i], x[j]],
                    'z': [z[i], z[j]],
                    'searchIndex': j,
                }
                listofCandidateWave.append(wave)
            # end
        # end
    # end

    print(len(listofCandidateWave))
    print('successfully filter out candidate wave')

    listofCandidateWave12 = []

    for i in range(len(listofCandidateWave)):
        startSearchIndex = listofCandidateWave[i]['searchIndex']
        # third point should be within 0.382+-5%? we take 0.382+*1.05=0.4011
        timeInterval = (listofCandidateWave[i]['z'][1] - listofCandidateWave[i]['z'][0]) * 0.4011
        for j in range(startSearchIndex, len(x)):
            # wave 2 is a drop and point should at around 0.382 and wave 2 drop destination is higher than start of wave 1
            if x[j] > listofCandidateWave[i]['x'][1] and z[j] - listofCandidateWave[i]['z'][1] <= timeInterval and x[
                j] < listofCandidateWave[i]['x'][0] and wave2_fibonacci_check(x[j], listofCandidateWave[i]['x'][0],
                                                                              listofCandidateWave[i]['x'][1]):
                currWave = copy.deepcopy(listofCandidateWave[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave12.append(currWave)

            # end
        # end
    # end
    print(len(listofCandidateWave12))
    print('successfully filter out candidate wave 12')
    listofCandidateWave123 = []
    for i in range(len(listofCandidateWave12)):
        startSearchIndex = listofCandidateWave12[i]['searchIndex']
        # forth point should be within 1.618+-5%? we take 1.618+*1.05=1.6989
        timeInterval = (listofCandidateWave12[i]['z'][1] - listofCandidateWave12[i]['z'][0]) * 1.6989
        for j in range(startSearchIndex, len(x)):
            # wave 3 is a rise and point should at around 1.618 and wave 3 must be the longest wave
            if x[j] < listofCandidateWave12[i]['x'][2] and z[j] - listofCandidateWave12[i]['z'][2] <= timeInterval and \
                    z[j] - listofCandidateWave12[i]['z'][2] >= listofCandidateWave12[i]['z'][1] - \
                    listofCandidateWave12[i]['z'][0] and z[j] - listofCandidateWave12[i]['z'][2] >= \
                    listofCandidateWave12[i]['z'][2] - listofCandidateWave12[i]['z'][1] and wave3_fibonacci_check(x[j],
                                                                                                                  listofCandidateWave12[
                                                                                                                      i][
                                                                                                                      'x'][
                                                                                                                      1],
                                                                                                                  listofCandidateWave12[
                                                                                                                      i][
                                                                                                                      'x'][
                                                                                                                      2]):
                currWave = copy.deepcopy(listofCandidateWave12[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave123.append(currWave)

            # end
        # end
    # end
    print(len(listofCandidateWave123))
    print('successfully filter out candidate wave123')

    listofCandidateWave1234 = []
    for i in range(len(listofCandidateWave123)):
        startSearchIndex = listofCandidateWave123[i]['searchIndex']
        # forth point should be within 0.382+-5%? we take 0.382+*1.05=0.4011
        timeInterval = (listofCandidateWave123[i]['z'][1] - listofCandidateWave123[i]['z'][0]) * 0.4011
        wave3length = listofCandidateWave123[i]['z'][3] - listofCandidateWave123[i]['z'][2]
        for j in range(startSearchIndex, len(x)):
            # wave 4 is a fall and point should at around 1.618 and wave 4 must not fall below the end of wave 1
            if x[j] > listofCandidateWave123[i]['x'][3] and z[j] - listofCandidateWave123[i]['z'][3] <= timeInterval and \
                    x[j] < listofCandidateWave123[i]['x'][1] and z[j] - listofCandidateWave123[i]['z'][
                3] <= wave3length and wave4_fibonacci_check(x[j], listofCandidateWave123[i]['x'][2],
                                                            listofCandidateWave123[i]['x'][3]):
                currWave = copy.deepcopy(listofCandidateWave123[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave1234.append(currWave)

            # end
        # end
    # end

    print(len(listofCandidateWave1234))
    print('successfully filter out candidate wave1234')

    listofCandidateWave12345 = []
    for i in range(len(listofCandidateWave1234)):
        startSearchIndex = listofCandidateWave1234[i]['searchIndex']
        # forth point should be within 01.618+-5%? we take 1.618+*1.05=0.4011
        timeInterval = (listofCandidateWave1234[i]['z'][1] - listofCandidateWave1234[i]['z'][0]) * 1.6989
        wave3length = listofCandidateWave1234[i]['z'][3] - listofCandidateWave1234[i]['z'][2]
        for j in range(startSearchIndex, len(x)):
            # wave 4 is a fall and point should at around 1.618 and wave 4 must not fall below the end of wave 1
            if x[j] < listofCandidateWave1234[i]['x'][4] and z[j] - listofCandidateWave1234[i]['z'][
                4] <= timeInterval and z[j] - listofCandidateWave1234[i]['z'][
                4] <= wave3length and wave5_fibonacci_check(x[j], listofCandidateWave1234[i]['x'][0],
                                                            listofCandidateWave1234[i]['x'][1],
                                                            listofCandidateWave1234[i]['x'][2],
                                                            listofCandidateWave1234[i]['x'][3],
                                                            listofCandidateWave1234[i]['x'][4]):
                currWave = copy.deepcopy(listofCandidateWave1234[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave12345.append(currWave)

            # end
        # end
    # end
    print(len(listofCandidateWave12345))
    print('successfully filter out candidate wave12345')
    return listofCandidateWave12345
########################################
# Traditional only make use of fibonacci retracement level, time interval does not necessary follow fibonacci series

##############################################
def Traditional_ElliottWave_label_upward(data):
    v = data
    j = range(len(data))
    x = []
    z = []
    b = []
    # finding the high point and low point
    for i in range(1, len(v) - 1):
        if (v[i] <= v[i + 1] and v[i - 1] >= v[i]) or (v[i] >= v[i + 1] and v[i - 1] <= v[i]):
            # finding peaks and valleys and then place in a new matrix
            x.append(v[i])
            z.append(j[i])

            diff4x = diff(x)
            diff4x.insert(0, 1)

            diff4z = diff(x)
            diff4z.insert(0, 1)

            x = trimming(x, otherThan(diff4x, otherthan=0))
            z = trimming(z, otherThan(diff4z, otherthan=0))

            b = [x, z]
        # end
    # end
    # for each point find the first wave
    listofCandidateWave = []
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i] < x[j]:
                wave = {
                    'x': [x[i], x[j]],
                    'z': [z[i], z[j]],
                    'searchIndex': j,
                }
                listofCandidateWave.append(wave)
            # end
        # end
    # end

    print(len(listofCandidateWave))
    print('successfully filter out candidate wave')

    listofCandidateWave12 = []

    for i in range(len(listofCandidateWave)):
        startSearchIndex = listofCandidateWave[i]['searchIndex']
        # third point should be within 0.382+-5%? we take 0.382+*1.05=0.4011
        # timeInterval=(listofCandidateWave[i]['z'][1]-listofCandidateWave[i]['z'][0])*0.4011
        for j in range(startSearchIndex, len(x)):
            # wave 2 is a drop and point should at around 0.382 and wave 2 drop destination is higher than start of wave 1
            if x[j] < listofCandidateWave[i]['x'][1] and x[j] > listofCandidateWave[i]['x'][
                0] and wave2_fibonacci_check(x[j], listofCandidateWave[i]['x'][0], listofCandidateWave[i]['x'][1]):
                currWave = copy.deepcopy(listofCandidateWave[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave12.append(currWave)

            # end
        # end
    # end
    print(len(listofCandidateWave12))
    print('successfully filter out candidate wave 12')
    listofCandidateWave123 = []
    for i in range(len(listofCandidateWave12)):
        startSearchIndex = listofCandidateWave12[i]['searchIndex']
        # forth point should be within 1.618+-5%? we take 1.618+*1.05=1.6989
        # timeInterval=(listofCandidateWave12[i]['z'][1]-listofCandidateWave12[i]['z'][0])*1.6989
        for j in range(startSearchIndex, len(x)):
            # wave 3 is a rise and point should at around 1.618 and wave 3 must be the longest wave
            if x[j] > listofCandidateWave12[i]['x'][2] and z[j] - listofCandidateWave12[i]['z'][2] >= \
                    listofCandidateWave12[i]['z'][1] - listofCandidateWave12[i]['z'][0] and z[j] - \
                    listofCandidateWave12[i]['z'][2] >= listofCandidateWave12[i]['z'][2] - \
                    listofCandidateWave12[i]['z'][1] and wave3_fibonacci_check(x[j], listofCandidateWave12[i]['x'][1],
                                                                               listofCandidateWave12[i]['x'][2]):
                currWave = copy.deepcopy(listofCandidateWave12[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave123.append(currWave)

            # end
        # end
    # end
    print(len(listofCandidateWave123))
    print('successfully filter out candidate wave123')

    listofCandidateWave1234 = []
    for i in range(len(listofCandidateWave123)):
        startSearchIndex = listofCandidateWave123[i]['searchIndex']
        # forth point should be within 0.382+-5%? we take 0.382+*1.05=0.4011
        timeInterval = (listofCandidateWave123[i]['z'][1] - listofCandidateWave123[i]['z'][0]) * 0.4011
        wave3length = listofCandidateWave123[i]['z'][3] - listofCandidateWave123[i]['z'][2]
        for j in range(startSearchIndex, len(x)):
            # wave 4 is a fall and point should at around 1.618 and wave 4 must not fall below the end of wave 1
            if x[j] < listofCandidateWave123[i]['x'][3] and z[j] - listofCandidateWave123[i]['z'][3] <= timeInterval and \
                    x[j] > listofCandidateWave123[i]['x'][1] and z[j] - listofCandidateWave123[i]['z'][
                3] <= wave3length and wave4_fibonacci_check(x[j], listofCandidateWave123[i]['x'][2],
                                                            listofCandidateWave123[i]['x'][3]):
                currWave = copy.deepcopy(listofCandidateWave123[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave1234.append(currWave)

            # end
        # end
    # end

    print(len(listofCandidateWave1234))
    print('successfully filter out candidate wave1234')

    listofCandidateWave12345 = []
    for i in range(len(listofCandidateWave1234)):
        startSearchIndex = listofCandidateWave1234[i]['searchIndex']
        # forth point should be within 01.618+-5%? we take 1.618+*1.05=0.4011
        timeInterval = (listofCandidateWave1234[i]['z'][1] - listofCandidateWave1234[i]['z'][0]) * 1.6989
        wave3length = listofCandidateWave1234[i]['z'][3] - listofCandidateWave1234[i]['z'][2]
        for j in range(startSearchIndex, len(x)):
            # wave 4 is a fall and point should at around 1.618 and wave 4 must not fall below the end of wave 1
            if x[j] > listofCandidateWave1234[i]['x'][4] and z[j] - listofCandidateWave1234[i]['z'][
                4] <= timeInterval and z[j] - listofCandidateWave1234[i]['z'][
                4] <= wave3length and wave5_fibonacci_check(x[j], listofCandidateWave1234[i]['x'][0],
                                                            listofCandidateWave1234[i]['x'][1],
                                                            listofCandidateWave1234[i]['x'][2],
                                                            listofCandidateWave1234[i]['x'][3],
                                                            listofCandidateWave1234[i]['x'][4]):
                currWave = copy.deepcopy(listofCandidateWave1234[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave12345.append(currWave)

            # end
        # end
    # end
    print(len(listofCandidateWave12345))
    print('successfully filter out candidate wave12345')
    return listofCandidateWave12345


########################################
##############################################
def Traditional_ElliottWave_label_downward(data):
    v = data
    j = range(len(data))
    x = []
    z = []
    b = []
    # finding the high point and low point
    for i in range(1, len(v) - 1):
        if (v[i] <= v[i + 1] and v[i - 1] >= v[i]) or (v[i] >= v[i + 1] and v[i - 1] <= v[i]):
            # finding peaks and valleys and then place in a new matrix
            x.append(v[i])
            z.append(j[i])

            diff4x = diff(x)
            diff4x.insert(0, 1)

            diff4z = diff(x)
            diff4z.insert(0, 1)

            x = trimming(x, otherThan(diff4x, otherthan=0))
            z = trimming(z, otherThan(diff4z, otherthan=0))

            b = [x, z]
        # end
    # end
    # for each point find the first wave
    listofCandidateWave = []
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i] > x[j]:
                wave = {
                    'x': [x[i], x[j]],
                    'z': [z[i], z[j]],
                    'searchIndex': j,
                }
                listofCandidateWave.append(wave)
            # end
        # end
    # end

    print(len(listofCandidateWave))
    print('successfully filter out candidate wave')

    listofCandidateWave12 = []

    for i in range(len(listofCandidateWave)):
        startSearchIndex = listofCandidateWave[i]['searchIndex']
        # third point should be within 0.382+-5%? we take 0.382+*1.05=0.4011
        # timeInterval=(listofCandidateWave[i]['z'][1]-listofCandidateWave[i]['z'][0])*0.4011
        for j in range(startSearchIndex, len(x)):
            # wave 2 is a drop and wave 2 drop destination is higher than start of wave 1
            if x[j] > listofCandidateWave[i]['x'][1] and x[j] < listofCandidateWave[i]['x'][
                0] and wave2_fibonacci_check(x[j], listofCandidateWave[i]['x'][0], listofCandidateWave[i]['x'][1]):
                currWave = copy.deepcopy(listofCandidateWave[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave12.append(currWave)

            # end
        # end
    # end
    print(len(listofCandidateWave12))
    print('successfully filter out candidate wave 12')
    listofCandidateWave123 = []
    for i in range(len(listofCandidateWave12)):
        startSearchIndex = listofCandidateWave12[i]['searchIndex']
        # forth point should be within 1.618+-5%? we take 1.618+*1.05=1.6989
        # timeInterval=(listofCandidateWave12[i]['z'][1]-listofCandidateWave12[i]['z'][0])*1.6989
        for j in range(startSearchIndex, len(x)):
            # wave 3 is a rise and wave 3 must be the longest wave
            if x[j] < listofCandidateWave12[i]['x'][2] and z[j] - listofCandidateWave12[i]['z'][2] >= \
                    listofCandidateWave12[i]['z'][1] - listofCandidateWave12[i]['z'][0] and z[j] - \
                    listofCandidateWave12[i]['z'][2] >= listofCandidateWave12[i]['z'][2] - \
                    listofCandidateWave12[i]['z'][1] and wave3_fibonacci_check(x[j], listofCandidateWave12[i]['x'][1],
                                                                               listofCandidateWave12[i]['x'][2]):
                currWave = copy.deepcopy(listofCandidateWave12[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave123.append(currWave)

            # end
        # end
    # end
    print(len(listofCandidateWave123))
    print('successfully filter out candidate wave123')

    listofCandidateWave1234 = []
    for i in range(len(listofCandidateWave123)):
        startSearchIndex = listofCandidateWave123[i]['searchIndex']
        # forth point should be within 0.382+-5%? we take 0.382+*1.05=0.4011
        timeInterval = (listofCandidateWave123[i]['z'][1] - listofCandidateWave123[i]['z'][0]) * 0.4011
        wave3length = listofCandidateWave123[i]['z'][3] - listofCandidateWave123[i]['z'][2]
        for j in range(startSearchIndex, len(x)):
            # wave 4 is a fall and wave 4 must not fall below the end of wave 1
            if x[j] > listofCandidateWave123[i]['x'][3] and z[j] - listofCandidateWave123[i]['z'][3] <= timeInterval and \
                    x[j] > listofCandidateWave123[i]['x'][1] and z[j] - listofCandidateWave123[i]['z'][
                3] <= wave3length and wave4_fibonacci_check(x[j], listofCandidateWave123[i]['x'][2],
                                                            listofCandidateWave123[i]['x'][3]):
                currWave = copy.deepcopy(listofCandidateWave123[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave1234.append(currWave)

            # end
        # end
    # end

    print(len(listofCandidateWave1234))
    print('successfully filter out candidate wave1234')

    listofCandidateWave12345 = []
    for i in range(len(listofCandidateWave1234)):
        startSearchIndex = listofCandidateWave1234[i]['searchIndex']
        # forth point should be within 01.618+-5%? we take 1.618+*1.05=0.4011
        timeInterval = (listofCandidateWave1234[i]['z'][1] - listofCandidateWave1234[i]['z'][0]) * 1.6989
        wave3length = listofCandidateWave1234[i]['z'][3] - listofCandidateWave1234[i]['z'][2]
        for j in range(startSearchIndex, len(x)):
            # wave 4 is a fall and point should at around 1.618 and wave 4 must not fall below the end of wave 1
            if x[j] < listofCandidateWave1234[i]['x'][4] and z[j] - listofCandidateWave1234[i]['z'][
                4] <= timeInterval and z[j] - listofCandidateWave1234[i]['z'][
                4] <= wave3length and wave5_fibonacci_check(x[j], listofCandidateWave1234[i]['x'][0],
                                                            listofCandidateWave1234[i]['x'][1],
                                                            listofCandidateWave1234[i]['x'][2],
                                                            listofCandidateWave1234[i]['x'][3],
                                                            listofCandidateWave1234[i]['x'][4]):
                currWave = copy.deepcopy(listofCandidateWave1234[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave12345.append(currWave)

            # end
        # end
    # end
    print(len(listofCandidateWave12345))
    print('successfully filter out candidate wave12345')
    return listofCandidateWave12345
########################################
##############################################
def Practical_ElliottWave3_label_upward(data):
    v = data
    j = range(len(data))
    x = []
    z = []
    b = []
    # finding the high point and low point
    for i in range(1, len(v) - 1):
        if (v[i] <= v[i + 1] and v[i - 1] >= v[i]) or (v[i] >= v[i + 1] and v[i - 1] <= v[i]):
            # finding peaks and valleys and then place in a new matrix
            x.append(v[i])
            z.append(j[i])

            diff4x = diff(x)
            diff4x.insert(0, 1)

            diff4z = diff(x)
            diff4z.insert(0, 1)

            x = trimming(x, otherThan(diff4x, otherthan=0))
            z = trimming(z, otherThan(diff4z, otherthan=0))

            b = [x, z]
        # end
    # end
    # for each point find the first wave
    listofCandidateWave = []
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i] < x[j]:
                wave = {
                    'x': [x[i], x[j]],
                    'z': [z[i], z[j]],
                    'searchIndex': j,
                }
                listofCandidateWave.append(wave)
            # end
        # end
    # end

    print(len(listofCandidateWave))
    print('successfully filter out candidate wave')

    listofCandidateWave12 = []

    for i in range(len(listofCandidateWave)):
        startSearchIndex = listofCandidateWave[i]['searchIndex']
        # third point should be within 0.382+-5%? we take 0.382+*1.05=0.4011
        timeInterval = (listofCandidateWave[i]['z'][1] - listofCandidateWave[i]['z'][0]) * 0.4011
        for j in range(startSearchIndex, len(x)):
            # wave 2 is a drop and point should at around 0.382 and wave 2 drop destination is higher than start of wave 1
            if x[j] < listofCandidateWave[i]['x'][1] and z[j] - listofCandidateWave[i]['z'][1] <= timeInterval and x[
                j] > listofCandidateWave[i]['x'][0] and wave2_fibonacci_check(x[j], listofCandidateWave[i]['x'][0],
                                                                              listofCandidateWave[i]['x'][1]):
                currWave = copy.deepcopy(listofCandidateWave[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave12.append(currWave)

            # end
        # end
    # end
    print(len(listofCandidateWave12))
    print('successfully filter out candidate wave 12')
    return listofCandidateWave12


########################################
##############################################
def Practical_ElliottWave4_label_downward(data):
    v = data
    j = range(len(data))
    x = []
    z = []
    b = []
    # finding the high point and low point
    for i in range(1, len(v) - 1):
        if (v[i] <= v[i + 1] and v[i - 1] >= v[i]) or (v[i] >= v[i + 1] and v[i - 1] <= v[i]):
            # finding peaks and valleys and then place in a new matrix
            x.append(v[i])
            z.append(j[i])

            diff4x = diff(x)
            diff4x.insert(0, 1)

            diff4z = diff(x)
            diff4z.insert(0, 1)

            x = trimming(x, otherThan(diff4x, otherthan=0))
            z = trimming(z, otherThan(diff4z, otherthan=0))

            b = [x, z]
        # end
    # end
    # for each point find the first wave
    listofCandidateWave = []
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i] > x[j]:
                wave = {
                    'x': [x[i], x[j]],
                    'z': [z[i], z[j]],
                    'searchIndex': j,
                }
                listofCandidateWave.append(wave)
            # end
        # end
    # end

    print(len(listofCandidateWave))
    print('successfully filter out candidate wave')

    listofCandidateWave12 = []

    for i in range(len(listofCandidateWave)):
        startSearchIndex = listofCandidateWave[i]['searchIndex']
        # third point should be within 0.382+-5%? we take 0.382+*1.05=0.4011
        timeInterval = (listofCandidateWave[i]['z'][1] - listofCandidateWave[i]['z'][0]) * 0.4011
        for j in range(startSearchIndex, len(x)):
            # wave 2 is a drop and point should at around 0.382 and wave 2 drop destination is higher than start of wave 1
            if x[j] > listofCandidateWave[i]['x'][1] and z[j] - listofCandidateWave[i]['z'][1] <= timeInterval and x[
                j] < listofCandidateWave[i]['x'][0] and wave2_fibonacci_check(x[j], listofCandidateWave[i]['x'][0],
                                                                              listofCandidateWave[i]['x'][1]):
                currWave = copy.deepcopy(listofCandidateWave[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave12.append(currWave)

            # end
        # end
    # end
    print(len(listofCandidateWave12))
    print('successfully filter out candidate wave 12')
    listofCandidateWave123 = []
    for i in range(len(listofCandidateWave12)):
        startSearchIndex = listofCandidateWave12[i]['searchIndex']
        # forth point should be within 1.618+-5%? we take 1.618+*1.05=1.6989
        timeInterval = (listofCandidateWave12[i]['z'][1] - listofCandidateWave12[i]['z'][0]) * 1.6989
        for j in range(startSearchIndex, len(x)):
            # wave 3 is a rise and point should at around 1.618 and wave 3 must be the longest wave
            if x[j] < listofCandidateWave12[i]['x'][2] and z[j] - listofCandidateWave12[i]['z'][2] <= timeInterval and \
                    z[j] - listofCandidateWave12[i]['z'][2] >= listofCandidateWave12[i]['z'][1] - \
                    listofCandidateWave12[i]['z'][0] and z[j] - listofCandidateWave12[i]['z'][2] >= \
                    listofCandidateWave12[i]['z'][2] - listofCandidateWave12[i]['z'][1] and wave3_fibonacci_check(x[j],
                                                                                                                  listofCandidateWave12[
                                                                                                                      i][
                                                                                                                      'x'][
                                                                                                                      1],
                                                                                                                  listofCandidateWave12[
                                                                                                                      i][
                                                                                                                      'x'][
                                                                                                                      2]):
                currWave = copy.deepcopy(listofCandidateWave12[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave123.append(currWave)

            # end
        # end
    # end
    print(len(listofCandidateWave123))
    print('successfully filter out candidate wave123')
    return listofCandidateWave123
########################################
##############################################
def Practical_ElliottWave5_label_upward(data):
    v = data
    j = range(len(data))
    x = []
    z = []
    b = []
    # finding the high point and low point
    for i in range(1, len(v) - 1):
        if (v[i] <= v[i + 1] and v[i - 1] >= v[i]) or (v[i] >= v[i + 1] and v[i - 1] <= v[i]):
            # finding peaks and valleys and then place in a new matrix
            x.append(v[i])
            z.append(j[i])

            diff4x = diff(x)
            diff4x.insert(0, 1)

            diff4z = diff(x)
            diff4z.insert(0, 1)

            x = trimming(x, otherThan(diff4x, otherthan=0))
            z = trimming(z, otherThan(diff4z, otherthan=0))

            b = [x, z]
        # end
    # end
    # for each point find the first wave
    listofCandidateWave = []
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i] < x[j]:
                wave = {
                    'x': [x[i], x[j]],
                    'z': [z[i], z[j]],
                    'searchIndex': j,
                }
                listofCandidateWave.append(wave)
            # end
        # end
    # end

    print(len(listofCandidateWave))
    print('successfully filter out candidate wave')

    listofCandidateWave12 = []

    for i in range(len(listofCandidateWave)):
        startSearchIndex = listofCandidateWave[i]['searchIndex']
        # third point should be within 0.382+-5%? we take 0.382+*1.05=0.4011
        timeInterval = (listofCandidateWave[i]['z'][1] - listofCandidateWave[i]['z'][0]) * 0.4011
        for j in range(startSearchIndex, len(x)):
            # wave 2 is a drop and point should at around 0.382 and wave 2 drop destination is higher than start of wave 1
            if x[j] < listofCandidateWave[i]['x'][1] and z[j] - listofCandidateWave[i]['z'][1] <= timeInterval and x[
                j] > listofCandidateWave[i]['x'][0] and wave2_fibonacci_check(x[j], listofCandidateWave[i]['x'][0],
                                                                              listofCandidateWave[i]['x'][1]):
                currWave = copy.deepcopy(listofCandidateWave[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave12.append(currWave)

            # end
        # end
    # end
    print(len(listofCandidateWave12))
    print('successfully filter out candidate wave 12')
    listofCandidateWave123 = []
    for i in range(len(listofCandidateWave12)):
        startSearchIndex = listofCandidateWave12[i]['searchIndex']
        # forth point should be within 1.618+-5%? we take 1.618+*1.05=1.6989
        timeInterval = (listofCandidateWave12[i]['z'][1] - listofCandidateWave12[i]['z'][0]) * 1.6989
        for j in range(startSearchIndex, len(x)):
            # wave 3 is a rise and point should at around 1.618 and wave 3 must be the longest wave
            if x[j] > listofCandidateWave12[i]['x'][2] and z[j] - listofCandidateWave12[i]['z'][2] <= timeInterval and \
                    z[j] - listofCandidateWave12[i]['z'][2] >= listofCandidateWave12[i]['z'][1] - \
                    listofCandidateWave12[i]['z'][0] and z[j] - listofCandidateWave12[i]['z'][2] >= \
                    listofCandidateWave12[i]['z'][2] - listofCandidateWave12[i]['z'][1] and wave3_fibonacci_check(x[j],
                                                                                                                  listofCandidateWave12[
                                                                                                                      i][
                                                                                                                      'x'][
                                                                                                                      1],
                                                                                                                  listofCandidateWave12[
                                                                                                                      i][
                                                                                                                      'x'][
                                                                                                                      2]):
                currWave = copy.deepcopy(listofCandidateWave12[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave123.append(currWave)

            # end
        # end
    # end
    print(len(listofCandidateWave123))
    print('successfully filter out candidate wave123')

    listofCandidateWave1234 = []
    for i in range(len(listofCandidateWave123)):
        startSearchIndex = listofCandidateWave123[i]['searchIndex']
        # forth point should be within 0.382+-5%? we take 0.382+*1.05=0.4011
        timeInterval = (listofCandidateWave123[i]['z'][1] - listofCandidateWave123[i]['z'][0]) * 0.4011
        wave3length = listofCandidateWave123[i]['z'][3] - listofCandidateWave123[i]['z'][2]
        for j in range(startSearchIndex, len(x)):
            # wave 4 is a fall and point should at around 1.618 and wave 4 must not fall below the end of wave 1
            if x[j] < listofCandidateWave123[i]['x'][3] and z[j] - listofCandidateWave123[i]['z'][3] <= timeInterval and \
                    x[j] > listofCandidateWave123[i]['x'][1] and z[j] - listofCandidateWave123[i]['z'][
                3] <= wave3length and wave4_fibonacci_check(x[j], listofCandidateWave123[i]['x'][2],
                                                            listofCandidateWave123[i]['x'][3]):
                currWave = copy.deepcopy(listofCandidateWave123[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave1234.append(currWave)

            # end
        # end
    # end

    print(len(listofCandidateWave1234))
    print('successfully filter out candidate wave1234')

    return listofCandidateWave1234
########################################
